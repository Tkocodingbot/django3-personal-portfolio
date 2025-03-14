from django.db import models

class project(models.Model):
    tittle=models.CharField(max_length=100)
    description=models.CharField(max_length=250)
    image=models.ImageField(upload_to='portfolio/images')
    url=models.URLField(blank=True)

    def __str__(self):
        return self.tittle