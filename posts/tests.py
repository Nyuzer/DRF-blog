from django.test import TestCase
from django.contrib.auth.models import User
from .models import Posts


class BlogTest(TestCase):

    @classmethod
    def setUpTestData(self):
        testuser = User.objects.create_user(username='testuser',
                                            password='testuser')
        testuser.save()

        testpost = Posts.objects.create(title='Blog title', author=testuser, body='Blog body')
        testpost.save()

    def test_Blog_content(self):
        post = Posts.objects.get(pk=1)
        author = f'{post.author}'
        title = f'{post.title}'
        body = f'{post.body}'

        self.assertEqual(author, 'testuser')
        self.assertEqual(title, 'Blog title')
        self.assertEqual(body, 'Blog body')


