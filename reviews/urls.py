from django.urls import path
from . import views

urlpatterns = [
    # account
    path("accounts/", views.index, name="index"),
    # reviews
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
