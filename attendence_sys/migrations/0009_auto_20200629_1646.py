from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendence_sys', '0008_auto_20200629_0102'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendence',
            name='date',
        ),
        migrations.RemoveField(
            model_name='attendence',
            name='time',
        ),
        migrations.AddField(
            model_name='attendence',
            name='date_created',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
