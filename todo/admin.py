from django.contrib import admin

# Register your models here.
from django.contrib import admin
from todo.models import ToDoItem, ToDoList

admin.site.register(ToDoItem)
admin.site.register(ToDoList)
