from django import template

register = template.Library()

@register.filter
def duration_format(value):
    hours = value // 60
    minutes = value % 60
    if hours > 0:
        return f"{hours}h {minutes:02d}m"
    else:
        return f"{minutes}m"