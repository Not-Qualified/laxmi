from django.contrib import admin
from .models import Person

# Register your models here.

class PersonAdmin(admin.ModelAdmin):
	list_display = ["person", "mobile_one", "city", "country", "date_added", ]

	def person(self, obj):
		return f"{obj.first_name} {obj.last_name}"

	person.short_description = "Name"


admin.site.register(Person, PersonAdmin)