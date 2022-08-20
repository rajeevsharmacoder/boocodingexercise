# Generated by Django 4.1 on 2022-08-20 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PostComment',
            fields=[
                ('CommentId', models.AutoField(primary_key=True, serialize=False)),
                ('CommentText', models.CharField(max_length=2048)),
                ('Likes', models.BigIntegerField(default=0)),
                ('LikedBy', models.CharField(max_length=102400)),
                ('Dislikes', models.BigIntegerField(default=0)),
                ('DislikedBy', models.CharField(max_length=102400)),
                ('CommentorId', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('ProfileId', models.AutoField(primary_key=True, serialize=False)),
                ('Username', models.CharField(max_length=128)),
                ('FirstName', models.CharField(max_length=128)),
                ('LastName', models.CharField(max_length=128)),
                ('ProfileImage', models.ImageField(blank=True, max_length=1024, null=True, upload_to='images/')),
            ],
        ),
    ]