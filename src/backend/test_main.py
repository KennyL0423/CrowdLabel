import pytest

from httpx import AsyncClient

from fastapi.testclient import TestClient
from pprint import pprint
from main import app, init_models_sync
from datetime import datetime
from pathlib import Path

client = TestClient(app)


admin = {
    'username': 'admin',
    'email': 'admin@example.com',
    'password': 'secret123',
    'user_type': 'admin',
    'verification_code': '123456',
}

johndoe = {
    'username': 'johndoe',
    'email': 'johndoe@example.com',
    'password': 'secret123',
    'user_type': 'respondent',
    'verification_code': '123456',
}

req1 = {
    'username': 'req1',
    'email': 'req1@gmail.com',
    'password': 'requester123',
    'user_type': 'requester',
    'verification_code': '123456'
}

resp1 = {
    'username': 'resp1',
    'email': 'resp1@gmail.com',
    'password': 'respondent123',
    'user_type': 'respondent',
    'verification_code': '123456'
}

example_task = Path('D:/tsinghua/se 软件工程/CrowdLabel/examples/bounding.zip')
expected = {'cover_image': 'cover.jpg',
    'credits': 2.0,
    'description': 'This task is an example of a valid task',
    'introduction': 'This is an example',
    'name': 'Example task',
    'questions': [{'answers': [],
                    'options': ['Positive', 'Negative', 'Neutral', 'N/A'],
                    'prompt': 'What sentiment does this text convey',
                    'question_id': 1,
                    'question_type': 'single_choice',
                    'resource': 'text.txt'},
                {'answers': [],
                    'prompt': 'Draw a box around the person in this image',
                    'question_id': 2,
                    'question_type': 'bounding_box',
                    'resource': 'camouflage.jpeg'},
                {'answers': [],
                    'prompt': 'Transcribe the following audio recording',
                    'question_id': 3,
                    'question_type': 'open',
                    'resource': 'armstrong.mp3'},
                {'answers': [],
                    'options': ['lake', 'mountain', 'sky', 'human'],
                    'prompt': 'What objects are present in the following image',
                    'question_id': 4,
                    'question_type': 'multi_choice',
                    'resource': 'nature.jpg'},
                {'answers': [],
                    'options': ['7', '8', '9', '10'],
                    'prompt': 'Which of the following is a prime number?',
                    'question_id': 5,
                    'question_type': 'multi_choice'}],
    'requester': 'req1',
    'respondents_claimed': [],
    'respondents_completed': [],
    'responses_required': 2,
    'tags': ['object-bounding',
            'sentiment-analysis',
            'audio-transcription',
            'object-detection'],
}

def __cover(token, task_id):
    return client.get(f'/tasks/{task_id}/cover-image', headers=token)
def __availability(username=None, email=None):
    request = {}
    if username:
        request['username'] = username
    if email:
        request['email'] = email
    return client.put('/users/availability', json=request)
def __register(user):
    return client.post('/users/register', json=user)
def __login(user):
    # TODO
    response = client.post('/login', data={
        'username': user['username'],
        'password': user['password']
    })
    assert response.status_code == 200
    token = {'Authorization': f'Bearer {response.json()["access_token"]}'}
    return token
def __top_up(token, amount):
    response = client.post('/users/me/credits',
        headers=token,
        json={'amount': amount}
    )
    assert response.status_code == 200
def __get_me(token):
    return client.get('/users/me/', headers=token)
def __upload_task(token, file):
    files = {'task_file': (file.name, open(file, 'rb'))}
    response = client.post('/tasks/upload',
        headers=token,
        files=files
    )
    return response
def __claim(token, task_id):
    response = client.post(f'/tasks/{task_id}/claim', headers=token)
    return response
def __get_task(token, task_id):
    return client.get(f'/tasks/{task_id}', headers=token)
def __credits(token, amount):
    return client.post('/users/me/credits', headers=token, json={'amount': amount})
def __get_task_question_resource(token, task_id, question_id):
    return client.get(f'/tasks/{task_id}/questions/{question_id}/resource', headers=token)
def __answer(token, task_id, question_id, answer):
    return client.put(f'/tasks/{task_id}/questions/{question_id}/answer', headers=token, json=answer)
def time_in_range(time, buffer=5):
    if isinstance(time, str):
        time = datetime.strptime(time, '%Y-%m-%dT%H:%M:%S.%f')
    return abs((datetime.utcnow() - time).total_seconds()) < buffer

def compare_tasks(t1, t2,
    exclude = {
        'date_created',
    },
    sets = {
        'respondents_claimed',
        'respondents_completed',
        'tags'
    }
):
    for key in t1:
        if key in exclude:
            continue
        if key in sets:
            assert set(t1[key]) == set(t2[key])
            continue
        assert t1[key] == t2[key]

def test_get_me():
    init_models_sync()
    __register(req1)
    token = __login(req1)
    response = __get_me(token)
    assert response.status_code == 200
    json = response.json()
    for field in ['username', 'email', 'user_type']:
        assert req1[field] == json[field]
    assert 'tasks_requested' in json

    __register(johndoe)
    token2 = __login(johndoe)
    response = __get_me(token2)
    for key in ['tasks_claimed', 'tasks_completed']:
        assert key in response.json()
    
def test_register():
    init_models_sync()
    response = __register(admin)
    assert response.status_code == 201
    json = response.json()
    assert 'date_created' in json
    assert time_in_range(json['date_created'])
    del json['date_created'] # remove date_created from equality check
    expected = {
        'username': 'admin',
        'email': 'admin@example.com',
        'user_type': 'admin',
        'credits': 0,
        'tested': False,
        'tasks_claimed': [],
        'tasks_completed': [],
        'tasks_requested': []
    }
    assert json == expected
