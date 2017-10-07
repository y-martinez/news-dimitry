from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.core.urlresolvers import reverse

@python_2_unicode_compatible
class News(models.Model):
	slug = models.SlugField(unique=True, max_length=255)
	title = models.CharField(max_length=255)
	date = models.DateField(auto_now_add=True)
	content = models.TextField()

	class Meta:
		verbose_name_plural = 'news'

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('news:detail', kwargs = {'slug': self.slug})