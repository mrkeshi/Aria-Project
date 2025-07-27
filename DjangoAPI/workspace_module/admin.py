from django.contrib import admin


# Register your models here.
from .models import *



@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'status', 'created_at', ]
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title','id']
@admin.register(TaskCategories)
class TaskCategoryAdmin(admin.ModelAdmin):
    list_display = ['category',]



@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name','project']
@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ['user','project','skill','level']

