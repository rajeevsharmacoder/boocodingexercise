from django.test import SimpleTestCase
from django.urls import resolve, reverse
from boocodingexercise import views


class TestUrls(SimpleTestCase):

    def test_get_user_profile_url_is_resolved(self):
        url = reverse('boocodingexercise:get_profile_api', args=(1,))
        self.assertEquals(resolve(url).func, views.get_profile_api)

    def test_create_user_profile_url_is_resolved(self):
        url = reverse('boocodingexercise:create_profile_api')
        self.assertEquals(resolve(url).func, views.create_profile_api)

    def test_post_comment_url_is_resolved(self):
        url = reverse('boocodingexercise:create_comment_api')
        self.assertEquals(resolve(url).func, views.create_comment_api)

    def test_get_single_comment_url_is_resolved(self):
        url = reverse('boocodingexercise:get_comment_api', args=(4,))
        self.assertEquals(resolve(url).func, views.get_comment_api)

    def test_get_all_comments_url_is_resolved(self):
        url = reverse('boocodingexercise:get_all_comments_api')
        self.assertEquals(resolve(url).func, views.get_all_comments_api)

    def test_like_comment_url_is_resolved(self):
        url = reverse('boocodingexercise:like_comment', args=(3,))
        self.assertEquals(resolve(url).func, views.like_comment)

    def test_dislike_comment_url_is_resolved(self):
        url = reverse('boocodingexercise:dislike_comment', args=(4,))
        self.assertEquals(resolve(url).func, views.dislike_comment)
