from typing import Protocol, OrderedDict

from decimal import Decimal

from django.db import transaction
from django.db.models import QuerySet, Sum, Q, Avg, Case, When, Value, DecimalField, F

from accounts import models, constants


class AccountReposInterface(Protocol):

    @staticmethod
    def get_accounts() -> QuerySet[models.Account]: ...

    @staticmethod
    def create_account(data: OrderedDict) -> None: ...


class AccountReposV1:

    @staticmethod
    def get_accounts() -> QuerySet[models.Account]:
        return models.Account.objects.prefetch_related('wallets',).annotate(
            total_amount=Sum(
                'wallets__amount',
                filter=Q(wallets__amount_currency__in=(
                    constants.AmountCurrencyChoices.KZT,
                    constants.AmountCurrencyChoices.USD
                )),
                default=Decimal(0.0)
                             ),
            avg_amount=Avg('wallets__amount',
                           default=Decimal(0.0)),
            custom_amount=Sum(
                Case(
                    When(
                        Q(wallets__amount_currency=constants.AmountCurrencyChoices.RUB),
                        then=F('wallets__amount')*2),
                    When(
                        Q(wallets__amount_currency=constants.AmountCurrencyChoices.USD),
                        then=F('wallets__amount')*3),
                    default=Value(Decimal(0.0)),
                    output_field=DecimalField()
                )
            )
        )

    @staticmethod
    # @transaction.atomic()
    def create_account(data: OrderedDict) -> None:
        with transaction.atomic():
            wallets = data.pop('wallets')
            account = models.Account.objects.create(**data)
            # raise AttributeError
            models.Wallet.objects.bulk_create([
                models.Wallet(**w, account=account) for w in wallets
            ])


# str(Account.objects.only('id','first_name').query)
# str(Account.objects.defer('id','first_name').query)