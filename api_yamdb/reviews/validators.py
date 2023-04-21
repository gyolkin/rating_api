import datetime as dt

from django.core.exceptions import ValidationError


def year_validator(value):
    if value > dt.datetime.now().year:
        raise ValidationError(
            f'{value} год не подходит! Он еще не наступил.',
            params={'value': value}
        )
