from fastapi import Depends, UploadFile, status
from fastapi.routing import APIRouter
from utils.filetransfer import download_file, upload_file
from .auth import get_current_user
import services.tasks
import services.users
from .jsondocumentedresponse import JSONDocumentedResponse, create_documentation, forbidden_jdr, not_found_jdr
import schemas.tasks
import schemas.questions
from utils.datetime_str import datetime_now_str
from typing import Optional
from utils.config import get_config
import pathlib

TASK_UPLOAD_DIR = pathlib.Path(get_config('file_locations.tasks'))
router = APIRouter()
task_service = services.tasks.Tasks()


###############################################################################
get_task_success_jdr = JSONDocumentedResponse(
    status.HTTP_200_OK,
    'Successfully queried tasks.',
    schemas.tasks.TaskSearchResponse
)
get_task_failed_hdr = JSONDocumentedResponse(
    status.HTTP_400_BAD_REQUEST,
    'Task query failed.',
    schemas.tasks.ErrorResponse
)
@router.put('/',
    description=task_service.search.__doc__ + schemas.tasks.TaskSearchRequest.__doc__,
    **create_documentation([get_task_success_jdr, get_task_failed_hdr])
)
async def search_tasks(query: schemas.tasks.TaskSearchRequest, current_user=Depends(get_current_user(['respondent']))):
    """
    Task search
    """
    # TODO: complete arguments
    tasks = await task_service.search(current_user, query)
    print('#' * 80)
    print(tasks)
    if isinstance(tasks, str):
        return get_task_failed_hdr.response(schemas.tasks.ErrorResponse(tasks))

    # exclude tasks.questions
    return get_task_success_jdr.response(schemas.tasks.TaskSearchResponse(tasks=tasks[0], total=tasks[1]), exclude={'questions'})
###############################################################################
upload_success_jdr = JSONDocumentedResponse(
    status.HTTP_200_OK,
    'Task uploaded and created successfully',
    list[schemas.questions.Question]
)
upload_failed_jdr = JSONDocumentedResponse(
    status.HTTP_400_BAD_REQUEST,
    'Task not created',
    schemas.tasks.ErrorResponse
)
@router.post('/upload',
    **create_documentation([upload_success_jdr, upload_failed_jdr])
)
async def upload_task(task_file: UploadFile, current_user=Depends(get_current_user(['requester']))):
    out_path = TASK_UPLOAD_DIR / ('upload_' + current_user.username + '_' + datetime_now_str() + '.zip')
    await upload_file(task_file, out_path)
    task = await task_service.process_task_archive(out_path)
    if isinstance(task, str):
        return upload_failed_jdr.response(schemas.tasks.ErrorResponse(error=task))
    task = await task_service.create_task(current_user, task, out_path)
    if isinstance(task, str):
        return upload_failed_jdr.response(schemas.tasks.ErrorResponse(error=task))

    return upload_success_jdr.response(task)
###############################################################################




""" create_task_success_jdr = JSONDocumentedResponse(
    status.HTTP_201_CREATED,
    'Task created successfully',
    schemas.tasks.Task
)
create_task_failed_jdr = JSONDocumentedResponse(
    status.HTTP_400_BAD_REQUEST,
    'Task not created',
    schemas.tasks.ErrorResponse
)
@router.post('/create',
    **create_documentation([create_task_success_jdr, create_task_failed_jdr])
)
async def create_task(task: schemas.tasks.CreateTaskRequest, questions_file: UploadFile,

    current_user=Depends(get_current_user(['requester']))
):

    cover_filename = 'cover_' + current_user.username + datetime_now_str() + '.png'
    questions_filename = 'questions_' + current_user.username + datetime_now_str() + '.zip'

    await upload_file(questions_file, questions_filename)

    #questions = await task_service.process_task_archive(questions_filename)

    result = await task_service.create_task(
        creator=current_user,
        name=task.name,
        description=task.description,
        introduction=task.introduction,
        cover_filename=cover_filename if cover else None,
        responses_required=task.responses_required,
        credits=task.credits,
    )

    if not isinstance(result, schemas.tasks.Task):
        return create_task_failed_jdr(schemas.tasks.ErrorResponse(result))

    if cover:
        await upload_file(cover, 'cover_' + current_user.username + datetime_now_str() + '.png') """









###############################################################################
get_task_success_jdr = JSONDocumentedResponse(
    status.HTTP_200_OK,
    'Task found successfully.',
    schemas.tasks.Task,
)
@router.get('/{task_id}',
    description='Get a task based on its task_id',
    **create_documentation([get_task_success_jdr, not_found_jdr, forbidden_jdr])    
)
async def get_task(task_id: int, current_user=Depends(get_current_user())):
    task = await task_service.get_task(task_id=task_id)
    if not task:
        return {'description': 'Task not found'}, status.HTTP_404_NOT_FOUND

    return task

###############################################################################
task_delete_success_jdr = JSONDocumentedResponse(
    status.HTTP_200_OK,
    'Task deleted successfully',
)
@router.delete('/{task_id}',
    **create_documentation([task_delete_success_jdr, forbidden_jdr, not_found_jdr])
)
async def delete_task(task_id: int, current_user=Depends(get_current_user(['requester']))):
    task = await task_service.get_task(task_id)
    if not task:
        return not_found_jdr.response()
    response = await task_service.delete_task(task_id)
    if response == 'forbidden':
        return forbidden_jdr.response()
    return task_delete_success_jdr.response()
###############################################################################
claim_success_jdr = JSONDocumentedResponse(
    status.HTTP_200_OK,
    'Task claimed successfully.',
    schemas.tasks.Task,
)
claim_failed_jdr = JSONDocumentedResponse(
    status.HTTP_400_BAD_REQUEST,
    'Task claim failed.',
    schemas.tasks.ErrorResponse,
)
@router.post('/{task_id}/claim',
    **create_documentation([claim_success_jdr, claim_failed_jdr])
)
async def claim_task(task_id: int, current_user=Depends(get_current_user(['respondent']))):
    task = await task_service.claim_task(current_user.username,task_id)

    return claim_success_jdr.response(task)
###############################################################################

@router.get('/{task_id}/download',)
async def download_task_results(task_id: int, current_user=Depends(get_current_user(['requester']))):
    filename = await task_service.create_task_results_file(task_id)
    return await download_file(filename)
###############################################################################

@router.patch('/{task_id}')
async def edit_task(task_id: int, current_user=Depends(get_current_user)):
    return 'editing task ' + str(task_id)
###############################################################################
