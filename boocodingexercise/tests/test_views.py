from json import JSONDecoder, JSONEncoder
from urllib import response
from django.test import TestCase, Client
from django.urls import reverse
from boocodingexercise import models


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.create_profile_api_url = reverse(
            'boocodingexercise:create_profile_api')
        self.get_profile_api_url = reverse(
            'boocodingexercise:get_profile_api', args=(2,))
        self.create_comment_api_url = reverse(
            'boocodingexercise:create_comment_api')
        self.get_comment_api_url = reverse(
            'boocodingexercise:get_comment_api', args=(3,))
        self.get_all_comments_api_url = reverse(
            'boocodingexercise:get_all_comments_api')
        self.like_comment_url = reverse(
            'boocodingexercise:like_comment', args=(3,))
        self.dislike_comment_url = reverse(
            'boocodingexercise:dislike_comment', args=(3,))

    # def test_create_profile_api_POST(self):
    #     data = {
    #         "Username": "testusername",
    #         "FirstName": "Test",
    #         "LastName": "User",
    #         "ProfileImage": "/Users/rajeevsharma/Dev/django_mongodb_check/django_mongodb_check_project/media/me1.jpeg"
    #     }
    #     response = self.client.post(self.create_profile_api_url, data)
    #     self.assertEquals(response.status_code, 200)

    def test_get_profile_api_GET(self):
        response = self.client.get(self.get_profile_api_url)
        self.assertEquals(response.status_code, 200)

    # def test_create_comment_api_POST(self):
    #     data = {
    #         "CommentText": "Test Comment Text",
    #         "CommentorId": 3
    #     }
    #     response = self.client.post(self.create_comment_api_url, data)
    #     self.assertEquals(response.status_code, 200)

    def test_get_comment_api_GET(self):
        response = self.client.get(self.get_comment_api_url)
        self.assertEquals(response.status_code, 200)

    def test_get_all_comments_api_GET(self):
        response = self.client.get(self.get_all_comments_api_url)
        self.assertEquals(response.status_code, 200)

    # def test_like_comment_PUT(self):
    #     response = self.client.put(self.like_comment_url)
    #     self.assertEquals(response.status_code, 200)

    # def test_dislike_comment_PUT(self):
    #     response = self.client.put(self.dislike_comment_url)
    #     self.assertEquals(response.status_code, 200)
