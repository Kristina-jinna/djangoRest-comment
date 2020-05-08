from django.db import models
import datetime

# Create your models here.

class UserAuthor(models.Model):
    idvk = models.IntegerField()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    bd = models.DateField(datetime.date)

    def __str__(self):
        return self.first_name



class Group(models.Model):
    id_vk_group = models.IntegerField()
    name_group = models.CharField(max_length=200)
    id_User = models.ForeignKey('UserAuthor', on_delete=models.CASCADE)

    def __str__(self):
        return self.name_group

class Post(models.Model):
    id_vk_post = models.IntegerField()
    name_post = models.CharField(max_length=1000)
    body_post = models.TextField()
    id_User = models.ForeignKey('UserAuthor', on_delete=models.CASCADE)

    def __str__(self):
        return self.name_post



