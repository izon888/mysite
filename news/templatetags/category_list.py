from django import template
from ..models import Category

register = template.Library()


@register.inclusion_tag('news/inc/_sidebar.html')
def load_category_list():
    return {'categories': Category.objects.all()}

