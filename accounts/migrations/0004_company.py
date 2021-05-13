# Generated by Django 3.2 on 2021-05-13 01:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0003_rename_profile_sns_user_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=13, verbose_name='전화번호')),
                ('email', models.EmailField(max_length=50, verbose_name='이메일')),
                ('regiNum', models.IntegerField(max_length=10, verbose_name='사업자번호')),
                ('compName', models.CharField(max_length=30, verbose_name='회사명')),
                ('capName', models.CharField(max_length=30, verbose_name='대표자명')),
                ('address', models.CharField(max_length=30, verbose_name='회사 주소')),
                ('employee', models.ManyToManyField(blank=True, related_name='employer', to='accounts.Profile')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='아이디')),
            ],
        ),
    ]