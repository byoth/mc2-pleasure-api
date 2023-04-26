# README

## 시작하기

### 가상환경

- python3 -m venv env
- source env/bin/activate
- deactivate

### 패키지

- pip install --upgrade pip
- pip install <package_name>
- pip freeze > requirements.txt
- pip install -r requirements.txt

### 구조 생성

- django-admin startproject <project_name>
- django-admin startapp <model_name>

### 마이그레이션

- python manage.py makemigrations
- python manage.py migrate