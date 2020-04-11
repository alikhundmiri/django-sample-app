from django.contrib import admin
from . models import Post, Detail


# Register your models here.
class PostAdmin(admin.ModelAdmin):
	list_display = ["person_name", "person_job", "post_slug"]
	list_filter = ["person_name", "person_job", "post_slug"]
	search_fields = ["person_name", "person_job", "post_slug"]

	class Meta:
		model = Post

admin.site.register(Post, PostAdmin)


class DetailsAdmin(admin.ModelAdmin):
	list_display = ["user", "parent_post","details"]
	list_filter = ["user", "parent_post","details"]
	search_fields = ["user", "parent_post","details"]

	class Meta:
		model = Detail

admin.site.register(Detail, DetailsAdmin)