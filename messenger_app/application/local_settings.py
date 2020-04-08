DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'messenger_app',
        'USER': 'messenger_app',
        'PASSWORD': '123',
        'HOST': '127.0.0.1',
        'PORT': '5432',
        'TEST': {
            'NAME': 'test_messenger',
            'USER': 'messenger_app',
            'PASSWORD': '123',
            'HOST': '127.0.0.1',
            'PORT': '5432',
        }
    }
}
