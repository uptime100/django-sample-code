import datetime

import humanize
from django import template

register = template.Library()


@register.simple_tag
def to_date(value):
    try:
        return humanize.naturaltime(datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%fZ"))
    except ValueError:
        return humanize.naturaltime(datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ"))