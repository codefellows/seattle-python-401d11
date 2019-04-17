from django.db import models
from django.contrib.auth.models import User


class Budget(models.Model):
    name = models.CharField(max_length=128)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='budgets'
    )
    total_budget = models.FloatField()

    def __repr__(self):
        return '<Budget: ' + self.name + '>'

    def __str__(self):
        return self.user.username + ': ' + self.name


class Transaction(models.Model):
    description = models.CharField(max_length=2048)
    budget = models.ForeignKey(
        Budget,
        on_delete=models.CASCADE,
        related_name='transactions'
    )
    TYPE_CHOICES = [
        ('withdrawal', 'withdrawal'),
        ('deposit', 'deposit')
    ]
    type = models.CharField(
        choices=TYPE_CHOICES,
        max_length=16
    )
    amount = models.FloatField()

    def __repr__(self):
        return '<Transaction: ' + self.name + '>'

    def __str__(self):
        return self.budget.name + ' ' + self.type + ': ' + self.description
