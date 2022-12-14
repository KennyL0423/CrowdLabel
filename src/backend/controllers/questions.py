from fastapi import status
from .base import app
import services.questions as qs
import services.tasks as ts
from fastapi import APIRouter, Path
import schemas.tasks
import schemas.questions
from .jsondocumentedresponse import JSONDocumentedResponse, create_documentation
from . import tasks as tc
import services.questions

from .auth import Depends, get_current_user

router = APIRouter()

""" @router.get('/questions')
async def questions():
    return 'api: questions'

@app.post('/create_question_from_file')
async def create_question_from_file(details:FilePath):
    response = await services.question.create_question_from_file(
        details.id,
        details.path,
        )
    if response['status'] != 'ok':
        return {
            'error': f'{response} already exists'
        }, 400
    else:
        return {
            'status':'ok'
        }, 200

@app.post('/create_question')
async def create_question(details:QuestionInfo):
    response = await services.question.create_question(
        details.type,
        details.prompt,
        details.resource,
        details.options,
        details.task_id
    )
    if response != 'ok':
        return {
            'error': f'{response} already exists'
        }, 400
    else:
        return {
        "type":details.type,
        "prompt":details.prompt,
        "resource":details.resource,
        "options":details.options,
        "task_id":details.task_id
        }, 200
@router.delete('/questions')
async def delete_question(details:ID):
    response = await services.question.delete_question(details.id)
    if response[0]['status'] != 'ok':
        return {
            'error' : f'delete failed'
        },400
    else :
        return {
            'id':details.id
        },200
@router.post('/edit_question')
async def edit_question(details:IDWithQuestionInfo):
    response = await services.question.edit_question(
        details.id,
        details.type,
        details.prompt,
        details.resource,
        details.options,
        details.task_id
    )
    if response[0]['status'] != 'ok':
        return {
            'error': 'edit failed'
        },400
    else:
        return {
            "type":response[0]["type"],
            "prompt":response[0]["prompt"],
            "resource":response[0]["resource"],
            "options":response[0]["options"],
            "task_id":response[0]["task_id"]
            
        } """


question_not_found_error = JSONDocumentedResponse(
    status.HTTP_404_NOT_FOUND,
    'Question not found'
)
@router.get('/questions/{question_id}',
    **create_documentation([question_not_found_error])
)
async def get_question(question_id: int, task=Depends(tc.get_task), current_user=Depends(get_current_user)):

    question = await qs.get_question(task, question_id)
    if not question:
        return question_not_found_error.response()
    
    return question


create_answer_success = JSONDocumentedResponse(
    status.HTTP_200_OK,
    'Answer created successfully. Answer is returned',
    schemas.questions.Answer,
)
create_answer_failed = JSONDocumentedResponse(
    status.HTTP_400_BAD_REQUEST,
    'Answer not created. Error message is returned',
    schemas.tasks.ErrorResponse,
)
@router.post('',
    **create_documentation([create_answer_success, create_answer_failed])
)
async def create_answer(answer: schemas.questions.Answer, task_id: int=Path(), question_id: int=Path(), current_user=Depends(get_current_user)):
    response = services.questions.create_answer(current_user, task_id, question_id, answer)
    if response:
        return create_answer_failed.response(schemas.tasks.ErrorResponse(response))    
    return create_answer_success.response(answer)