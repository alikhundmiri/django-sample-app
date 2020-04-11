from django.contrib import admin
from . models import Post


# Register your models here.
class PostAdmin(admin.ModelAdmin):
	list_display = ["person_name", "person_job", "post_slug"]
	list_filter = ["person_name", "person_job", "post_slug"]
	search_fields = ["person_name", "person_job", "post_slug"]

	class Meta:
		model = Post

admin.site.register(Post, PostAdmin)