'''import os
import django
from django.core.management import call_command

# Указываем Django, где лежит settings.py
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'oak_build.settings')
django.setup()

# Делаем дамп с контролем кодировки
with open('fixture/goods/categs.json', 'w', encoding='utf-8') as f:
    call_command('dumpdata', 'goods.Categories', indent=2, stdout=f)
'''