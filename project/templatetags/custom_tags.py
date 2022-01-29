from django import template
import string
register = template.Library()

@register.simple_tag
def splitFunc(value):
    return value.split(":")

@register.simple_tag
def getValueFromIndex(data,index):
    return data[index]