def test_login():
    init_models_sync()
    def login(user):
        return client.post('/login', data={
            'username': user['username'],
            'password': user['password']
        })
    response = login(johndoe)
    assert response.status_code == 401
    __register(johndoe)
    response = login(johndoe)
    assert response.status_code == 200
    assert 'access_token' in response.json()  
def test_availability():
    init_models_sync()
    response = __availability(req1['username'], resp1['email'])
    assert response.status_code == 200 and response.json() == {'username': True, 'email': True}
    response = __availability(req1['username'])
    assert response.status_code == 200 and response.json() == {'username': True}
    response = __availability(email=resp1['email'])
    assert response.status_code == 200 and response.json() == {'email': True}
    __register(req1)
    response = __availability(req1['username'], resp1['email'])
    assert response.status_code == 200 and response.json() == {'username': False, 'email': True}
    __register(resp1)
    response = __availability(req1['username'], resp1['email'])
    assert response.status_code == 200 and response.json() == {'username': False, 'email': False}

def test_upload():
    init_models_sync()
    __register(req1)
    token = __login(req1)
    __top_up(token, 1000)

    file = example_task
    response = __upload_task(token, file)
    print(response.status_code)
    print(response.json())
    assert response.status_code == 200
    json = response.json()
    assert 'date_created' in json
    assert time_in_range(json['date_created'])
    assert 'task_id' in json
    assert 'tags' in json

    compare_tasks(expected, json)

    response = __get_me(token)
    assert response.status_code == 200
    assert json['task_id'] in response.json()['tasks_requested']



def test_search():
    init_models_sync()
    __register(req1)
    token = __login(req1)
    __credits(token, 100)
    task1 = __upload_task(token, example_task)
    __register(johndoe)
    jd = __login(johndoe)
    response = client.put('/tasks/', headers=jd, json={})
    assert response.status_code == 200
    json = response.json()
    assert 'tasks' in json and 'total' in json
    assert json['total'] == 1 and len(json['tasks']) == 1
    response = client.put('/tasks/', headers=jd, json={'credits_min': 0, 'credits_max': 10})
    assert response.status_code == 200
    json = response.json()
    assert len(json['tasks']) == 1
def test_claim():
    init_models_sync()
    __register(johndoe)
    __register(req1)
    reqt = __login(req1)
    johnt = __login(johndoe)
    __credits(reqt, 100)
    task_id = __upload_task(reqt, example_task).json()['task_id']
    cresp = __claim(johnt, task_id)
    assert cresp.status_code == 200
    assert johndoe['username'] in __get_task(reqt, task_id).json()['respondents_claimed']
    assert task_id in __get_me(johnt).json()['tasks_claimed']
def test_credits():
    init_models_sync()
    __register(johndoe)
    token = __login(johndoe)
    assert __get_me(token).json()['credits'] == 0

    assert __credits(token, -1000).status_code == 400
    assert __get_me(token).json()['credits'] == 0

    deposit = 25.4
    assert __credits(token, deposit).status_code == 200
    assert __get_me(token).json()['credits'] == deposit

    withdraw = -12.7
    assert __credits(token, withdraw).status_code == 200
    assert __get_me(token).json()['credits'] == deposit + withdraw
def test_get_task():
    init_models_sync()
    __register(req1)
    token = __login(req1)
    __credits(token, 100)
    __credits(token, 100)
    task = __upload_task(token, example_task).json()
    response = __get_task(token, task['task_id'])
    assert response.status_code == 200
    json = response.json()
    compare_tasks(task, json)
def test_get_task_question_resource():
    init_models_sync()
    __register(req1)
    token = __login(req1)
    __credits(token, 100)
    task_id = __upload_task(token, example_task).json()['task_id']
    response = __get_task_question_resource(token, task_id, 2)
    assert response.status_code == 200
    assert response.status_code == 200
    content = response.content
    with open('../../examples/example_task/camouflage.jpeg', 'rb') as f:
        original = f.read()
    assert content == original
def test_answer():

    init_models_sync()
    __register(johndoe)
    __register(req1)
    reqt = __login(req1)
    johnt = __login(johndoe)
    __credits(reqt, 100)
    task_id = __upload_task(reqt, example_task).json()['task_id']
    cresp = __claim(johnt, task_id)   
    response = __answer(johnt, task_id, 1,
        {'choice': 1}
    )
    assert response.status_code == 200

    task = __get_task(reqt, task_id).json()
    print('#'*100)
    pprint(task)
    for question in task['questions']:
        if question['question_id'] == 1:
            assert question['answers'] == [{'choice': 1}]
            break

def test_cover():
    init_models_sync()
    __register(johndoe)
    __register(req1)
    reqt = __login(req1)
    __credits(reqt, 100)
    task_id = __upload_task(reqt, example_task).json()['task_id']
    response = __cover(reqt, task_id)
    assert response.status_code == 200
    with open('../../examples/example_task/cover.jpg', 'rb') as f:
        assert f.read() == response.content
if __name__ == '__main__':
    
    
    """ test_availability()
    test_register()
    test_login()
    test_get_me()
    test_credits()
    test_upload()
    test_get_task()
    test_claim()
    test_get_task_question_resource() 
    test_answer()
   

    test_cover() """
    
    test_search()
