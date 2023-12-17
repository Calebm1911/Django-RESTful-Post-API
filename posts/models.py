from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=240)
    topic = models.CharField(max_length=240)
    content = models.CharField(max_length=2000)
    postDate = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name