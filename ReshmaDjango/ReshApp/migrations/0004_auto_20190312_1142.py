# Generated by Django 2.1.7 on 2019-03-12 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ReshApp', '0003_auto_20190311_1837'),
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sid', models.CharField(max_length=10)),
                ('sname', models.CharField(max_length=24)),
            ],
        ),
        migrations.DeleteModel(
            name='Emp',
        ),
        migrations.DeleteModel(
            name='NetworksModels',
        ),
    ]
