from django.db import models
from django.conf import settings
from django.db import models
# Create your models here.


class PostBlog(models.Model):
    content_title = models.CharField(max_length=250)
    image = models.FileField(upload_to='blog/', default='blog/images/')
    date = models.DateField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    content = models.TextField(max_length=1000)

    def __str__(self):
        return self.content_title