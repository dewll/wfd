from back.models import User, StationRequest
import pytest
import json



@pytest.mark.django_db
def test_user_signup(client,user_data):
    headers = {
            "Content-Type": "application/json;charset=UTF-8"
        }
    assert User.objects.count() == 0
    resp = client.post('/api/users', data =user_data, headers=headers)
    assert User.objects.count() == 1
    assert resp.status_code == 201

@pytest.mark.django_db
def test_station_form(client,request_station_data):
    headers = {
            "Content-Type": "application/json;charset=UTF-8"
        }
    assert StationRequest.objects.count() == 0
    resp = client.post('/api/users', data =request_station_data, headers=headers)
    assert StationRequest.objects.count() == 1
    assert resp.status_code == 201

#TESTING FOR DEFAULT USER LOGIN   
@pytest.mark.django_db
def test_default_user_login(client, create_test_user, user_data):
    headers = {
            "Content-Type": "application/json;charset=UTF-8"
        }
    assert User.objects.count() == 1
    resp = client.post('/api/signin', data =user_data, headers=headers)
    assert resp.status_code == 200


#TESTING FOR APPROVED STATION LOGIN    
@pytest.mark.django_db
def test_approved_station_login(client, create_approve_station_user, approved_staion_data):
    headers = {
            "Content-Type": "application/json;charset=UTF-8"
        }
    data = {"email":"user1@email.com","username":"balo", "password":"user1@email.com"}
    assert User.objects.count() == 1
    resp = client.post('/api/signin', data =data, headers=headers)
    assert resp.status_code == 200
      
@pytest.mark.django_db
def test_user_home(client, authentication_token):
    headers = {
        'Http_Accept': '*/*',
        'HTTP_AUTHORIZATION': f'Bearer {authentication_token}'
    }
    resp = client.get('/api/home', headers=headers )
    r = resp.json()
    print(r)
    assert resp.status_code == 200