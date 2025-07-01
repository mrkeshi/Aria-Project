from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.core.exceptions import ValidationError
from core.models import *


# Create your models here.

# class Workspace(models.Model):
#     title = models.CharField(max_length=255)
#     user = models.ManyToManyField(settings.AUTH_USER_MODULE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     finished_at = models.DateTimeField(null=True, blank=True)
#     def __str__(self):
#         return self.title

class Project(models.Model):
    """a project can be created """
    # TODO so this need creator that we assning it as manger
    # FIXED many2many realationship

    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.BooleanField(default=False)
    project_manager = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # workspace = models.ForeignKey(Workspace, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    finished_at = models.DateTimeField(null=True, blank=True)
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='users')

    def __str__(self):
        return self.title


class Task(models.Model):
    """task is small part of project who manger  or for example a higher
     level than normal worker like senior.
      give this small peaces to someone to do .
     task have title description and project that belong to a deadline for end
     when they created and when they updated all of task can belong to
     specific category
     and have rate and review after task finished that can be filled
     """
    # TODO  still need some changes and should add field bound with user to do a task

    IMPORTANCE = [
        ("1", "کم اهمیت"),
        ("2", "متوسط"),
        ("3", "مهم"),
    ]

    assigned = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="task_creator", on_delete=models.CASCADE,
                                 null=True, blank=True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='tasks_assigned', on_delete=models.CASCADE,
                                null=True)
    title = models.CharField(max_length=255)
    attached = models.FileField(upload_to='tasks/attached', null=True, blank=True)
    description = models.TextField()
    rate = models.SmallIntegerField(null=True, validators=[MinValueValidator(0), MaxValueValidator(100)], blank=True)
    progress = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='tasks')
    # workspace = models.ForeignKey(Workspace, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    finished_at = models.DateTimeField(null=True, blank=True)
    category = models.ForeignKey('TaskCategories', related_name='task', on_delete=models.SET_NULL, null=True,
                                 blank=True)
    review = models.TextField(null=True, blank=True)
    done = models.BooleanField(default=False)
    importance = models.CharField(max_length=1, choices=IMPORTANCE)
    assigned_attached = models.FileField(upload_to='task/assigned_attached', null=True, blank=True)
    owner_note = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['-created_at'])
        ]

    def save(self, *args, **kwargs):
        if self.progress == 100:
            self.done = True
        else:
            self.done = False
        super(Task, self).save(*args, **kwargs)


class TaskCategories(models.Model):
    """this is a model that categories tasks for specific person  like manager
     who can categories task for what he desire

    category is string field for different task from other

     """
    # something is in my mind that what if we make relationships between
    # categorie and project that
    # TODO need to add user to it
    project_name = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, related_name='task_category')
    category = models.CharField(max_length=32)

    def __str__(self):
        return self.category


class Skill(models.Model):
    name = models.CharField(max_length=255)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.name


class Role(models.Model):
    class Level(models.IntegerChoices):
        JUNIOR = "3", "کارمند عادی"
        SENIOR = "2", "کارمند ارشد"
        PM = "1", "مدیر پروژه"

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.SET_NULL, null=True, blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    level = models.PositiveSmallIntegerField(default=1, choices=Level.choices)

    # def __str__(self):
    # return self.user.email + " " + self.project.title

# برای