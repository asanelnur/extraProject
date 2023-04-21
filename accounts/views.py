from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from accounts import serializers, models, filters, constants, services
from django_filters import rest_framework as filter

# Create your views here.


class WalletViewSet(ModelViewSet):
    queryset = models.Wallet.objects.select_related('account') # it's like a join
    serializer_class = serializers.WalletSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = filters.WalletFilter


class AccountViewSet(ModelViewSet):
    account_service = services.AccountServiceV1()
    # queryset = account_service.get_accounts()
    # serializer_class = serializers.CreateAccountSerializer
    filter_backends = (filter.DjangoFilterBackend,)
    filterset_fields = ('first_name', 'last_name')

    def get_serializer_class(self):
        print(f'{self.action=}')
        if self.action in ('list', 'retrieve'):
            return serializers.RetrieveAccountSerializer
        return serializers.CreateAccountSerializer

    def get_queryset(self):
        return self.account_service.get_accounts(action=self.action)

    def perform_create(self, serializer: serializers.CreateAccountSerializer):
        self.account_service.create_account(data=serializer.validated_data)


class AccountViewSetV2(ModelViewSet):
    account_service = services.AccountServiceV1()
    serializer_class = serializers.RetrieveAccountSerializer
    filter_backends = (filter.DjangoFilterBackend,)
    filterset_fields = ('first_name', 'last_name')

    def perform_create(self, serializer: serializers.CreateAccountSerializer):
        self.account_service.create_account(data=serializer.validated_data)

    def get_queryset(self):
        return self.account_service.get_accounts(action=self.action)

#n+1 problem week 10 lecture2
#prefetch_related
#many to many
#one to many


#selected_releted:
#one to one
#many to one

# annotate для каждого аккаунта отдельно
#aggregate общий статистика шыгару керек болган кезде
# Account.objects.aggregate(wallets_total_amount=Sum('wallets__amount', default=Decimal(0)))
