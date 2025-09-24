from django.db import models

# Create your models here.

class Post (models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)



    #to get the latest the data or to filter by dates in ascending
    class Meta:
        ordering = ['-created_at']


    def __str__(self):
        return self.title


class Comment(models.Model):
    #sets a pk  fk relation to the post model
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Comment by {self.author} on {self.post.title}"

