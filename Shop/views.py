import django.http
from django.http import Http404
from django.shortcuts import render
from .forms import CommentForm
from django.shortcuts import redirect
from .models import DoorModel, Comment
from django.contrib.auth.decorators import login_required


def main(request):
    models = DoorModel.objects.all()
    comments = Comment.objects.all()
    context = {"models": models, 'comments': comments}
    return render(request, 'main.html', context)


def modelview(request, model_id):
    model = DoorModel.objects.get(id=model_id)
    context = {'model': model}
    return render(request, 'model.html', context)


@login_required
def add_comment(request):
    if request.method != 'POST':
        form = CommentForm()
    else:
        form = CommentForm(data=request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.author = request.user
            new_comment.save()
        return redirect('shop:main')
    context = {'form': form}
    return render(request, 'add_comment.html', context)


@login_required
def edit_comment(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    if request.user != comment.author:
        raise Http404
    if request.method != 'POST':
        form = CommentForm(instance=comment)
    else:
        form = CommentForm(instance=comment, data=request.POST)
        if form.is_valid():
            form.save()
        return redirect('shop:main')
    context = {'form': form, 'comment': comment}
    return render(request, 'edit_comment.html', context)






