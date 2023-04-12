from page_objects.base_page import BasePage
from faker import Faker


class NewUser(BasePage):
    fake = Faker('ru_RU')
    NEW_USER_FIRST_NAME = fake.first_name()
    NEW_USER_LAST_NAME = fake.last_name()
    NEW_USER_EMAIL = fake.email()
    NEW_USER_PASSWORD = 'qwerty'

class AdminCredentials(BasePage):
    ADMIN_USERNAME = 'user'
    ADMIN_PASSWORD = 'bitnami'
