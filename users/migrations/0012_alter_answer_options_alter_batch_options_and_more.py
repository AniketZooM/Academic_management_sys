

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_quizcategory_question_answer'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answer',
            options={'verbose_name_plural': 'Quiz Answers'},
        ),
        migrations.AlterModelOptions(
            name='batch',
            options={'verbose_name_plural': 'Batch Creation'},
        ),
        migrations.AlterModelOptions(
            name='classwithsubject',
            options={'verbose_name_plural': 'Class and Subject Selection'},
        ),
        migrations.AlterModelOptions(
            name='createexam',
            options={'verbose_name_plural': 'Create Exam'},
        ),
        migrations.AlterModelOptions(
            name='customuser',
            options={'verbose_name_plural': 'User Account *VIP*'},
        ),
        migrations.AlterModelOptions(
            name='guardian',
            options={'verbose_name_plural': 'User (Guardian)'},
        ),
        migrations.AlterModelOptions(
            name='homework',
            options={'verbose_name_plural': 'Homework Assigned by Teachers'},
        ),
        migrations.AlterModelOptions(
            name='makebatch',
            options={'verbose_name_plural': 'Batch and Subject-Based Teacher'},
        ),
        migrations.AlterModelOptions(
            name='marksofstudent',
            options={'verbose_name_plural': 'Marks of Students'},
        ),
        migrations.AlterModelOptions(
            name='messageforstudent',
            options={'verbose_name_plural': 'Send Messages to Students'},
        ),
        migrations.AlterModelOptions(
            name='messageforteacher',
            options={'verbose_name_plural': 'Send Messages to Teachers'},
        ),
        migrations.AlterModelOptions(
            name='noteandsheet',
            options={'verbose_name_plural': 'Notes Given by Teachers'},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'verbose_name_plural': 'Quiz Questions'},
        ),
        migrations.AlterModelOptions(
            name='quizcategory',
            options={'verbose_name_plural': 'Quiz Categories'},
        ),
        migrations.AlterModelOptions(
            name='shift',
            options={'verbose_name_plural': 'Shift Creation'},
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name_plural': 'User (Student)'},
        ),
        migrations.AlterModelOptions(
            name='subjects',
            options={'verbose_name_plural': 'Add Subject'},
        ),
        migrations.AlterModelOptions(
            name='teacher',
            options={'verbose_name_plural': 'User (Teacher)'},
        ),
        migrations.AddField(
            model_name='quizcategory',
            name='class_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.classwithsubject'),
        ),
        migrations.AddField(
            model_name='quizcategory',
            name='subject',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.subjects'),
        ),
        migrations.AddField(
            model_name='quizcategory',
            name='teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.teacher'),
        ),
    ]
