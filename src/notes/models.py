from django.db import models

# Create your models here.

LABEL_CHOICES = (
    ('P', 'primary'),
    ('SE','secondary'),
    ('S','success'),
    ('D','danger'),
    ('W',' warning'),
    ('I','info'),
    ('L','light'),
    ('DA','dark'),
)

class Note(models.Model):
    title = models.CharField(max_length=100)
    due_date = models.DateTimeField()
    label = models.CharField(max_length=5,choices=LABEL_CHOICES)
    links = models.URLField(max_length = 300)

    def __str__(self):
        return self.title
    

