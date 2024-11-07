import environ
import os

# Определяем путь к корню проекта
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Инициализация переменных окружения
env = environ.Env()
env_file = os.path.join(BASE_DIR, '.env')

# Проверяем наличие .env и читаем его
if os.path.exists(env_file):
    environ.Env.read_env(env_file)

# Настройка секретного ключа и других переменных
SECRET_KEY = env('SECRET_KEY', default='default_secret_key')
DEBUG = env.bool('DEBUG', default=False)
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=[])
DATABASES = {
    'default': env.db('DATABASE_URL', default='sqlite:///db.sqlite3')
}

ROOT_URLCONF = 'ptm_310524_slavaGon4ar.urls'  # Замените 'ptm_310524_slavaGon4ar' на имя вашего проекта

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # Добавьте пути к вашим шаблонам, если они есть
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',  # Для сессий
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Для аутентификации
    'django.contrib.messages.middleware.MessageMiddleware',  # Для сообщений
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


INSTALLED_APPS = [
    'django.contrib.admin',         # Для панели администрирования
    'django.contrib.auth',          # Для аутентификации пользователей
    'django.contrib.contenttypes',  # Для управления типами контента
    'django.contrib.sessions',       # Для сессий пользователей
    'django.contrib.messages',       # Для системы сообщений
    'django.contrib.staticfiles',    # Для статических файлов

    # Добавьте другие ваши приложения здесь
    'my_app',  # Например, ваше основное приложение
]

STATIC_URL = '/static/'  # URL для доступа к статическим файлам
