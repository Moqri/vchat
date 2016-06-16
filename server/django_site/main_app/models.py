from django.db import models


class User(models.Model):
    peer_id = models.CharField(max_length=200)
    status = models.CharField(max_length=200)