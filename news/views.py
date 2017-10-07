from django.views.generic import ListView, DetailView

from .models import News

class NewsListView(ListView):
	template_name = 'news_list.html'
	model = News

class NewsDetailView(DetailView):
	template_name = 'news_detail.html'
	model = News