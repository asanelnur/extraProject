from rest_framework import  serializers
from accounts import models


class _AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Account
        fields = ('first_name', 'last_name')


class WalletSerializer(serializers.ModelSerializer):
    # account = serializers.PrimaryKeyRelatedField(read_only=True)
    account = _AccountSerializer(read_only=True)

    class Meta:
        model = models.Wallet
        fields = '__all__'


class _AccountWalletSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Wallet
        fields = (
            'amount',
            'amount_currency',
        )


class CreateAccountSerializer(serializers.ModelSerializer):
    # wallets = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
    wallets = _AccountWalletSerializer(write_only=True, many=True)
    # total_amount = serializers.DecimalField(read_only=True, decimal_places=2, max_digits=12)
    # avg_amount = serializers.DecimalField(read_only=True, decimal_places=2, max_digits=12)
    # custom_amount = serializers.DecimalField(read_only=True, decimal_places=2, max_digits=12)

    class Meta:
        model = models.Account
        fields = '__all__'


class RetrieveAccountSerializer(serializers.ModelSerializer):
    wallets = _AccountWalletSerializer(read_only=True, many=True)

    class Meta:
        model = models.Account
        fields = '__all__'
