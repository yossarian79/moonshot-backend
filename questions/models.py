from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
# Create your models here.



    
class Question(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.TextField(max_length=200)
    description = models.TextField(max_length=1024)

    def __str__(self):
        return '%s %s' % (self.title, self.description)
        
    def get_absolute_url(self):
       return reverse('question_detail', args=[str(self.id)])    


