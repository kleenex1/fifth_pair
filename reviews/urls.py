from django.urls import path
from . import views

urlpatterns = [
    # account
    path('accounts/', views.index, name="index" ),
  

    # reviews
    path('reviews/', views.reviews_index, name='reviews-index'),
    path('reviews/create', views.reviews_create, name='reviews-create'),
    path('reviews/<int:pk>/detail', views.reviews_detail, name='reviews-detail'),
    path('reviews/<int:pk>/update', views.reviews_update, name='reviews-update'),
    path('reviews/<int:pk>/delete', views.reviews_delete, name='reviews-delete'),

    # comments

]
