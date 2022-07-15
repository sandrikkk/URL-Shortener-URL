from url_shortener_api.views import PremiumShortenerUrlApiView
from url_shortener_api.views import ShortenerUrlApiView, RetrieveUrlApiView, Redirector
from django.urls import path

urlpatterns = [
    path('short-url/', ShortenerUrlApiView.as_view()),
    path('short-url/<int:pk>/', RetrieveUrlApiView.as_view()),
    path('short-url/premium/', PremiumShortenerUrlApiView.as_view()),
    path('<str:shortener_link>/',Redirector.as_view())
]
