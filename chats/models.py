import email
from email.policy import default
from operator import mod
from unittest.util import _MAX_LENGTH
from xml.parsers.expat import model
from django.db import models

import uuid

# Create your models here.sss


class Organization(models.Model)   :
    id = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    name = models.CharField(max_length = 100,null = False)
    created_at = models.DateTimeField("Created at", auto_now_add=True,null = False)
    created_by = models.CharField(max_length = 100,null = True)
    is_active = models.BooleanField(default=True)
    deleted_at = models.DateTimeField("Delete at", auto_now=False,null = True)
    deleted_by = models.CharField(max_length = 100,null = True)

    def __str__(self):
        return self.name



class Bot(models.Model):
    id = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    name = models.CharField(max_length = 100,null = False)
    created_at = models.DateTimeField("Created at", auto_now_add=True)
    created_by = models.CharField(max_length = 100,null = True)
    is_active = models.BooleanField(default=True)
    deleted_by = models.CharField(max_length = 100,null = True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.name
    


class Department(models.Model):
    id = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    name = models.CharField(max_length = 100,null = False)
    created_at = models.DateTimeField("Created at", auto_now_add=True)
    created_by = models.CharField(max_length = 100,null = True)
    is_active = models.BooleanField(default=True)
    deleted_by = models.CharField(max_length = 100,null = True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    bot = models.ForeignKey(Bot, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Agent(models.Model):
    id = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    name = models.CharField(max_length = 100,null = False)
    email = models.EmailField(max_length = 254,null = False)
    created_at = models.DateTimeField("Created at", auto_now_add=True)
    created_by = models.CharField(max_length = 100,null = True)
    is_active = models.BooleanField(default=True)
    deleted_by = models.CharField(max_length = 100,null = True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Channel(models.Model):
    id = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    name = models.CharField(max_length = 100,null = False)
    created_at = models.DateTimeField("Created at", auto_now_add=True)
    created_by = models.CharField(max_length = 100,null = True)
    is_active = models.BooleanField(default=True)
    deleted_by = models.CharField(max_length = 100,null = True)
    credential =models.JSONField("json", null=False, default=dict)
    bot = models.ForeignKey(Bot, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Conversations(models.Model):
    id = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    name = models.CharField(max_length = 100,null = False)
    Channel = models.CharField(max_length = 100,null = False)
    sender_id = models.PositiveIntegerField(null=True, blank=True)
    sender_name = models.CharField(max_length = 100,null = True)
    created_at = models.DateTimeField("Created at", auto_now_add=True)
    created_by = models.CharField(max_length = 100,null = True)
    is_active = models.BooleanField(default=True)
    deleted_by = models.CharField(max_length = 100,null = True)
    bot = models.ForeignKey(Bot, on_delete=models.CASCADE)
    agent = models.CharField(max_length = 100,null = False)
    status = models.CharField(max_length = 100,null = False)

    def __str__(self):
        return self.name



Roles=(
    ('user', 'user'),
    ('agent', 'agent')

)

class Message(models.Model):
    id = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    sender_id = models.PositiveIntegerField(null=True, blank=True)
    Channel = models.CharField(max_length = 100,null = False)
    created_at = models.DateTimeField("Created at", auto_now_add=True)
    created_by = models.CharField(max_length = 100,null = True)
    is_active = models.BooleanField(default=True)
    deleted_by = models.CharField(max_length = 100,null = True)
    conversation = models.ForeignKey(Conversations, on_delete=models.CASCADE)
    autor = models.CharField(max_length = 100,null = False)
    autortype = models.CharField(max_length=10,choices = Roles,default = 'user')

    def __str__(self):
        return str(self.id)


class UserProfile(models.Model):
    id = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    sender_id = models.PositiveIntegerField(null=True, blank=True)
    Channel = models.CharField(max_length = 100,null = False)
    name = models.CharField(max_length = 100,null = False)
    created_at = models.DateTimeField("Created at", auto_now_add=True)
    created_by = models.CharField(max_length = 100,null = True)
    is_active = models.BooleanField(default=True)
    deleted_by = models.CharField(max_length = 100,null = True)
    option = models.BooleanField(default=True)
    phonenumber = models.CharField(max_length=10,null=False)
    bot = models.ForeignKey(Bot, on_delete=models.CASCADE)
    

    def __str__(self):
        return str(self.id)
