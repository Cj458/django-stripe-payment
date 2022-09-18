# django-stripe-payment


Чтобы запускать этот проект в localhost:

## Чтобы запускать этот проект в localhost:

Используйте менеджер пакетов [pip](https://pip.pypa.io/en/stable/), чтобы установить pipenv.

```bash
pipe install pipenv
```

клонировать репо

Запустить команду pipenv install, чтобы создать виртуальную среду и установить все зависимости

```terminal
pipenv install 
```

сделать миграцию с помощью команды python manage.py makemigrations

```terminal
python manage.py makemigrations
```

создать администратора

```terminal
python manage.py createsuperuser
```

создать Item в админке


в settings.py заполните STRIPE_PUBLIC_KEY и STRIPE_SECRET_KEY своими ключами



## P.S

Запуск с Docker пока не работает, но работаю над этим


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[CALEB](https://calebjason.herokuapp.com/)