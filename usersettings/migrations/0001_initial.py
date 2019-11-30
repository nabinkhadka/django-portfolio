# Generated by Django 2.2.7 on 2019-11-30 10:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialURL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('linkedin', 'LinkedIn'), ('medium', 'Medium'), ('pintrest', 'Pintrest'), ('twitter', 'Twitter'), ('github', 'Github'), ('facebook', 'Facebook')], default='other', max_length=25, verbose_name='URL Type')),
                ('link', models.URLField(blank=True, default=None, max_length=1024, null=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Social Url',
                'verbose_name_plural': 'Social Url',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, db_index=True, verbose_name='modified')),
                ('bio', models.CharField(max_length=1024, verbose_name='User bio')),
                ('imageurl', models.URLField(blank=True, default=None, max_length=1024, null=True, verbose_name='Profile picture')),
                ('image', models.ImageField(default=None, null=True, upload_to='profile/%Y/%m/%d', verbose_name='profile image')),
                ('urls', models.ManyToManyField(blank=True, related_name='user_urls', to='usersettings.SocialURL', verbose_name='User Urls')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'User Profile',
                'verbose_name_plural': 'User Profiles',
            },
        ),
        migrations.CreateModel(
            name='SiteSetting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, db_index=True, verbose_name='modified')),
                ('maxblog', models.IntegerField(verbose_name='Max Blog on home')),
                ('sitetitle', models.CharField(max_length=150, unique=True, verbose_name='Site title')),
                ('disqusname', models.CharField(blank=True, default=None, max_length=150, null=True, verbose_name='Disqus short name')),
                ('googleanalyticid', models.CharField(blank=True, default=None, max_length=150, null=True, verbose_name='Google analytics ID')),
                ('keywords', models.CharField(blank=True, default=None, max_length=512, null=True, verbose_name='Site SEO keywords')),
                ('sitevarification', models.CharField(blank=True, default=None, max_length=150, null=True, verbose_name='Google Site Verification')),
                ('description', models.CharField(blank=True, default=None, max_length=150, null=True, verbose_name='Site Description')),
                ('twitterid', models.CharField(blank=True, default=None, max_length=150, null=True, verbose_name='Twitter Handle')),
                ('fbappid', models.CharField(blank=True, default=None, max_length=150, null=True, verbose_name='Twitter Handle')),
                ('fblink', models.URLField(blank=True, default=None, max_length=1024, null=True, verbose_name='Facebook Page link')),
                ('locale', models.CharField(blank=True, default=None, max_length=150, null=True, verbose_name='Site Locale')),
                ('icon', models.ImageField(blank=True, default=None, null=True, upload_to='icon/%Y/%m/%d', verbose_name='Site Favicon')),
                ('iconurl', models.URLField(blank=True, default=None, max_length=1024, null=True, verbose_name='Favicon url')),
                ('site_name', models.CharField(blank=True, default=None, max_length=150, null=True, verbose_name='FB site name')),
                ('defprofile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to='usersettings.UserProfile', verbose_name='Default Profile')),
            ],
            options={
                'verbose_name': 'Site settings',
                'verbose_name_plural': 'Site settings',
            },
        ),
    ]
