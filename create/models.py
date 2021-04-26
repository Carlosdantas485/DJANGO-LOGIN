from django.db import models

class login (models.Model):

    STATUS = (
        ('Doing', 'Doing'),
        ('Done', 'Done'),
    )

    name = models.CharField(max_length=255)
    about = models.TextField(max_length=500, default='')
    
    done = models.CharField(
        max_length=5,
        choices=STATUS,
    )

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    class Meta:
        verbose_name_plural = 'Tasks'


    def __str__(self):
        return self.name