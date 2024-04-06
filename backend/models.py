from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BlogPost(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='blog_images/')
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title
      
class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author.username} on {self.blog_post.title}"
      
class UserDetails(models.Model):
  user=models.OneToOneField(User, on_delete=models.CASCADE)
  image=models.ImageField(upload_to='userimage')
  full_name=models.CharField(max_length=200, null=True,blank=True)
  bio = models.CharField(max_length=200, null=True, blank=True)
  phone =models.CharField(max_length=15, null=True,blank=True)
  updated=models.DateTimeField(auto_now=True)
  created=models.DateTimeField(auto_now=True)
  
  def __str__(self):
      return self.user.username
  
      

