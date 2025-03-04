# Generated by Django 3.2.4 on 2021-06-30 13:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0002_alter_posts_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postcomments',
            name='post_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='details', to='posts.posts'),
        ),
        migrations.AlterField(
            model_name='postcomments',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='details', to=settings.AUTH_USER_MODEL),
        ),
    ]
