from django.shortcuts import render, get_object_or_404
from django.conf import settings

from .models import Post
# Create your views here.

# LANDING PAGE
# this page will list all the entries
# DONE
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

	return render(request, 'core/new_post.html', context)


# this page will allow view of individial post
def post_detail(request, slug=None):
	post = get_object_or_404(Post, post_slug=slug)
	context = {
		'production' : settings.DEBUG,
		'post' : post,
	}

	return render(request, 'core/post_detail.html', context)
