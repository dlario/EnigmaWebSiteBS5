from django.contrib import admin

# Register your models here.
from .models import ContactInformation, Person, CompanyPerson, Company

class CompanyPersonInline(admin.TabularInline):
    model = CompanyPerson

class ContactInline(admin.TabularInline):
    model = ContactInformation

class PersonInline(admin.TabularInline):
    model = Person

class CompanyPersonAdmin(admin.ModelAdmin):
    inlines = [CompanyPersonInline]


class ContactAdmin(admin.ModelAdmin):
    inlines = [ContactInline]

class PersonAdmin(admin.ModelAdmin):
    inlines = [PersonInline]

admin.site.register(Company, CompanyPersonAdmin)

admin.site.register(Person, ContactAdmin)
