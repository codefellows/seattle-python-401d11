from django.contrib.auth.models import User
from django.dispatch import receiver
from django.utils import timezone
from django.db import models


class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='categories')
    name = models.CharField(max_length=180, default='Untitled')
    description = models.TextField(blank=True, null=True)

    date_uploaded = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)

    def __repr__(self):
        return '<Category: {}>'.format(self.name)

    def __str__(self):
        return '{}'.format(self.name)


class Card(models.Model):
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cards', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='cards')
    title = models.CharField(max_length=180, default='Untitled')
    description = models.TextField(blank=True, null=True)

    date_uploaded = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)
    date_completed = models.DateField(blank=True, null=True)

    STATES = (
        ('COMPLETE', 'Complete'),
        ('INCOMPLETE', 'Incomplete'),
    )
    status = models.CharField(
        max_length=16,
        choices=STATES,
        default='Incomplete'
    )

    def __repr__(self):
        return '<Card: {} | {}>'.format(self.title, self.status)

    def __str__(self):
        return '{} | {}'.format(self.title, self.status)


@receiver(models.signals.post_save, sender=Card)
def set_card_completed_date(sender, instance, **kwargs):
    """Update the date completed if completed."""
    if instance.date_completed == 'Complete' and not instance.date_completed:
        instance.date_completed = timezone.now()
        instance.save()
