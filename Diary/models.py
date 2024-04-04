from django.db import models
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField

# Create your models here.
class Diary(models.Model):
    owner = models.ForeignKey(get_user_model(), related_name="diaries", on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body = RichTextField()
    datecreated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Diaries'
        ordering = ('-datecreated',)

