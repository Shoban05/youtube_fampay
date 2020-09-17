# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

# PostgreSQL database
DB_HOST = 'localhost'
DB_PORT = '5432'
DB_USER = 'fampay'
DB_PASSWORD = 'fampay'
DB_NAME = 'fampay'

DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql_psycopg2',
       'NAME': DB_NAME,
       'USER': DB_USER,
       'PASSWORD': DB_PASSWORD,
       'HOST': DB_HOST,
       'PORT': DB_PORT,
   }
}