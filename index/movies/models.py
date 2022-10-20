from django.db import models
from django.utils import timezone

class Video(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=5000)
    date_posted = models.DateTimeField(default=timezone.now)
    video_id = models.CharField(max_length=50)
    tags = models.CharField(max_length=400)
    clips = models.FileField(upload_to='clips')

    def __str__(self):
        return f'/{self.title}/'

    # def get_absolute_url(self):
    #     return reverse("model_detail", kwargs={"pk": self.pk})
    