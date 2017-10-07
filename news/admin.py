from django.contrib import admin
from django.utils.text import slugify

from .models import News

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
	date_hierarchy = 'date'
	exclude = ('slug', 'date',)

	def save_model(self, request, obj, form, change):
		obj.slug = slugify(obj.title)
		return super(NewsAdmin, self).save_model(request, obj, form, change)
