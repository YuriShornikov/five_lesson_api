#django-admin startproject lesson1 .    - создание своего проекта lesson1(название)  . - место создания, в данном случае это расположение место папки
#python manage.py runserver - запуск сервера
#./manage.py migrate - создание бд
#python manage.py startapp demo   запуск приложения с названием demo
#ctrl-Breake   - остановка работы сервера
#в созданном пакете через app в файле views.py прописывают функции для пользователя
#в пакете lesson1 в файле urls.py прописываются связи с views.py для отображения для пользователя в браузере (роутинг)
#python manage.py makemigrations в папке migrations создается файл с записями изменений
#python manage.py migrate - чтобы вступили в силу изменения
#python manage.py createsuperuser создание админки
#admin dbonlyfun@gmail.com Irregularlydgango
# views     models       urls     templates
#createdb -U postgres (название бд)
#pip install psycopg2-binary
#python manage.py createsuperuser    , далее указываем лог и пасс, которые хотим установить
#pip install djangorestframework - уствновик фреймворка
#python manage.py sell - зайти в консоль
#from demo.models import Weapon - импортируем модель в консоль
#Weapon(power=10, rarity='epic', value=100).save() - создаем в данном случае оружие
#exit() - выйти из консоли
#visual studio - устанавливаем расширение rest_client, через него открываем нашу папку, создаем файл requests.http
#в файле пишем GET http://localhost:8000/demo/      ###     POST http://localhost:8000/demo/