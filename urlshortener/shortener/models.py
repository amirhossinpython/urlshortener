from django.db import models


class Link(models.Model):
    original_url = models.URLField()
    short_code = models.CharField(max_length=10, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    clicks = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return f"{self.original_url} -> {self.short_code}"
    
