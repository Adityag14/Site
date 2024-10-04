from django.urls import path
from .views import IndexView, contact_view

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('home/', IndexView.as_view(), {'page': 'home'}, name='home'),
    path('career/', IndexView.as_view(), {'page': 'career'}, name='career'),
    path('contact/', contact_view, name='contact_view'),

]
