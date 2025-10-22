from django.urls import path
from . import views

app_name = 'homepage'
 
urlpatterns = [
    path('', views.IndexCreateView.as_view(), name='index'),
    path('profile/<slug:username>/', views.ProfileListView.as_view(), name='profile'),
    path('order/<int:pk>/edit/', views.OrderUpdateView.as_view(), name='order_edit'),
    path('order/<int:pk>/delete/', views.OrderDeleteView.as_view(), name='order_delete'),
]