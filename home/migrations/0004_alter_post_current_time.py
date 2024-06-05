from datetime import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_post_current_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='current_time',
            field=models.DateTimeField(default=datetime.now),
        ),
    ]
