from django.db import models

class About(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    profile_image = models.ImageField(upload_to='profile/')

    def __str__(self):
        return self.title


class Skill(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='skills/')
    level = models.PositiveIntegerField(help_text="Enter value between 0 to 100")

    def __str__(self):
        return self.name



class Project(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='projects/')
    frontend = models.CharField(max_length=200)
    backend = models.CharField(max_length=200)
    description = models.TextField()
    github_link = models.URLField()
    live_link = models.URLField(blank=True)

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Education(models.Model):
    degree = models.CharField(max_length=200)
    institute = models.CharField(max_length=200)
    year = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.degree

    
class Certification(models.Model):
    title = models.CharField(max_length=200)
    issuer = models.CharField(max_length=150)
    year = models.CharField(max_length=50)
    image = models.ImageField(upload_to='certifications/', blank=True, null=True)

    def __str__(self):
        return self.title
