from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Posts
from .forms import PostForm
from django.http import Http404
import random


def post_search_view(request):
    print(request)
    query_dict = request.GET
    print(query_dict)
    query_data = query_dict.get("query")
    object_from_db = None
    try:
        if int(query_data):
            object_from_db = Posts.objects.get(id=query_data)
    except Posts.DoesNotExist:
        raise Http404
    except:
        object_from_db = "Вам нужно передовать только числа !"
    context = {
        "object": object_from_db
    }
    return render(request, 'posts/post_search.html', context=context)


def post_list_view(request):
    print(request.GET)
    my_object = Posts.objects.all()
    len_object = len(my_object)
    my_random_object_from_db = Posts.objects.get(id=random.randint(1, len_object))
    all_posts = Posts.objects.all()
    context = {"my_first_object": my_random_object_from_db,
               "posts": all_posts}
    return render(request, 'posts/test.html', context=context)


def post_detail_view(request, id=None):
    post_object = None
    if id is not None:
        try:
            post_object = Posts.objects.get(id=id)
        except:
            raise Http404

    context = {
        "post_object": post_object
    }
    return render(request, 'posts/post_detail.html', context=context)


@login_required
def post_create_view(request):
    form = PostForm(request.POST or None)
    context = {"form": form}
    if form.is_valid():  # is clean
        title = form.cleaned_data.get("title")
        description = form.cleaned_data.get("description")
        post_object = Posts.objects.create(title=title, description=description)
        context["post_object"] = post_object
        context["created"] = True
    return render(request, 'posts/post_create.html', context=context)


"""
def post_create_view(request):
    message = False
    context = {}
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        if title and description:
            Posts.objects.create(title=title, description=description)
            return HttpResponseRedirect("/posts/create/")
        else:
            message = "You sanded empty form !"
    context = {"message": message}
    return render(request, 'posts/post_create.html', context=context)
"""
