from django.contrib import admin
from .models import Staff, Product


# CR: The admin could be more functional...
# Read more on how to customize the admin:
# https://docs.djangoproject.com/en/3.0/ref/contrib/admin/

# Register your models here.
admin.site.register(Staff)
admin.site.register(Product)

# CR: Report is missing in the admin
