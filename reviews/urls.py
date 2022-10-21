from django.urls import path
from . import views

urlpatterns = [
    # account
    path("signup/", views.accounts_signup, name="accounts-signup"),
    path("accounts/login/", views.accounts_login, name="accounts-login"),
    path("detail/<int:pk>/", views.accounts_detail, name="accounts-detail"),
    path("edit/", views.accounts_edit, name="accounts-edit"),
    path("password/", views.accounts_password, name="accounts-password"),
    path("logout/", views.accounts_logout, name="accounts-logout"),
    path("delete/", views.accounts_delete, name="accounts-delete"),
    # reviews
    path("reviews/", views.reviews_index, name="reviews-index"),
    path("reviews/create", views.reviews_create, name="reviews-create"),
    path("reviews/<int:pk>/detail", views.reviews_detail, name="reviews-detail"),
    path("reviews/<int:pk>/update", views.reviews_update, name="reviews-update"),
    path("reviews/<int:pk>/delete", views.reviews_delete, name="reviews-delete"),
    # comments
    path(
        "reviews/<int:pk>/comment_create/", views.comment_create, name="comment-create"
    ),
    path(
        "reviews/<int:review_pk>/comment/<int:comment_pk>/comment_delete",
        views.comment_delete,
        name="comment-delete",
    ),
]
