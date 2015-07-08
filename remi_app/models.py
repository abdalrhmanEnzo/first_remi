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

    def __unicode__(self):
        return self.full_name


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

    def __unicode__(self):
        return '( ' + self.user_from.user_name + ' --> ' + self.user_to.user_name + ' )'


class Reminder(models.Model):
    reminder_id = models.IntegerField(primary_key=True, auto_created=True)
    # list --> foreign key for list_reminder table.
    user = models.ForeignKey(User)
    time_created = models.DateTimeField(auto_now_add=True)
    reminder_title = models.CharField(max_length=100)
    reminder_time = models.DateTimeField()
    reminder_desc = models.TextField(max_length=400)
    reminder_pic = models.FilePathField(default='/default/reminder_pic.jpg')
    joined_count = models.IntegerField(default=1)
    share_count = models.IntegerField(default=0)
    comments_count = models.IntegerField(default=0)
    repeat = models.BooleanField(default=False)  # repeated reminder or no.

    def __unicode__(self):
        return self.reminder_title + ' --> ' + self.reminder_time.strftime('%Y-%m-%d %H:%M')


class Post(models.Model):
    PRIVACY = (
        ('p', 'public'),
        ('o', 'onlyMe'),
        ('f', 'friends'),
        ('c', 'custom'),
        )

    post_id = models.IntegerField(primary_key=True, auto_created=True)
    post_desc = models.TextField(max_length=400)
    reminder = models.ForeignKey(Reminder)
    user = models.ManyToManyField(User)  # creator, still thinking of it.
    share_date = models.DateTimeField(auto_now_add=True)
    privacy_type = models.CharField(max_length=1, choices=PRIVACY, default='p')

    def __unicode__(self):
        return self.post_desc


class Comment(models.Model):
    COMMENT_TYPE = (
        ('r', 'Reminder'),
        ('l', 'ReminderList'),
    )

    comment_id = models.IntegerField(primary_key=True, auto_created=True)
    post = models.ForeignKey(Post)
    user = models.ForeignKey(User)
    comment_desc = models.TextField(max_length=200)
    comment_date = models.DateTimeField(auto_now_add=True)
    comment_type = models.CharField(max_length=1, choices=COMMENT_TYPE, default='r')

    def __unicode__(self):
        return self.comment_desc


class LookUpTag(models.Model):
    tag_id = models.IntegerField(primary_key=True, auto_created=True)
    tag_desc = models.CharField(max_length=100)


class Tag(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    lkp_tag = models.ForeignKey(LookUpTag)
    post = models.ForeignKey(Post)

    def __unicode__(self):
        return self.lkp_tag.tag_desc


class ReminderList(models.Model):
    PRIVACY = (
        ('p', 'public'),
        ('o', 'onlyMe'),
        ('f', 'friends'),
        ('c', 'custom'),
        )

    list_id = models.IntegerField(primary_key=True, auto_created=True)
    user = models.ForeignKey(User)
    time_created = models.DateTimeField(auto_now_add=True)
    list_desc = models.TextField(max_length=400)
    list_pic = models.FilePathField(default='/default/list_pic.jpg')
    joined_count = models.IntegerField(default=1)
    share_count = models.IntegerField(default=0)
    comments_count = models.IntegerField(default=0)
    # list_type = models.CharField(max_length=1, choices= LIST_TYPES, default='')
    list_privacy = models.CharField(max_length=1, choices=PRIVACY, default='p')


class Notification(models.Model):
    NOTIFY_TYPE = (
        ('s', 'share'),
        ('c', 'comment'),
        ('r', 'remind'),
        )

    notification_id = models.IntegerField(primary_key=True, auto_created=True)
    post = models.ForeignKey(Post)
    user = models.ForeignKey(User)
    notification_date = models.DateTimeField(auto_now_add=True)
    notification_type = models.CharField(max_length=1, choices=NOTIFY_TYPE)
    # notification_desc = models.TextField(max_length=200)

    def __unicode__(self):
        operation = ''

        if self.notification_type == 'c':
            operation = 'commented on '
        elif self.notification_type == 's':
            operation = 'shared'
        else:
            operation = 'liked'

        return self.user.user_name + ' ' + operation + ' your post'
