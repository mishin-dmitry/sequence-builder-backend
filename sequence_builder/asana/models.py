from django.db import models


class Asana(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=False, blank=True, upload_to="images/")
