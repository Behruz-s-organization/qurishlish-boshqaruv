# Qurilish Boshqaruv Backend Saas (Software as a Service)

## Loyihani Run qilish ketma-ketligi
``` bash
cp .env.example .env # .env fileda kerakli maydonlarni toldirish kerak
```
``` bash
docker-compose up --build -d
```

## Client qo'shish
``` bash
docker exec -it <container_name> bash

python manage.py createclient
```

## SuperUser yaratish uchun
``` bash
python manage.py createuser
```
- Schema name: -> client qoshishda kiritgan schema name.
- Username: -> login qilish uchun username.
- First name: -> Ism (shart emas).
- Last name: -> Familiya (shart emas).
- Phone number: -> Telefon raqam (shart emas).
- Password: -> login qilish uchun parol.