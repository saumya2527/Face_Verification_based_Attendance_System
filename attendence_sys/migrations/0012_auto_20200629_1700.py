from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendence_sys', '0011_attendence'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendence',
            name='date_created',
        ),
        migrations.AddField(
            model_name='attendence',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='attendence',
            name='time',
            field=models.TimeField(auto_now_add=True, null=True),
        ),
    ]
