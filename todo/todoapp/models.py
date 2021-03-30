from django.db import models


class Item(models.Model):

    name = models.CharField(max_length=50, null=True)
    description = models.TextField(max_length=300, null=True, blank=True)
    completed = models.BooleanField(default=False)
    pub_date = models.DateTimeField("published date", auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f"{self.name}  ----   {self.description} ----  {self.pub_date}"
