from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    publish_date = models.DateField(auto_now=False, auto_now_add=False)
    description = models.TextField(default="")
    mail = models.EmailField()
    categories = models.ManyToManyField('Category') 
    image = models.URLField()

    def __str__(self):
        return self.title

class Category(models.Model):
    title = models.CharField(max_length=50)
    text_color = models.CharField(max_length = 100)
    background_color = models.CharField(max_length = 100)
    def __str__(self):
        return self.title
