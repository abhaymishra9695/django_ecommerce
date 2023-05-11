from django import template

register = template.Library()

@register.filter
def get_products(category):
    return category.product_set.all()

