from xml.etree.ElementTree import Comment
from django.test import TestCase, Client
from boocodingexercise import models


class TestModels(TestCase):

    def setUp(self):
        self.myprofile = models.UserProfile(
            Username="rajeevsharma", FirstName="Rajeev", LastName="Sharma", ProfileImage="media/me1.jpg")
        self.mycomment = models.PostComment(
            CommentText="My Comment", CommentorId=0)

    def test_user_profile_creation(self):
        self.newprofile = models.UserProfile(
            Username="newuser", FirstName="New", LastName="User", ProfileImage="media/me2.jpg")
        self.assertNotEquals(self.myprofile.Username, self.newprofile.Username)

    def test_post_comment(self):
        self.newcomment = models.PostComment(
            CommentText="New Comment", CommentorId=self.myprofile.ProfileId)
        self.assertNotEquals(self.mycomment.CommentText,
                             self.newcomment.CommentText)
