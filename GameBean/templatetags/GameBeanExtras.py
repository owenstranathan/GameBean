from django import template

register = template.Library()

@register.filter
def class_name(value):
    return value.__class__.__name__

@register.filter
def get_range( value ):
    return range( value )

@register.filter
def mod( argument, value):
    return argument%value

@register.filter
def filter_by_id(queryset, id):
    return queryset.filter(id=id)

@register.filter
def count(queryset):
    return queryset.count()
