from django.core.management import BaseCommand

from ._loader import data_loader
from reviews.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        data_loader(User, 'users.csv')
