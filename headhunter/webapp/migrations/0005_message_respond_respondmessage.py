# Generated by Django 4.1.3 on 2022-11-21 16:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webapp', '0004_alter_resumes_author_alter_resumes_email_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(blank=True, max_length=3000, null=True, verbose_name='Текст сообщения')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
        ),
        migrations.CreateModel(
            name='Respond',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='respond_resume', to='webapp.resumes', verbose_name='Резюме')),
                ('vacancy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='respond_vacancy', to='webapp.vacancies', verbose_name='Вакансия')),
            ],
        ),
        migrations.CreateModel(
            name='RespondMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message_text', to='webapp.message', verbose_name='Сообщение')),
                ('respond', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='respond_message', to='webapp.respond', verbose_name='Отклик')),
            ],
        ),
    ]