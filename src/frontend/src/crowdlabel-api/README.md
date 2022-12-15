# crowd_label_api

CrowdLabelApi - JavaScript client for crowd_label_api
API for CrowdLabel
This SDK is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 0.1.0
- Package version: 0.1.0
- Build package: org.openapitools.codegen.languages.JavascriptClientCodegen

## Installation

### For [Node.js](https://nodejs.org/)

#### npm

To publish the library as a [npm](https://www.npmjs.com/), please follow the procedure in ["Publishing npm packages"](https://docs.npmjs.com/getting-started/publishing-npm-packages).

Then install it via:

```shell
npm install crowd_label_api --save
```

Finally, you need to build the module:

```shell
npm run build
```

##### Local development

To use the library locally without publishing to a remote npm registry, first install the dependencies by changing into the directory containing `package.json` (and this README). Let's call this `JAVASCRIPT_CLIENT_DIR`. Then run:

```shell
npm install
```

Next, [link](https://docs.npmjs.com/cli/link) it globally in npm with the following, also from `JAVASCRIPT_CLIENT_DIR`:

```shell
npm link
```

To use the link you just defined in your project, switch to the directory you want to use your crowd_label_api from, and run:

```shell
npm link /path/to/<JAVASCRIPT_CLIENT_DIR>
```

Finally, you need to build the module:

```shell
npm run build
```

#### git

If the library is hosted at a git repository, e.g.https://github.com/GIT_USER_ID/GIT_REPO_ID
then install it via:

```shell
    npm install GIT_USER_ID/GIT_REPO_ID --save
```

### For browser

The library also works in the browser environment via npm and [browserify](http://browserify.org/). After following
the above steps with Node.js and installing browserify with `npm install -g browserify`,
perform the following (assuming *main.js* is your entry file):

```shell
browserify main.js > bundle.js
```

Then include *bundle.js* in the HTML pages.

### Webpack Configuration

Using Webpack you may encounter the following error: "Module not found: Error:
Cannot resolve module", most certainly you should disable AMD loader. Add/merge
the following section to your webpack config:

```javascript
module: {
  rules: [
    {
      parser: {
        amd: false
      }
    }
  ]
}
```

## Getting Started

Please follow the [installation](#installation) instruction and execute the following JS code:

```javascript
var CrowdLabelApi = require('crowd_label_api');


var api = new CrowdLabelApi.AuthApi()
var username = "username_example"; // {String} 
var password = "password_example"; // {String} 
var opts = {
  'grantType': "grantType_example", // {String} 
  'scope': "''", // {String} 
  'clientId': "clientId_example", // {String} 
  'clientSecret': "clientSecret_example" // {String} 
};
var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
api.loginLoginPost(username, password, opts, callback);

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*CrowdLabelApi.AuthApi* | [**loginLoginPost**](docs/AuthApi.md#loginLoginPost) | **POST** /login | Login
*CrowdLabelApi.AuthApi* | [**tokenTokenPost**](docs/AuthApi.md#tokenTokenPost) | **POST** /token | Token
*CrowdLabelApi.QuestionsApi* | [**createAnswerQuestionsPost**](docs/QuestionsApi.md#createAnswerQuestionsPost) | **POST** /questions | Create Answer
*CrowdLabelApi.QuestionsApi* | [**getQuestionQuestionsQuestionsQuestionIdGet**](docs/QuestionsApi.md#getQuestionQuestionsQuestionsQuestionIdGet) | **GET** /questions/questions/{question_id} | Get Question
*CrowdLabelApi.TasksApi* | [**claimTaskTasksTaskIdClaimPost**](docs/TasksApi.md#claimTaskTasksTaskIdClaimPost) | **POST** /tasks/{task_id}/claim | Claim Task
*CrowdLabelApi.TasksApi* | [**deleteTaskTasksTaskIdDelete**](docs/TasksApi.md#deleteTaskTasksTaskIdDelete) | **DELETE** /tasks/{task_id} | Delete Task
*CrowdLabelApi.TasksApi* | [**downloadTaskResultsTasksTaskIdDownloadGet**](docs/TasksApi.md#downloadTaskResultsTasksTaskIdDownloadGet) | **GET** /tasks/{task_id}/download | Download Task Results
*CrowdLabelApi.TasksApi* | [**editTaskTasksTaskIdPatch**](docs/TasksApi.md#editTaskTasksTaskIdPatch) | **PATCH** /tasks/{task_id} | Edit Task
*CrowdLabelApi.TasksApi* | [**getTaskTasksTaskIdGet**](docs/TasksApi.md#getTaskTasksTaskIdGet) | **GET** /tasks/{task_id} | Get Task
*CrowdLabelApi.TasksApi* | [**searchTasksTasksGet**](docs/TasksApi.md#searchTasksTasksGet) | **GET** /tasks/ | Search Tasks
*CrowdLabelApi.TasksApi* | [**uploadTaskTasksUploadPost**](docs/TasksApi.md#uploadTaskTasksUploadPost) | **POST** /tasks/upload | Upload Task
*CrowdLabelApi.UsersApi* | [**availabilityUsersAvailabilityPut**](docs/UsersApi.md#availabilityUsersAvailabilityPut) | **PUT** /users/availability | Availability
*CrowdLabelApi.UsersApi* | [**editMeUsersMePatch**](docs/UsersApi.md#editMeUsersMePatch) | **PATCH** /users/me | Edit Me
*CrowdLabelApi.UsersApi* | [**getMeUsersMeGet**](docs/UsersApi.md#getMeUsersMeGet) | **GET** /users/me | Get Me
*CrowdLabelApi.UsersApi* | [**getUserUsersUsernameGet**](docs/UsersApi.md#getUserUsersUsernameGet) | **GET** /users/{username} | Get User
*CrowdLabelApi.UsersApi* | [**registerUsersRegisterPost**](docs/UsersApi.md#registerUsersRegisterPost) | **POST** /users/register | Register
*CrowdLabelApi.UsersApi* | [**verifyEmailUsersVerifyEmailPost**](docs/UsersApi.md#verifyEmailUsersVerifyEmailPost) | **POST** /users/verify-email | Verify Email


## Documentation for Models

 - [CrowdLabelApi.Answer](docs/Answer.md)
 - [CrowdLabelApi.AvailabilityRequest](docs/AvailabilityRequest.md)
 - [CrowdLabelApi.AvailabilityResponse](docs/AvailabilityResponse.md)
 - [CrowdLabelApi.BodyCreateAnswerQuestionsPost](docs/BodyCreateAnswerQuestionsPost.md)
 - [CrowdLabelApi.Email](docs/Email.md)
 - [CrowdLabelApi.ErrorResponse](docs/ErrorResponse.md)
 - [CrowdLabelApi.HTTPValidationError](docs/HTTPValidationError.md)
 - [CrowdLabelApi.LocationInner](docs/LocationInner.md)
 - [CrowdLabelApi.Question](docs/Question.md)
 - [CrowdLabelApi.RegistrationError](docs/RegistrationError.md)
 - [CrowdLabelApi.RegistrationRequest](docs/RegistrationRequest.md)
 - [CrowdLabelApi.Task](docs/Task.md)
 - [CrowdLabelApi.TaskSearchRequest](docs/TaskSearchRequest.md)
 - [CrowdLabelApi.TaskSearchResponse](docs/TaskSearchResponse.md)
 - [CrowdLabelApi.Token](docs/Token.md)
 - [CrowdLabelApi.User](docs/User.md)
 - [CrowdLabelApi.ValidationError](docs/ValidationError.md)


## Documentation for Authorization



### OAuth2PasswordBearer


- **Type**: OAuth
- **Flow**: password
- **Authorization URL**: 
- **Scopes**: N/A
