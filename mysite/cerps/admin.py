from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(People)
admin.site.register(Journal)
admin.site.register(Book)
admin.site.register(Patent)
admin.site.register(Grant)
admin.site.register(Award)