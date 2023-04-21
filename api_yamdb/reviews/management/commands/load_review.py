from django.core.management import BaseCommand

from ._loader import data_loader
from reviews.models import Review


class Command(BaseCommand):
    def handle(self, *args, **options):
        data_loader(Review, 'review.csv')
