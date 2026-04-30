from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.TextField(blank=False)
    description = models.TextField()
    priority = models.CharField(max_length=25)
    duedate = models.DateField()  # e.g. 2023-06-30
    is_complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    