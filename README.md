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