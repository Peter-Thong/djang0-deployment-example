from django import template

register = template.library()

@register.filter(name='cut')
def cut(value, arg):
    """
    this cut out all the value of "arg" from the string!
    """
    return value.raplace(arg, '')

# register.filter('cut', cut)
