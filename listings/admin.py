from django.contrib import admin
from .models import Listing

class ListingAdmin(admin.ModelAdmin):
  list_display = ('id', 'title', 'is_active', 'price', 'list_date', 'user')
  list_display_links = ('id', 'title')
  list_filter = ('user',)
  list_editable = ('is_active',)
  search_fields = ('title', 'description', 'address', 'city', 'price')
  list_per_page = 25

admin.site.register(Listing, ListingAdmin)