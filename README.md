# 🪵 OakBuild — интернет-магазин мебели

**Слоган:** *Прочность товаров как дуб*

OakBuild — это современный веб-магазин мебели, написанный на Django.  
Проект предоставляет удобный интерфейс для пользователей, которые хотят выбрать, найти и заказать качественную мебель онлайн.

---

## 🚀 Возможности

- 🔐 Регистрация и личный кабинет пользователя
- 🛍️ Просмотр каталога товаров
- 🛒 Добавление товаров в корзину и оформление заказа
- 🔍 Качественный и быстрый поиск по каталогу
- 📱 Адаптивный дизайн

---

📬 Обратная связь
Если у вас есть предложения или вы нашли баг — создайте Issue или напишите автору.

---

## 🛠️ Технологии

- Python 3.11+
- Django 5.1+
- POSTGRESQL (или другая база данных)
- HTML, CSS (Bootstrap 5)
- JavaScript (для динамики)

---

## 📦 Установка и запуск проекта

Следуйте этим шагам, чтобы развернуть проект локально:

### 1. Клонировать репозиторий

```bash
git clone https://github.com/MaRi0NeTka/furniture_store-OakBuild-.git
cd furniture_store-OakBuild-
```

### 2. Создать и активировать виртуальное окружение

```bash
python -m venv venv
source venv/bin/activate   # для Linux/macOS
venv\Scripts\activate      # для Windows
```

### 3. Установить зависимости

```bash
pip install -r requirements.txt
```

### 4. Выполнить миграции базы данных

```bash
python manage.py migrate
```

### 5. Загрузить фикстуры (предустановленные данные)

```bash
python manage.py loaddata fixtures/prods.json
python manage.py loaddata fixtures/categs.json
```
### 6. Создать суперпользователя (администратора)

```bash
python manage.py createsuperuser
```

### 7. Запуск

```bash
python manage.py runserver
```
