from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomUserChangeForm, ReviewForm, CommentForm
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login, logout, update_session_auth_hash
from .models import User, Comment, Review
from django.contrib.auth.decorators import login_required

def index(request):
    reviews = Review.objects.order_by('-pk')[:6]
    return render(request, 'base/base.html', {"reviews":reviews})

def accounts_signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("accounts-login")
    else:
        form = CustomUserCreationForm()
    context = {
        "form": form,
    }
    return render(request, "accounts/signup.html", context)


def accounts_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("reviews-index")
    else:
        form = AuthenticationForm()
    context = {
        "form": form,
    }
    return render(request, "accounts/login.html", context)


def accounts_detail(request, pk):
    form = User.objects.get(pk=pk)
    context = {
        "form": form,
    }
    return render(request, "accounts/detail.html", context)


@login_required
def accounts_edit(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("accounts-detail", request.user.pk)
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        "form": form,
    }
    return render(request, "accounts/edit.html", context)


def accounts_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect("accounts-detail", request.user.pk)
    else:
        form = PasswordChangeForm(request.user)
    context = {
        "form": form,
    }
    return render(request, "accounts/passwd.html", context)


def accounts_logout(request):
    logout(request)
    return redirect("reviews-index")


def accounts_delete(request):
    request.user.delete()
    logout(request)
    return redirect("reviews-index")


@login_required
def comment_create(request, pk):
    review = Review.objects.get(pk=pk)
    commentform = CommentForm(request.POST)
    if commentform.is_valid():
        comment = commentform.save(commit=False)
        comment.review = review
        comment.user = request.user
        comment.save()
        return redirect("reviews-detail", review.pk)


@login_required
def comment_delete(requet, review_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if requet.user == comment.user:
        comment.delete()
        return redirect("reviews-detail", review_pk)
    else:
        return redirect("reviews-detail", review_pk)


# reviews
def reviews_index(request):
    reviews = Review.objects.all()
    return render(request, "reviews/index.html", {"reviews": reviews})


@login_required
def reviews_create(request):
    if request.method == "POST":
        review_form = ReviewForm(request.POST, request.FILES)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect("reviews-index")
    else:
        review_form = ReviewForm()
    return render(request, "reviews/create.html", {"review_form": review_form})


def reviews_detail(request, pk):
    review = Review.objects.get(pk=pk)
    commentform = CommentForm()
    comments = review.comment_set.all()
    context = {
        "review": review,
        "commentform": commentform,
        "comments": comments,
    }
    return render(request, "reviews/detail.html", context)


@login_required
def reviews_update(request, pk):
    review = Review.objects.get(pk=pk)
    if request.user == review.user:
        if request.method == "POST":
            review_form = ReviewForm(request.POST, request.FILES, instance=review)
            if review_form.is_valid():
                review_form.save()
                return redirect("reviews-detail", review.pk)
        else:
            review_form = ReviewForm(instance=review)
        return render(request, "reviews/forms.html", {"review_form": review_form})
    else:
        return redirect("review-detail", review.pk)


@login_required
def reviews_delete(request, pk):
    review = Review.objects.get(pk=pk)
    review.delete()
    return redirect("reviews-index")
