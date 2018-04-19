import os
import django
from django.conf import settings


# variável de ambiente para definir quais configurações
# trocar lms.setting pelo nome do pacote do seu app
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LMS')


# 'pytest' chama automaticamente esta função quando
def pytest_configure():
    settings.DEBUG = False
    django.setup()

    