from django.core.management import BaseCommand, call_command


class Command(BaseCommand):
    def handle(self, *args, **options):
        print('Загружаем данные для всех моделей...')
        call_command('load_users')
        call_command('load_genre')
        call_command('load_category')
        call_command('load_titles')
        call_command('load_review')
        call_command('load_comments')
