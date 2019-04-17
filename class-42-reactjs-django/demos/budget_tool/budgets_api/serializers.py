from rest_framework import serializers
from django.contrib.auth.models import User
from budgets_app.models import Budget, Transaction
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'password',
            'first_name',
            'last_name'
        )

    def create(self, validated_data):
        user = super().create({
            'username': validated_data['username']
        })
        user.set_password(validated_data['password'])
        user.save()
        return user


class BudgetSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField(
        view_name='user_api',
        read_only=True
    )

    class Meta:
        model = Budget
        fields = (
            'id',
            'name',
            'user',
            'total_budget'
        )


class TransactionSerializer(serializers.ModelSerializer):
    budget = serializers.HyperlinkedRelatedField(
        view_name='budget_detail_api',
        read_only=True
    )

    class Meta:
        model = Transaction
        fields = (
            'id',
            'description',
            'budget',
            'type',
            'amount'
        )
