from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
  list_display = ('id', 'last_name', 'email', 'phone', 'creation_date')
  list_display_links = ('id', 'last_name')
  search_fields = ('last_name',)
  list_per_page = 25

admin.site.register(User, UserAdmin)