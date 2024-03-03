from django.db import models

# Create your models here.

class User(models.Model):
    class Role(models.TextChoices):
        admin = "admin", "ADMIN"
        user = "user", "USER"

    name = models.CharField(max_length=63, unique=True)
    email = models.EmailField()
    role = models.CharField(max_length=63, choices=Role.choices, default=Role.user)

    def __str__(self):
        return self.name


class Task(models.Model):
    class Status(models.TextChoices):
        done = "done", "DONE"
        process = "processing", "PROCESSING"
        put_off = "put_off", "PUT OFF"
        
    name = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=64,choices=Status.choices,default=Status.process)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='tasks',null=True)
