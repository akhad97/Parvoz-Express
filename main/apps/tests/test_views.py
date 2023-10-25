# import pytest 
# from django.urls import reverse
# from rest_framework import status 
# import uuid

# @pytest.fixture
# def manager_create_data(request):
#     data = {
#         'complete-data': (
#             status.HTTP_201_CREATED,
#             {
#                 'full_name': 'Sardor Salimov',
#                 'nickname': 'solih',
#                 'city': 'Namangan',
#                 'phone_number': 1234567,
#                 'price': 7000,
#                 'password': 'test-pass',
#                 'is_acitve': True
#             }
#         )
#     }
#     return data[request.param]

# @pytest.mark.django_db
# @pytest.mark.parametrize('manager_create_data', [
#     'complete-data'
# ], indirect=True)
# def test_manager_create(manager_create_data, client):
#     url = reverse('employee:manager_create') 
#     status_code, data = manager_create_data  
#     response = client.post(url, data=data) 
#     assert response.status_code == status_code




# @pytest.fixture
# def manager_update_data(request, manager_factory):
#     manager = manager_factory.create(
#         full_name='akhad abdullaev', 
#         price=2500,
#         city='Tashkent',
#         phone_number=1234567,
#         nickname='alish',
#         password='pass'
#         )
#     data = {
#         'complete-data': (
#             status.HTTP_200_OK, manager,
#             {
#                 'full_name': 'akhad abdullaev',  
#                 'nickname': 'updated-nickname',
#                 'city': 'Updated City',
#                 'phone_number': 9876543,
#                 'price': 8000, 
#                 'password': 'updated-pass', 
#                 'is_active': False 
#             }
#         ),
#     }
#     return data[request.param]


# @pytest.mark.django_db
# @pytest.mark.parametrize('manager_update_data', [
#     'complete-data'
# ], indirect=True)
# def test_manager_update(manager_update_data, client):
#     status_code, instance, data = manager_update_data  
#     url = reverse('employee:manager_update', kwargs={'guid':instance.guid}) 

#     response_patch = client.patch(url, data=data, content_type='application/json') 
#     response_put = client.put(url, data=data, content_type='application/json')

#     assert response_patch.status_code == status_code
#     assert response_put.status_code == status_code

#     if response_patch.status_code == status.HTTP_200_OK:
#         assert response_patch.json()
#     if response_put.status_code == status.HTTP_200_OK:
#         assert response_put.json()




# @pytest.fixture
# def manager_detail_data(request, manager_factory):
#     manager = manager_factory.create(
#         full_name='akhad abdullaev', 
#         price=2500,
#         city='Tashkent',
#         phone_number=1234567,
#         nickname='alish',
#         password='pass' 
#         )
#     data = {
#         'complete-data': (
#             status.HTTP_200_OK, manager
#         )
#     }
#     return data[request.param]


# @pytest.mark.django_db
# @pytest.mark.parametrize('manager_detail_data', [
#     'complete-data'
# ], indirect=True)
# def test_manager_detail(manager_detail_data, client):
#     status_code, instance = manager_detail_data  
#     url = reverse('employee:manager_detail', kwargs={'guid':instance.guid}) 
#     response = client.get(url)
#     assert response.status_code == status_code
#     if response.status_code == status.HTTP_200_OK:
#         assert response.json()



# @pytest.fixture
# def manager_delete_data(request, manager_factory):
#     manager = manager_factory.create(
#         full_name='akhad abdullaev', 
#         price=2500,
#         city='Tashkent',
#         phone_number=1234567,
#         nickname='alish',
#         password='pass'
#         )
#     data = {
#         'complete-data': (
#             status.HTTP_204_NO_CONTENT, manager
#         )
#     }
#     return data[request.param]


# @pytest.mark.django_db
# @pytest.mark.parametrize('manager_delete_data', [
#     'complete-data'
# ], indirect=True)
# def test_manager_delete(manager_delete_data, client):
#     status_code, instance = manager_delete_data  
#     url = reverse('employee:manager_delete', kwargs={'guid':instance.guid}) 
#     response = client.delete(url)
#     assert response.status_code == status_code
#     if response.status_code == status.HTTP_200_OK:
#         assert response.json()
