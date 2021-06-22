from django import template

register = template.Library()

@register.filter(name='short')
def short(value):
    """Gives First 10 characters of string"""
    return (value[:10]+'...')