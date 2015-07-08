__author__ = 'Adly'

from remi_app.models import Comment, LookUpTag, Notification, Post, Reminder, ReminderList, Tag, User, UserRelation
from rest_framework import serializers



class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('user_name','full_name','email','friends_no')