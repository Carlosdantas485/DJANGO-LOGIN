from django.db import models

class login (models.Model):

    STATUS = (
        ('Doing', 'Doing'),
        ('Done', 'Done'),
    )

    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, default='')
    phone = models.CharField(max_length=255, default='')
    password01 = models.CharField(max_length=255, default='')
    password02 = models.CharField(max_length=255, default='')
    
    done = models.CharField(
        max_length=5,
        choices=STATUS,
    )

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.name