from .base import *
import services.user
from .login_required import login_required
<<<<<<< HEAD
from utils.emailverification import send_verification_email
from fastapi import Response
from fastapi.responses import JSONResponse
from .schemas import *


API_VERSION = 1









@app.post('/login',
    response_model=JWT,
    status_code=200,
    description='Successful login. Returns the `jwt` associated with the provided credentials.',
    responses = {
        login_error.status_code: login_error.response_doc()
    }
)
async def login(credentials: Credentials):

    jwt = await services.user.login(credentials.username, credentials.password)

    if not jwt:
        return login_error.response()

    return {'jwt': jwt}
=======
from fastapi import Response
from fastapi.responses import JSONResponse
from .schemas import *
from services.user import username_exists, email_exists, send_verification_email

@app.post('/verify_email',

)
async def verify_email(email: Email):
    """
    Sends a verification email
    Returns 
    """
    return await send_verification_email(email)


>>>>>>> dev




@app.post('/register',
<<<<<<< HEAD
    response_model=JWT,
    status_code=201,
    description='Successful registration. Returns the `jwt` associated with the newly-created account',
=======
    #response_model=JWT,
    status_code=201,
    description='Successful registration. Returns the username, email, and user_type of the newly-created account.',
>>>>>>> dev
    responses = {
        login_error.status_code: login_error.response_doc()
    }
)
async def register(details: Registration):
    # TODO: 
<<<<<<< HEAD
=======
    print(details)
>>>>>>> dev
    response = services.user.create_user(
        details.username,
        details.email,
        details.password,
<<<<<<< HEAD
        details.usertype)
=======
        details.user_type)
>>>>>>> dev
    if response != 'ok':
        return {
            'error': f'{response} already exists'
        }, 400

    
    else:
<<<<<<< HEAD
        return 200
=======
        return {
            'username': details.username,
            'email': details.email,
            'user_type': details.user_type,
        }, 200
>>>>>>> dev



@app.post('/availability', response_model=Availability)
async def availability(fields: Availability):
    availability = Availability()
<<<<<<< HEAD
    availability.username = 'true'
    availability.email = 'true'
=======
    try:
        availability.username = username_exists(fields.username)
    except:
        availability.username = False
    try:
        availability.email = email_exists(fields.email)
    except:
        availability.email = False
    
>>>>>>> dev
    return availability


@app.get('/user/<username>')
@login_required
async def user(username):
<<<<<<< HEAD
    return 'requested info for ' + username


@app.post('/verify')
def verify():
    username = request.form['username']
    email = request.form['email']
    verification_code = request.form['code']
    verify_email(username, email, verification_code)
=======
    return 'requested info for ' + username
>>>>>>> dev
