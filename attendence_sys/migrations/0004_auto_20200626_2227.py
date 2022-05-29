from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendence_sys', '0003_faculty_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='Faculty_Images/'),
        ),
    ]
