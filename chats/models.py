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
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)

    created_at = models.DateTimeField("Created at", auto_now_add=True)
    created_by = models.CharField(max_length = 100,null = True)
    is_active = models.BooleanField(default=True)
    deleted_by = models.CharField(max_length = 100,null = True)
    deleted_at = models.DateTimeField("Delete at", auto_now=False,null = True)

    def __str__(self):
        return self.name
    


class Department(models.Model):
    id = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    name = models.CharField(max_length = 100,null = False)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    bot = models.ForeignKey(Bot, on_delete=models.CASCADE)

    created_at = models.DateTimeField("Created at", auto_now_add=True)
    created_by = models.CharField(max_length = 100,null = True)
    is_active = models.BooleanField(default=True)
    deleted_by = models.CharField(max_length = 100,null = True)
    deleted_at = models.DateTimeField("Delete at", auto_now=False,null = True)

    def __str__(self):
        return self.name


class Agent(models.Model):
    id = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    name = models.CharField(max_length = 100,null = False)
    email = models.EmailField(max_length = 254,null = False)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    created_at = models.DateTimeField("Created at", auto_now_add=True)
    created_by = models.CharField(max_length = 100,null = True)
    is_active = models.BooleanField(default=True)
    deleted_by = models.CharField(max_length = 100,null = True)
    deleted_at = models.DateTimeField("Delete at", auto_now=False,null = True)

    def __str__(self):
        return self.name


class Channel(models.Model):
    id = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    name = models.CharField(max_length = 100,null = False)
    bot = models.ForeignKey(Bot, on_delete=models.CASCADE)
    credential =models.JSONField("json", null=False, default=dict)

    created_at = models.DateTimeField("Created at", auto_now_add=True)
    created_by = models.CharField(max_length = 100,null = True)
    is_active = models.BooleanField(default=True)
    deleted_by = models.CharField(max_length = 100,null = True)
    deleted_at = models.DateTimeField("Delete at", auto_now=False,null = True)

    def __str__(self):
        return self.name

Options=(
    ('open', 'open'),
    ('close', 'open')
)


class Conversations(models.Model):
    id = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    name = models.CharField(max_length = 100,null = False)
    Channel = models.CharField(max_length = 100,null = False)
    sender_id = models.PositiveIntegerField(null=True, blank=True)
    sender_name = models.CharField(max_length = 100,null = True)
    agent = models.CharField(max_length = 100)
    bot = models.ForeignKey(Bot, on_delete=models.CASCADE)
    status = models.CharField(max_length=10,choices = Options,default = 'open')

    created_at = models.DateTimeField("Created at", auto_now_add=True)
    created_by = models.CharField(max_length = 100,null = True)
    is_active = models.BooleanField(default=True)
    deleted_at = models.DateTimeField("Delete at", auto_now=False,null = True)
    deleted_by = models.CharField(max_length = 100,null = True)

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
    conversation = models.ForeignKey(Conversations, on_delete=models.CASCADE)
    autortype = models.CharField(max_length=10,choices = Roles,default = 'user')
    autor = models.CharField(max_length = 100,null = False)
    attachment = models.CharField(max_length = 200,null = False)

    created_at = models.DateTimeField("Created at", auto_now_add=True)
    created_by = models.CharField(max_length = 100,null = True)
    is_active = models.BooleanField(default=True)
    deleted_at = models.DateTimeField("Delete at", auto_now=False,null = True)
    deleted_by = models.CharField(max_length = 100,null = True)

    def __str__(self):
        return str(self.id)


class UserProfile(models.Model):
    id = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    sender_id = models.PositiveIntegerField(null=True, blank=True)
    Channel = models.CharField(max_length = 100,null = False)
    name = models.CharField(max_length = 100,null = False)
    optin = models.BooleanField(default=True)
    bot = models.ForeignKey(Bot, on_delete=models.CASCADE)
    phonenumber = models.CharField(max_length=10,null=False)

    created_at = models.DateTimeField("Created at", auto_now_add=True)
    created_by = models.CharField(max_length = 100,null = True)
    is_active = models.BooleanField(default=True)
    deleted_at = models.DateTimeField("Delete at", auto_now=False,null = True)
    deleted_by = models.CharField(max_length = 100,null = True)
    

    def __str__(self):
        return str(self.id)
