import os
from csv import DictReader

from django.conf import settings


def data_loader(model, filename):
    if model.objects.exists():
        print(f'Данные для {model.__name__} уже загружены.')
    else:
        try:
            for row in DictReader(
                open(
                    os.path.join(settings.LOAD_DATA_DIR, filename),
                    encoding='utf8'
                )
            ):
                model_instance = model(**row)
                model_instance.save()
            print(f'Данные для {model.__name__} успешно загружены.')
        except FileNotFoundError:
            print(f'FileNotFoundError: Файл {filename} не найден.')


def add_genres(title_model, genre_model, filename):
    if title_model.objects.get(pk=1).genre.all().exists():
        print(f'Жанры для {title_model.__name__} уже добавлены.')
    else:
        try:
            for row in DictReader(
                open(
                    os.path.join(settings.LOAD_DATA_DIR, filename),
                    encoding='utf8'
                )
            ):
                title = title_model.objects.get(id=row['title_id'])
                genre = genre_model.objects.get(id=row['genre_id'])
                title.genre.add(genre)
            print(f'Жанры для {title_model.__name__} успешно загружены.')
        except FileNotFoundError:
            print(f'FileNotFoundError: Файл {filename} не найден.')
