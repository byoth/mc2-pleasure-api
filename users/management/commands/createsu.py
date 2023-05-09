from dotenv import load_dotenv
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
import os

load_dotenv()

class Command(BaseCommand):
    help = 'Creates a superuser.'

    def handle(self, *args, **options):
        admin_username = os.getenv('ADMIN_USERNAME')
        if not User.objects.filter(username=admin_username).exists():
            User.objects.create_superuser(
                username=admin_username,
                password=os.getenv('ADMIN_PASSWORD'),
            )
        print('Superuser has been created.')