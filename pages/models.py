from django.db import models

# Create your models here.




class twitter_ac(models.Model):
    
    name = models.CharField(max_length=200)
    ot1 = models.IntegerField()
    rp1 = models.IntegerField()
    rt1 = models.IntegerField()
    pt1 = models.IntegerField()
    f1 = models.IntegerField()
    p3 = models.IntegerField()

    def __str__(self):
        return self.name

class cal_tw(models.Model):

    name = models.CharField(max_length=200)
    ga = models.IntegerField()
    ss = models.IntegerField()
    fr = models.IntegerField()

    def __str__(self):
        return self.name

class cal_tweets(models.Model):
    
    name = models.CharField(max_length=200)
    ga = models.IntegerField()
    ss = models.FloatField()
    fr = models.FloatField()

    def __str__(self):
        return self.name

class data_twitter(models.Model):
    
    name = models.CharField(max_length=200)
    ot1 = models.IntegerField()
    rp1 = models.IntegerField()
    rt1 = models.IntegerField()
    pt1 = models.IntegerField()
    f1 = models.IntegerField()
    p3 = models.IntegerField()
    ga = models.IntegerField()
    ss = models.FloatField()
    fr = models.FloatField()

    def __str__(self):
        return self.name
