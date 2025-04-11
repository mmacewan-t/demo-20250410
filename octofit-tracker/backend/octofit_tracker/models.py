from bson import ObjectId
from djongo import models

class ObjectIdField(models.Field):
    def get_prep_value(self, value):
        if not value:
            return ObjectId()
        if not isinstance(value, ObjectId):
            return ObjectId(value)
        return value

class User(models.Model):
    id = ObjectIdField(primary_key=True)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

class Team(models.Model):
    id = ObjectIdField(primary_key=True)
    name = models.CharField(max_length=255)
    members = models.JSONField()

class Activity(models.Model):
    id = ObjectIdField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=255)
    duration = models.IntegerField()

class Leaderboard(models.Model):
    id = ObjectIdField(primary_key=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    score = models.IntegerField()

class Workout(models.Model):
    id = ObjectIdField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()