from django.contrib import admin
from .models import CSTEST,CTEST,CPPTEST,JAVATEST,PYTHONTEST,result
# Register your models here.

admin.site.register(CSTEST)
admin.site.register(CTEST)
admin.site.register(CPPTEST)
admin.site.register(JAVATEST)
admin.site.register(PYTHONTEST)
admin.site.register(result)

