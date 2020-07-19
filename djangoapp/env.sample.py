SECRET_KEY = "xxxxx"
DEBUG = True
ALLOWED_HOSTS = ["localhost"]

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
