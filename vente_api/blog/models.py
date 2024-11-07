from django.db import models
class Blog(models.Model):
    titre = models.CharField(max_length=150)
    date = models.DateField(auto_now_add=False)
    description=models.TextField()
    def __str__(self):
        return self.titre
