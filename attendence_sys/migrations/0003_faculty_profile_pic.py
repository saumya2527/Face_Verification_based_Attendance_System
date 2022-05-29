from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendence_sys', '0002_attendence_period'),
    ]

    operations = [
        migrations.AddField(
            model_name='faculty',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='Student_Images/'),
        ),
    ]
