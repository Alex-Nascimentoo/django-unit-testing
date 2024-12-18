from django.test import TestCase
from task1.models import Post
from django.contrib.auth.models import User

class TestTask1Models(TestCase):

  def test_post_str(self):
    post = Post(title='Test Post', content='Test Content')
    self.assertEqual(str(post), 'Test Post')

  def test_post_like_users(self):
    user = User.objects.create_user(
      username = 'testuser',
      password = 'pass',
    )

    user2 = User.objects.create_user(
      username = 'testuser2',
      password = 'pass2',
    )

    post = Post.objects.create(
      title = 'Test Post',
      content = 'Test Content',
    )

    post.likes.set([user.pk, user2.pk])
    
    self.assertEqual(post.likes.count(), 2)
