from django.contrib import admin

from home1.models import library

# Register your models here.
#admin.site.register(Book)
#admin.site.register(Author)
#admin.site.register(Genre)

# @admin.register(Book)
# class bookadmin(admin.ModelAdmin):
#     search_fields=('id','name')
#     list_filter=('name','purchase_date')

# @admin.register(Author)
# class authoradmin(admin.ModelAdmin):
#     search_fields=('author_name',' timestamp ')
#     list_filter=('date_of_birth','date_of_death')

# @admin.register(Genre)
# class genreadmin(admin.ModelAdmin):
#     search_fields=('id','name')
#     list_filter=('name','name')

@admin.register(library)
class libraryadmin(admin.ModelAdmin):
    list_filter=('Branch','IssueDate')