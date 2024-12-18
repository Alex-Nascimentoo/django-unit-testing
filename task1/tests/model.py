from django.test import TestCase
from task1.models import Post
from django.contrib.auth.models import User

class TestTask1Models(TestCase):

  @classmethod
  def setUpTestData(cls):
    user = User.objects.create_user(
      username = 'testuser',
      password = 'pass',
    )

    user2 = User.objects.create_user(
      username = 'testuser2',
      password = 'pass2',
    )

    cls.post = Post.objects.create(
      title = 'Test Post',
      content = 'Test Content',
      slug = 'slug',
    )

    cls.post.likes.set([user.pk, user2.pk])


  def test_post_str(self):
    self.assertEqual(str(self.post), 'Test Post')


  def test_post_like_users(self):
    self.assertEqual(self.post.likes.count(), 2)

  
  def test_post_get_absolute_url(self):
    self.post.slug = Post.objects.get(id=1)
    self.assertEqual(self.post.slug.get_absolute_url(), '/slug/')
