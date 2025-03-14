from django.db import models

class Blog(models.Model):
    tittle = models.CharField(max_length=200)
    date = models.DateField(blank=True, null=True)
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.tittle



