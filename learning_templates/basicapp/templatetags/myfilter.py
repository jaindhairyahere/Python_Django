from django import template

register = template.Library()

@register.filter(name='cost')
def cost(value,arg):
	return value*arg
