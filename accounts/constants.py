from django.db import models


class AmountCurrencyChoices(models.TextChoices):
    RUB = 'RUB'
    KZT = 'KZT'
    USD = 'USD'
