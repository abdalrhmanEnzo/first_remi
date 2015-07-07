from django.db import models

class User(models.Model):
    SEX = (
        ('f', 'Female'),
        ('m', 'Male'),
        ('o', 'Other'),
    )

    STATUS = (
        ('a', 'active'),
        ('i', 'inactive'),
        ('s', 'suspended'),
    )

    user_id = models.IntegerField(primary_key=True, auto_created=True)
    user_name = models.CharField(primary_key=True, max_length=100)
    password = models.CharField(max_length=100)
    full_name = models.CharField(max_length=200, default='anonymous')
    email = models.EmailField(max_length=100)
    sex = models.CharField(max_length=1, choices=SEX, default='m')
    status = models.CharField(max_length=1, choices=STATUS, default='a')
    profile_pic = models.FilePathField(default='/default/profile_pic.jpg')
    friends_no = models.IntegerField()
    date_joined = models.DateField(auto_now_add=True)
    verified = models.BooleanField(default=False)

class UserRelation(models.Model):
    RELATION = (
        ('p', 'pending'),
        ('a', 'add'),
        ('f', 'follow'),
        ('b', 'block'),
        )

    relation_id = models.IntegerField(primary_key=True, auto_created=True)
    user_from = models.ForeignKey(User, related_name='user_from')
    user_to = models.ForeignKey(User, related_name='user_to')
    relation_type = models.CharField(max_length=1, choices=RELATION, default='p')
    request_date = models.DateTimeField(auto_now_add=True)
    accept_date = models.DateTimeField()
    block_date = models.DateTimeField()
    follow_date = models.DateTimeField()

class LookUpReminder(models.Model):
    type_id = models.IntegerField(primary_key=True, auto_created=True)
    type_desc = models.CharField(max_length=50, default='General')

class Reminder(models.Model):
    reminder_id = models.IntegerField(primary_key=True, auto_created=True)
    # list --> foreign key for list_reminder table.
    user = models.ForeignKey(User)
    time_created = models.DateTimeField(auto_now_add=True)
    reminder_title = models.CharField(max_length=100)
    reminder_desc = models.TextField(max_length=400)
    reminder_pic = models.FilePathField(default='/default/reminder_pic.jpg')
    joined_count = models.IntegerField(default=0)
    repost_count = models.IntegerField(default=0)
    comments_count = models.IntegerField(default=0)
