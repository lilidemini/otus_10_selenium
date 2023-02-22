# Домашняя работа 
1. установить библиотеки из requirements.txt
pip install -r requirements.txt
__________________________________
2. запустить в docker приложение Opencart
__________________________________
3. запустить автотесты на страницах:
Главная 
pytest -v -m Main

Каталог 
pytest -v -m Catalog

Карточки товаров 
pytest -v -m Product

Страница логина в админку 
pytest -v -m Login

Страница регистрации пользователя 
pytest -v -m Register

