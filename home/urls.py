from django.urls import path
from .views import Homepageview, stone_index, Aboutpageview
from . import views


urlpatterns = [
    path('', Homepageview.as_view(), name='home'),
    path('Products/', views.stone_index, name='stonespage' ),
    path('Products/<int:pk>/', views.stone_detail, name='stone_detail'),
    path('about/', Aboutpageview.as_view(), name= 'about')
]
