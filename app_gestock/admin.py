from django.contrib import admin

# Register your models here.
from .models import t_article, t_categories, t_cupboard, t_products, t_room, t_types

admin.site.register(t_article)
admin.site.register(t_categories)
admin.site.register(t_cupboard)
admin.site.register(t_products)
admin.site.register(t_room)
admin.site.register(t_types)