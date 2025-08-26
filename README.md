# Django Mini Project with Yandex Object Storage

Это минимальный Django проект для загрузки фотографий в Яндекс Object Storage с админкой для управления.  

---

## Функциональность

- Загрузка фотографий через Django Admin
- Файлы сохраняются **только в Yandex Object Storage**
- Статические файлы и админка работают локально
- Удаление модели через админку удаляет файлы из облака
- Минимальная структура проекта, легко расширять

---

## Установка и запуск

1. Клонируйте репозиторий:

```bash
git clone https://github.com/Largasson/Django_remote_stoarge.git
cd Django_cloud_storage
```

2. Создайте и активируйте виртуальное окружение:
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux / MacOS
source .venv/bin/activate

```
3. Установите зависимости:
```bash
pip install -r requirements.txt

```
4. Выполните миграции:
```bash
python manage.py migrate        
```
5. Запустите сервер разработки:
```bash
python manage.py runserver
```
6. Откройте админку по адресу http://127.0.0.1:8000/admin/

Логин для админки: admin
Пароль: 12345

Файл .env по запросу
