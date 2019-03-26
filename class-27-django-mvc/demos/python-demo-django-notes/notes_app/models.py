from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=48)
    detail = models.CharField(max_length=4096)

    STATES = [
        ('incomplete', 'Incomplete'),
        ('complete', 'Complete'),
    ]
    status = models.CharField(choices=STATES, default='incomplete', max_length=48)

    def __repr__(self):
        return f'<Note: { self.title } | Status: { self.status }>'

    def __str__(self):
        return f'{ self.title } | Status: { self.status }'
