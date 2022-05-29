from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendence_sys', '0009_auto_20200629_1646'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Attendence',
        ),
    ]
