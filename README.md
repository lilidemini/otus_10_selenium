# Домашняя работа 
1. установить библиотеки из requirements.txt
pip install -r requirements.txt

# ALARM: используется webdriver-manager, 
# который автоматически скачивает драйвер для браузеров
__________________________________
2. запустить в docker приложение Opencart
__________________________________
3. запустить автотесты на страницах:
Главная 
pytest -v -m main

Каталог 
pytest -v -m catalog

Карточки товаров 
pytest -v -m product

Страница логина в админку 
pytest -v -m login

Страница регистрации пользователя 
pytest -v -m register

