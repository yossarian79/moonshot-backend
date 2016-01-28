from django.contrib import admin
from .models import Question
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id','author','title','description')
admin.site.register(Question,QuestionAdmin)

# Register your models here.
