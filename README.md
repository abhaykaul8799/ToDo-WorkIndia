
## To Do Application Backend using REST API.

START BY RUNNING <python web.py> in terminal.


SQL ENGINE USED = MYSQL

DATABASE NAME = main

DATABASE SCHEMA =>

    agent (id<varchar>,password<varchar>)
    
    tasks (taskid<int><pk>,id<varchar>,title<varchar>,description<varchar>,category<varchar>,due_date<date>)

API CALLS SUPPORTED =>

[POST] /app/agent/

Request Data: {
    'agent_id': str,
    'password': str
}

If successful,

Response Data: {
    'status':'account created',
    'status_code': 200
}

else

Response Data: {
    'status':'failure',
    'status_code': 401
}

__________________________________________________

[POST] /app/agent/auth

Request Data: {
    'agent_id': str,
    'password': str
}

// PASSWORD STORED IN A SALTED HASH FORMAT

If successful,

Response Data: {
    'status': 'success',
    'agent_id': str,
    'status_code': 200
}

else

Response Data: {
    'status':'failure',
    'status_code': 401
}

__________________________________________________

[GET] /app/sites/list/

Request Data: {
    'agent': str
}

Response Data: {
    LIST OF TASKS
}

__________________________________________________

[POST] /app/sites/

Request Data: {
    'title': str,
    'description': str,
    'category': str,
    'due_date': date
}

// DATE FORMAT USED IS YYYY-MM-DD

Response Data: {
    'status': 'success',
    'status_code': 200
}
