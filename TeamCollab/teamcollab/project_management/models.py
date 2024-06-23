from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class User(AbstractUser):
    email = models.EmailField(unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    
    groups = models.ManyToManyField(
        Group,
        related_name='project_management_app_user_set',  # Unique related_name for groups
        blank=True,
        help_text=('The groups this user belongs to. A user will get all permissions '
                   'granted to each of their groups.'),
        related_query_name='user',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='project_management_app_user_permissions_set',  # Unique related_name for user_permissions
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='user',
    )

class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class ProjectMember(models.Model):
    ROLE_CHOICES = (
        ('Admin', 'Admin'),
        ('Member', 'Member'),
    )
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

class Task(models.Model):
    STATUS_CHOICES = (
        ('To Do', 'To Do'),
        ('In Progress', 'In Progress'),
        ('Done', 'Done'),
    )
    PRIORITY_CHOICES = (
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    )
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=15, choices=STATUS_CHOICES)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES)
    assigned_to = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()

class Comment(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
