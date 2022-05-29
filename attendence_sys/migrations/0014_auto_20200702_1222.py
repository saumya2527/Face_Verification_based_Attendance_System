import attendence_sys.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendence_sys', '0013_auto_20200630_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty',
            name='profile_pic',
            field=models.ImageField(blank=True, height_field=600, null=True, upload_to=attendence_sys.models.user_directory_path, width_field=600),
        ),
    ]
