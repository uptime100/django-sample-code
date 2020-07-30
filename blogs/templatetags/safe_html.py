from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag
def safe_html(value):
    return mark_safe(value)
