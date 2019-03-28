from django.utils import timezone
from django import template


register = template.Library()


@register.filter
def get_date_string(value):
    now_aware = timezone.now()
    delta = value - now_aware

    if delta.days == 0:
        return "Today!"
    elif delta.days < 1:
        return "%s %s ago!" % (abs(delta.days), ("day" if abs(delta.days) == 1 else "days"))
    elif delta.days == 1:
        return "Tomorrow"
    elif delta.days > 1:
        return "In %s days" % delta.days
