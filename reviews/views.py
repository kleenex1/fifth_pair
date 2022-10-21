from django.shortcuts import render, redirect
from .models import Comment, Review
from .forms import ReviewForm, CommentForm

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


# reviews
def reviews_index(request):
    reviews = Review.objects.all()
    return render(request, 'reviews/index.html', {"reviews": reviews})


def reviews_create(request):
    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('reviews-index')
    else:
        review_form = ReviewForm()
    return render(request, 'reviews/create.html', {'review_form':review_form})

def reviews_detail(request, pk):
    review = Review.objects.get(pk=pk)
    return render(request, 'reviews/detail.html', {"review": review})

def reviews_update(request, pk):
    review = Review.objects.get(pk=pk)
    if request.user == review.user:
        if request.method == 'POST':
            review_form = ReviewForm(request.POST, request.FILES, instance=review)
            if review_form.is_valid():
                review_form.save()
                return redirect('review-detail', review.pk)
        else:
            review_form = ReviewForm(instance=review)
        return render(request, 'reviews/form.html', {"review_form": review_form})
    else:
        return redirect('review-detail', review.pk)        


def reviews_delete(request,pk):
    review = Review.objects.get(pk=pk)
    review.delete()
    return redirect('reviews-index')

