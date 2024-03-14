from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(verbose_name='title', max_length=50)
    author = models.CharField(verbose_name='author', max_length=50)
    about = models.CharField(verbose_name='about',max_length=90)
    full_text = models.TextField(verbose_name='text')
    date = models.DateTimeField(verbose_name='date of posting')

    def __str__(self):
        return self.title