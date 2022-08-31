## REGISTRATION FOR STATION REQUEST

‘https://wfdap.herokuapp.com/api/users’

##### Request body

```plaintext

{
"email": "string",
"phone": "string",
"station_name": "string",
"fullname": "string",
"location": "string",
"state": "string",
"reg_num": int
}
```

##### Response body

status code 201

```plaintext

body ={
"message": "Form submitted Successfully "
}
```

## REGISTRATION FOR SUPER ADMIN

‘https://wfdap.herokuapp.com/api/users’

##### Request body

```plaintext

{
"email": "string",
"password": "string"
}
```

##### Response body

status code 201

```plaintext

body = {
"message": "Registration Successfull for SuperAdmin"
}
```

## LOGIN

‘https://wfdap.herokuapp.com/api/signin’

##### Request body

```plaintext

{
"email": "string",
"password": "string"
}
```

##### Response body

status code = 200

```plaintext

body = {
"access": "string"
}
```

## PROTECTED ENDPOINT

'https://wfdap.herokuapp.com/api/home'

##### Request body

nothing

##### Response body

```plaintext

if valid token the response will be 200 satus
{
"message": "the user email"
}
if invalid token the response will be 401 status
{
"detail": "Unauthorized"
}
```
