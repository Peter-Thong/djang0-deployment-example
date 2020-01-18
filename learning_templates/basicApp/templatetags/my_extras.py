from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value, arg):
    """
    this cut out all the value of "arg" from the string!
    """
    return value.raplace(arg, '')

# register.filter('cut', cut)
