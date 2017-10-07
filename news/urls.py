from django.conf.urls import url
from .views import NewsListView, NewsDetailView

urlpatterns = [
	#url(r'^/?$', NewsListView().as_view(), name='list'),
	url(r'^(?P<slug>[\w_-]{3,255})/?$', NewsDetailView().as_view(), name='detail'),
]