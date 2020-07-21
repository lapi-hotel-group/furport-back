SECRET_KEY = "xxxxx"
DEBUG = True
ALLOWED_HOSTS = ["localhost"]
CORS_ORIGIN_WHITELIST = ["http://localhost:3000"]

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "django",
        "USER": "django",
        "PASSWORD": "password",
        "HOST": "postgres",
        "PORT": 5432,
    }
}

EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_HOST_USER = "sample@gmail.com"
EMAIL_HOST_PASSWORD = "passwd"
EMAIL_USE_TLS = True
