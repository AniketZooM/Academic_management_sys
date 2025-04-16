from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_noteandsheet_upload_note'),
    ]

    operations = [
        migrations.AddField(
            model_name='noteandsheet',
            name='teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.teacher'),
        ),
        migrations.AlterField(
            model_name='classwithsubject',
            name='s_class',
            field=models.CharField(blank=True, choices=[('First', 'First'), ('Second', 'Second'), ('Third', 'Third'), ('Fourth', 'Fourth'), ('Fifth', 'Fifth'), ('Sixth', 'Sixth'), ('Seventh', 'Seventh'), ('Eighth', 'Eighth'), ('Ninth (Science)', 'Ninth (Science)'), ('Ninth (Business Education)', 'Ninth (Business Education)'), ('Ninth (Humanities)', 'Ninth (Humanities)'), ('Tenth (Science)', 'Tenth (Science)'), ('Tenth (Business Education)', 'Tenth (Business Education)'), ('Tenth (Humanities)', 'Tenth (Humanities)'), ('Eleventh (Science)', 'Eleventh (Science)'), ('Eleventh (Business Education)', 'Eleventh (Business Education)'), ('Eleventh (Humanities)', 'Eleventh (Humanities)'), ('Twelfth (Science)', 'Twelfth (Science)'), ('Twelfth (Business Education)', 'Twelfth (Business Education)'), ('Twelfth (Humanities)', 'Twelfth (Humanities)')], max_length=50, null=True),
        ),
    ]
