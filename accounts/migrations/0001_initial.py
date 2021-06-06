# Generated by Django 3.2 on 2021-06-06 09:21

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
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_user', models.BooleanField(default=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='지갑주소')),
            ],
        ),
        migrations.CreateModel(
            name='SNS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('github', models.URLField(blank=True, verbose_name='깃허브')),
                ('blog', models.URLField(blank=True, verbose_name='블로그')),
                ('facebook', models.URLField(blank=True, verbose_name='페이스북')),
                ('insta', models.URLField(blank=True, verbose_name='인스타')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.person')),
            ],
            options={
                'verbose_name_plural': 'SNS',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('korName', models.CharField(max_length=30, verbose_name='한글이름')),
                ('engName', models.CharField(max_length=30, verbose_name='영문이름')),
                ('email', models.EmailField(max_length=50, verbose_name='이메일')),
                ('phone', models.CharField(max_length=13, verbose_name='전화번호')),
                ('github', models.URLField(blank=True, verbose_name='깃허브')),
                ('blog', models.URLField(blank=True, verbose_name='블로그')),
                ('facebook', models.URLField(blank=True, verbose_name='페이스북')),
                ('insta', models.URLField(blank=True, verbose_name='인스타')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('image_hash', models.CharField(blank=True, max_length=255, null=True)),
                ('user_id', models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, to='accounts.person', verbose_name='아이디')),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_company', models.BooleanField(default=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='지갑주소')),
            ],
        ),
    ]
