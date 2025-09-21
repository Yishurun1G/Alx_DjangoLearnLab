
INSTALLED_APPS = [
    ...
    'accounts',
    'django.contrib.admin',
    'django.contrib.auth',
    'accounts',
    'bookshelf',
    ...
]

AUTH_USER_MODEL = 'accounts.CustomUser'

# Media files (profile photos)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
