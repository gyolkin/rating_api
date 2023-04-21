from django.core.management import BaseCommand

from ._loader import data_loader
from reviews.models import Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        data_loader(Category, 'category.csv')
