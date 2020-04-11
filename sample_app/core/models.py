from django.db import models

from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.urls import reverse
from django.utils.text import slugify

class Post(models.Model):
	person_name				=			models.CharField(max_length=50)
	person_job 				=			models.CharField(max_length=30)

	post_slug				=			models.SlugField(max_length=80, unique=True)

	timestamp				=			models.DateTimeField(auto_now=False, auto_now_add=True)
	updated					=			models.DateTimeField(auto_now=True, auto_now_add=False)

	def __str__(self):
		return(str(self.post_slug))



################   P R E    S A V E    S T U F F     F O R     S L U G     C R E A T I O N

# This lower section, will create unique slugs when ever a new entry is requested
def create_slug(instance, new_slug=None):

	if new_slug is None:
		# slug = slugify(instance.blog_title)
		slug = slugify('{person_name} the {person_job}'.format(person_name, person_job))
	else:
		slug = new_slug

	qs = Post.objects.filter(post_slug=slug).order_by("-id")
	
	if qs.exists():
		# the code below, up until return, has been copied from my other project, text2image's code model
		# I remember solving the repetitive problem over there.
		if "_" in slug:
			a = slug.split('_')
			a_list = a[:-1] #remove the last element from this list.
			a = "-".join(a_list)
		else:
			a = slug
		return create_slug(instance, new_slug=new_slug)
	return slug

def create_title(instance, new_title=None):
	# TODO: 
	# Create a script which cuts the string from the first period, and takes the first
	# half as the title, and the rest as the blog post.
	new_title = "This is a sample"

	return new_title

def pre_save_location_receiver(sender, instance, *args, **kwargs):
	# if not instance.blog_title:
	# 	instance.blog_title = create_title(instance)
	if not instance.post_slug:
		instance.post_slug = create_slug(instance)

pre_save.connect(pre_save_location_receiver, sender=Post)
