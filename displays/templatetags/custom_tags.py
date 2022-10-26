from django import template
from displays.models import Notification

register = template.Library()

@register.inclusion_tag('notification.html', takes_context=True)
def show_notification(context):
    request_user = context['request'].user
    notifications = Notification.objects.filter(to_user=request_user).exclude(user_has_seen=True)
    return {'notifications': notifications}