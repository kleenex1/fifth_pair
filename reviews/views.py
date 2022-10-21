from django.shortcuts import render, redirect
from .models import Comment, Review
from .forms import CommentForm


def index(request):
    return render(request, "accounts/index.html")


def comment_create(request, pk):
    review = Review.objects.get(pk=pk)
    commentform = CommentForm(request.POST)
    if commentform.is_valid():
        comment = commentform.save(commit=False)
        comment.review = review
        comment.user = request.user
        comment.save()
        pass


def comment_delete(requet, review_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if requet.user == comment.user:
        comment.delet()
        pass
    else:
        pass
