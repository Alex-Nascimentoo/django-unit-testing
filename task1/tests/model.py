from django.test import TestCase
from task1.models import Post
from django.contrib.auth.models import User

class TestTask1Models(TestCase):

  def setUp(self):
    self.user = User.objects.create_user(
      username = 'testuser',
      password = 'pass',
    )

    self.user2 = User.objects.create_user(
      username = 'testuser2',
      password = 'pass2',
    )

    self.post = Post.objects.create(
      title = 'Test Post',
      content = 'Test Content',
    )

    self.post.likes.set([self.user.pk, self.user2.pk])


  def test_post_str(self):
    self.assertEqual(str(self.post), 'Test Post')


  def test_post_like_users(self):
    self.assertEqual(self.post.likes.count(), 2)
