REGISTRATION FOR STATION MANAGER
'https://wfdap.herokuapp.com/api/users'
Request body
{
"email": "string",
"phone": "string",
"station_name": "string",
"fullname": "string",
"location": "string",
"state": "string",
"reg_num": int
}

Response body
status code 201
body ={
"message": "Registration Successfull for Station Manager"
}

REGISTRATION FOR SUPER ADMIN
'https://wfdap.herokuapp.com/api/users'
Request body
{
"email": "balosod37@gmail.com",
"password": "string",
"account_type": "T1"

}
Response body
status code 201
body = {
"message": "Registration Successfull for SuperAdmin"
}

LOGIN
'https://wfdap.herokuapp.com/api/signin'
Request body
{
"email": "string",
"password": "string"
}

Response body
status code = 200
body = {
"access": "string"
}

PROTECTED ENDPOINT
'https://wfdap.herokuapp.com/api/home'
Request body
nothing

Response body
if valid token the response will be 200 satus
{
"message": "the user email"
}

if invalid token the response will be 401 status
{
"detail": "Unauthorized"
}
