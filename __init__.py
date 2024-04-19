import django

author = 'ayhan'
version = "1.0.6"

if django.VERSION < (3, 2):
    default_app_config = "JazzminTM.apps.JazzminTMConfig"


