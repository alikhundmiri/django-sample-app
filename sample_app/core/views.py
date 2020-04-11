from django.shortcuts import render
from django.conf import settings

from .models import Post
# Create your views here.

# LANDING PAGE
# this page will list all the entries
def index(request):
	posts = Post.objects.all()
	context = {
		'production' : settings.DEBUG,
		'posts' : posts,
	}

	return render(request, 'landing_page.html', context)


# This will allow the entry of new posts
def new_post(request):

	context = {
		'production' : settings.DEBUG,
	}

	return render(request, 'new_post.html', context)


# this page will allow view of individial post
def post_detail(request):

	context = {
		'production' : settings.DEBUG,
	}

	return render(request, 'post_detail.html', context)
