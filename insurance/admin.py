from django.contrib import admin
from insurance.models import Branch, Underwriter, Customer

admin.site.register(Branch)
admin.site.register(Underwriter)
admin.site.register(Customer)
