from .base import app
from .login_required import login_required
from utils.filetransfer import *
<<<<<<< HEAD
=======
from fastapi import APIRouter

task_router = APIRouter(prefix='/task')
>>>>>>> dev

@app.get('/tasks')
@login_required
async def tasks():
    return 'api: tasks'

<<<<<<< HEAD
@app.get('/task/<id>')
=======
@task_router.get('/')
>>>>>>> dev
@login_required
def task(id):
    return 'requested task with id ' + str(id)

<<<<<<< HEAD
@app.post(
    '/upload_task',
=======
@task_router.post(
    '/upload',
>>>>>>> dev
)
async def upload_task(in_file: UploadFile, data: str):
    upload_file(in_file, 'upload.test')


<<<<<<< HEAD
@app.get(
    '/download_results',
=======
@task_router.get(
    '/download',
>>>>>>> dev
)
async def download_results():
    return await download_file('main.py')
