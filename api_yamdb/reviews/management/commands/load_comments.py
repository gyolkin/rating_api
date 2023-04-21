from django.core.management import BaseCommand

from ._loader import data_loader
from reviews.models import Comment


class Command(BaseCommand):
    def handle(self, *args, **options):
        data_loader(Comment, 'comments.csv')
