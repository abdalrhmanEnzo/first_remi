# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('comment_id', models.AutoField(primary_key=True, serialize=False, auto_created=True)),
                ('comment_desc', models.TextField(max_length=200)),
                ('comment_date', models.DateTimeField(auto_now_add=True)),
                ('comment_type', models.CharField(default='r', max_length=1, choices=[('r', 'Reminder'), ('l', 'ReminderList')])),
            ],
        ),
        migrations.CreateModel(
            name='LookUpTag',
            fields=[
                ('tag_id', models.AutoField(primary_key=True, serialize=False, auto_created=True)),
                ('tag_desc', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('notification_id', models.AutoField(primary_key=True, serialize=False, auto_created=True)),
                ('notification_date', models.DateTimeField(auto_now_add=True)),
                ('notification_type', models.CharField(max_length=1, choices=[('s', 'share'), ('c', 'comment'), ('r', 'remind')])),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False, auto_created=True)),
                ('post_desc', models.TextField(max_length=400)),
                ('share_date', models.DateTimeField(auto_now_add=True)),
                ('privacy_type', models.CharField(default='p', max_length=1, choices=[('p', 'public'), ('o', 'onlyMe'), ('f', 'friends'), ('c', 'custom')])),
            ],
        ),
        migrations.CreateModel(
            name='Reminder',
            fields=[
                ('reminder_id', models.AutoField(primary_key=True, serialize=False, auto_created=True)),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('reminder_title', models.CharField(max_length=100)),
                ('reminder_time', models.DateTimeField()),
                ('reminder_desc', models.TextField(max_length=400)),
                ('reminder_pic', models.FilePathField(default='/default/reminder_pic.jpg')),
                ('joined_count', models.IntegerField(default=1)),
                ('share_count', models.IntegerField(default=0)),
                ('comments_count', models.IntegerField(default=0)),
                ('repeat', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ReminderList',
            fields=[
                ('list_id', models.AutoField(primary_key=True, serialize=False, auto_created=True)),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('list_desc', models.TextField(max_length=400)),
                ('list_pic', models.FilePathField(default='/default/list_pic.jpg')),
                ('joined_count', models.IntegerField(default=1)),
                ('share_count', models.IntegerField(default=0)),
                ('comments_count', models.IntegerField(default=0)),
                ('list_privacy', models.CharField(default='p', max_length=1, choices=[('p', 'public'), ('o', 'onlyMe'), ('f', 'friends'), ('c', 'custom')])),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True)),
                ('lkp_tag', models.ForeignKey(to='remi_app.LookUpTag')),
                ('post', models.ForeignKey(to='remi_app.Post')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False, auto_created=True)),
                ('user_name', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('full_name', models.CharField(default='anonymous', max_length=200)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('sex', models.CharField(default='m', max_length=1, choices=[('f', 'Female'), ('m', 'Male'), ('o', 'Other')])),
                ('status', models.CharField(default='a', max_length=1, choices=[('a', 'active'), ('i', 'inactive'), ('s', 'suspended')])),
                ('profile_pic', models.FilePathField(default='/default/profile_pic.jpg')),
                ('friends_no', models.IntegerField()),
                ('date_joined', models.DateField(auto_now_add=True)),
                ('verified', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='UserRelation',
            fields=[
                ('relation_id', models.AutoField(primary_key=True, serialize=False, auto_created=True)),
                ('relation_type', models.CharField(default='p', max_length=1, choices=[('p', 'pending'), ('a', 'add'), ('f', 'follow'), ('b', 'block')])),
                ('request_date', models.DateTimeField(auto_now_add=True)),
                ('accept_date', models.DateTimeField()),
                ('block_date', models.DateTimeField()),
                ('follow_date', models.DateTimeField()),
                ('user_from', models.ForeignKey(to='remi_app.User', related_name='user_from')),
                ('user_to', models.ForeignKey(to='remi_app.User', related_name='user_to')),
            ],
        ),
        migrations.AddField(
            model_name='reminderlist',
            name='user',
            field=models.ForeignKey(to='remi_app.User'),
        ),
        migrations.AddField(
            model_name='reminder',
            name='user',
            field=models.ForeignKey(to='remi_app.User'),
        ),
        migrations.AddField(
            model_name='post',
            name='reminder',
            field=models.ForeignKey(to='remi_app.Reminder'),
        ),
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.ManyToManyField(to='remi_app.User'),
        ),
        migrations.AddField(
            model_name='notification',
            name='post',
            field=models.ForeignKey(to='remi_app.Post'),
        ),
        migrations.AddField(
            model_name='notification',
            name='user',
            field=models.ForeignKey(to='remi_app.User'),
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(to='remi_app.Post'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(to='remi_app.User'),
        ),
    ]
