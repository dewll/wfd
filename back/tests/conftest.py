import pytest
from back.models import User, ApprovedStation


# FIXTURE FOR DEFAULT USER LOGIN
@pytest.fixture
def user_data():
    return{"email":"user@email.com","username":"balosod", "password":"Password123"}

@pytest.fixture
def create_test_user(user_data):
    test_user = User.objects.create_user(**user_data)
    test_user.set_password(user_data.get('password'))
    return test_user

# FIXTURE FOR APPROVED STATION LOGIN
@pytest.fixture
def create_approve_station_user():
    station_manager = User.objects.create_user(email='user1@email.com',username="balo",password ='user1@email.com',user_type ='1')
    station_manager.set_password('user1@email.com')
    return station_manager

@pytest.fixture
def approved_staion_data(create_approve_station_user):
    user = ApprovedStation.objects.create(email='user1@email.com',phone='123456789',
        station_name='bovas',
        fullname='Ojo wole',location='ibadan',
        state='oyo',business_reg_num=2,station_manager=create_approve_station_user)
    return user

@pytest.fixture
def request_station_data():
    return{"email":"user1@email.com","phone":"1234567",
           "station_name":"bovas","fullname":"Ojo wole",
           "location":"ibadan","state":"oyo",
           "business_reg_num":2}
 
@pytest.fixture
def authentication_token(client, create_test_user, user_data):
    headers = {
            "Content-Type": "application/json;charset=UTF-8"
    }
    resp = client.post('/api/signin', data =user_data, headers=headers)
    r = resp.json()['access']
    return r

