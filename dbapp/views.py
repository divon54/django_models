from django.shortcuts import render, get_object_or_404

from .models import Blogpost


# Create your views here.
def blog_list(request):
    posts = Blogpost.objects.all()
    return render(request, template_name='blog_list.html', context={'posts': posts})


def blog_detail(request, id):
    post = get_object_or_404(Blogpost, id=id)
    return render(request, template_name='blog_details.html', context={'post': post})
