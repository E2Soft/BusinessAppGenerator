
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

"""
Now goes values that can be customise for your app
"""

# SECURITY WARNING: keep the secret key used in production secret!
custom_SECRET_KEY = 'x2i0y6rljb(=zf-vls(-72hv#w)6=db*fa6)ncsq6p3u)@t6yo'

#Change this if you wish that you can debug your app
custom_DEBUG = True

#Change this if you wish that you can debug your template
custom_TEMPLATE_DEBUG = True

#if debug_app is False then this list must not be empty!Represents domains that can access your app
custom_ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# Internationalization
custom_LANGUAGE_CODE = 'en-us'

custom_TIME_ZONE = 'UTC'

custom_USE_I18N = True

custom_USE_L10N = True

custom_USE_TZ = True

#used database in your app
custom_DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

