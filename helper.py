import random
import requests
from faker import Faker
from data import Urls, DataOrder

fake = Faker()
body = {
    "email": f'{fake.first_name()}_{fake.last_name()}_7_{random.randint(100, 999)}@yandex.ru',
    "password": f'{random.randint(10000, 9999999999)}',
    "name": fake.name()
}


def create_order(create_and_delete_user):
    payload, token = create_and_delete_user
    ingredient = DataOrder.INGREDIENT
    response = requests.post(f'{Urls.CREATE_ORDER}', json={"ingredients": ingredient}, headers={'Authorization': token})

    return response
