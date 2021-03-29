from django.db import models
from django.utils import timezone


class Item(models.Model):

    name = models.CharField(max_length=50, null=True)
    description = models.TextField(max_length=300, null=True, blank=True)
    pub_date = models.DateTimeField("published date", default=timezone.now(), null=True, blank=True)

    def __str__(self):
        return f"{self.name}  ----   {self.description} ----  {self.pub_date}"
