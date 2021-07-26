from django.contrib import admin
from courses.models import Course, Type, BaseForArticle, Homework


admin.site.register(Course)
admin.site.register(Type)
admin.site.register(BaseForArticle)
admin.site.register(Homework)
