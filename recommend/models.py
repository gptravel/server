from django.db import models

class Recommend(models.Model):
    month = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    where = models.CharField(max_length=100)
    budget = models.CharField(max_length=100)
    keyword = models.CharField(max_length=100)
    purpose = models.CharField(max_length=100)
    accompany = models.CharField(max_length=100)
    answer = models.TextField(blank=True, default='')