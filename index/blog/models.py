from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})
    