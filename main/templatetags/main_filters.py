from django import template
register = template.Library()

@register.filter
def add_urlpath(url):
    return f'https://www.youtube.com/watch?v={url}'