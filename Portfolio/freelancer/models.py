# blog/models.py
from django.db import models
from django.utils import timezone

class Blog(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateTimeField(default=timezone.now)
    description = models.TextField()
    likes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    def total_comments(self):
        return self.comments.count()  # Custom method to count comments

class BlogImage(models.Model):
    blog = models.ForeignKey(Blog, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blog_images/%Y/%m/%d/')
    alt_text = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Image for {self.blog.title}"

class Comment(models.Model):
    blog = models.ForeignKey(Blog, related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=100, default='Anonymous')
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Comment by {self.author} on {self.blog.title}"
    



# projects

class Project(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateTimeField(default=timezone.now)  # Date completed
    description = models.TextField()
    likes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    def total_comments(self):
        return self.comments.count()  # Custom method to count comments

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='project_images/%Y/%m/%d/')
    alt_text = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Image for {self.project.title}"

class ProjectComment(models.Model):
    project = models.ForeignKey(Project, related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=100, default='Anonymous')
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    is_demo_request = models.BooleanField(default=False)  # Flag for demo requests
    demo_type = models.CharField(
        max_length=50,
        choices=[('standard', 'Standard'), ('elite', 'Elite')],
        null=True,
        blank=True
    )  # Type of demo requested

    def __str__(self):
        return f"Comment by {self.author} on {self.project.title}"

    def save(self, *args, **kwargs):
        # Automatically set demo request fields based on text content
        if '@demo' in self.text.lower():
            self.is_demo_request = True
            self.demo_type = 'standard'
        elif '@elite' in self.text.lower():
            self.is_demo_request = True
            self.demo_type = 'elite'
        super().save(*args, **kwargs)