from django.db import models
from django.utils import timezone
from django.dispatch import receiver
from django.contrib.auth.models import User


class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')
    title = models.CharField(max_length=48)
    detail = models.CharField(max_length=4096)

    STATES = [
        ('incomplete', 'Incomplete'),
        ('complete', 'Complete'),
    ]
    status = models.CharField(choices=STATES, default='incomplete', max_length=48)
    date_created = models.DateTimeField(default=timezone.now)
    date_modified = models.DateTimeField(auto_now=True)
    date_completed = models.DateTimeField(blank=True, auto_now=True)

    def __repr__(self):
        return f'<Note: { self.title } | Status: { self.status }>'

    def __str__(self):
        return f'{ self.title } | Status: { self.status }'

# stretch: research model signals 
@receiver(models.signals.post_save, sender=Note)
def set_note_completed_date(sender, instance, **kwargs):
    """Update the date completed if completed."""
    if instance.status == 'complete' and not instance.date_completed:
        instance.date_completed = timezone.now
        instance.save()
