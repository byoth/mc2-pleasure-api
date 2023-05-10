from decimal import Decimal
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils import timezone
import random
from musics.models import Music
from pins.models import Pin

class Command(BaseCommand):
    help = 'Creates dummy pins.'

    def add_arguments(self, parser):
        parser.add_argument('pins_count', type=int)

    def handle(self, *args, **options):
        pins_count = options['pins_count']
        musics = Music.objects.all()
        if not musics:
            Music.objects.create(
                applemusic_id='sample',
                title='Title',
                artist_name='Artist',
                created_at=timezone.now(),
            )
        users = User.objects.all()
        for _ in range(pins_count):
            music = random.choice(musics)
            user = random.choice(users)
            pin = Pin.objects.create(
                music=music,
                user=user,
                latitude=Decimal(random.uniform(-90, 90)),
                longitude=Decimal(random.uniform(-180, 180)),
                locality='Somewhere',
                sub_locality='어딘가',
                weather=random.choice(['sunny', 'cloudy', 'rainy', 'snowy']),
                temperature=random.randint(-20, 40),
                created_at=timezone.now(),
            )
            print(f"Created dummy Pin: {pin}")