from django import template

register = template.Library()

# use decorator
@register.filter(name='cut')
def cut(value, arg):
    """
    This cuts out all values of "arg" from the string!
    """
    return value.replace(arg, '')

# first of is template string, second one is function
# register.filter('cut', cut)
