from rgd_testing_utils.settings import *  # noqa

INSTALLED_APPS += [  # noqa
    'rgd_3d',
    'rgd_fmv',
    'rgd_geometry',
    'rgd_imagery',
    # Swagger
    'drf_yasg',
    'django_extensions',
]

ROOT_URLCONF = 'rgd_example.urls'
WSGI_APPLICATION = 'rgd_example.wsgi.application'


# Swagger
REFETCH_SCHEMA_WITH_AUTH = True
REFETCH_SCHEMA_ON_LOGOUT = True
OPERATIONS_SORTER = 'alpha'
DEEP_LINKING = True