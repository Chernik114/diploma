# Generated by Django 3.1.6 on 2021-02-15 16:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyAnswer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='MyQuestion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='MyQuestionField',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('type', models.IntegerField(default=0)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oprosi.myquestion')),
            ],
        ),
        migrations.CreateModel(
            name='MyAnswerField',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('data', models.TextField()),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oprosi.myanswer')),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oprosi.myquestionfield')),
            ],
        ),
        migrations.AddField(
            model_name='myanswer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oprosi.myquestion'),
        ),
    ]