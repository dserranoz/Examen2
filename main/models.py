from django.db import models


class Zombie(models.Model):
    name = models.CharField(max_length=20)
    cementery = models.CharField(max_length=20)

    def __unicode__(self):
        return '%s' % self.name


class Tweet(models.Model):
    status = models.CharField(max_length=140)
    zombie = models.ForeignKey('Zombie', related_name='tweetss')
    created_at = models.DateTimeField(auto_now_add=True)
