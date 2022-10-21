from django.urls import path
from . import views

urlpatterns = [
    # account
    path('signup/', views.accounts_signup, name="accounts-signup" ),
    path('login/', views.accounts_login, name="accounts-login"),
    path('detail/<int:pk>/', views.accounts_detail, name="accounts-detail"),
    path('edit/', views.accounts_edit, name="accounts-edit"),
    path('password/', views.accounts_password, name="accounts-password"),
    path('test/', views.test, name="test"),
    path('logout/', views.accounts_logout, name="accounts-logout"),
    path('delete/', views.accounts_delete, name="accounts-delete"),
    # reviews
  
    
    # comments

]
