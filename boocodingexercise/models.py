from django.db import models

# Create your models here.


class UserProfile(models.Model):
    ProfileId = models.AutoField(primary_key=True)
    Username = models.CharField(max_length=128)
    FirstName = models.CharField(max_length=128)
    LastName = models.CharField(max_length=128)
    ProfileImage = models.ImageField(
        null=True, blank=True, upload_to="images/", max_length=1024)


class PostComment(models.Model):
    CommentId = models.AutoField(primary_key=True)
    CommentText = models.CharField(max_length=2048)
    Likes = models.BigIntegerField(default=0)
    LikedBy = models.CharField(max_length=102400, default="")
    Dislikes = models.BigIntegerField(default=0)
    DislikedBy = models.CharField(max_length=102400, default="")
    CommentorId = models.BigIntegerField(null=False, blank=False)
