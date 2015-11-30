from django.contrib import admin
from insurance.models import Branch, Underwriter, Customer, Product, TextMessage

admin.site.register(Branch)
admin.site.register(Underwriter)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(TextMessage)
