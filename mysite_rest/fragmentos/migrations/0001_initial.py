# Generated by Django 4.0.3 on 2022-04-01 07:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Fragmento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('highlighted', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(blank=True, default='', max_length=100)),
                ('code', models.TextField()),
                ('linenos', models.BooleanField(default=False)),
                ('lenguage', models.CharField(choices=[('abap', 'abap'), ('algol', 'algol'), ('algol_nu', 'algol_nu'), ('arduino', 'arduino'), ('autumn', 'autumn'), ('borland', 'borland'), ('bw', 'bw'), ('colorful', 'colorful'), ('default', 'default'), ('dracula', 'dracula'), ('emacs', 'emacs'), ('friendly', 'friendly'), ('friendly_grayscale', 'friendly_grayscale'), ('fruity', 'fruity'), ('gruvbox-dark', 'gruvbox-dark'), ('gruvbox-light', 'gruvbox-light'), ('igor', 'igor'), ('inkpot', 'inkpot'), ('lilypond', 'lilypond'), ('lovelace', 'lovelace'), ('manni', 'manni'), ('material', 'material'), ('monokai', 'monokai'), ('murphy', 'murphy'), ('native', 'native'), ('one-dark', 'one-dark'), ('paraiso-dark', 'paraiso-dark'), ('paraiso-light', 'paraiso-light'), ('pastie', 'pastie'), ('perldoc', 'perldoc'), ('rainbow_dash', 'rainbow_dash'), ('rrt', 'rrt'), ('sas', 'sas'), ('solarized-dark', 'solarized-dark'), ('solarized-light', 'solarized-light'), ('stata', 'stata'), ('stata-dark', 'stata-dark'), ('stata-light', 'stata-light'), ('tango', 'tango'), ('trac', 'trac'), ('vim', 'vim'), ('vs', 'vs'), ('xcode', 'xcode'), ('zenburn', 'zenburn')], default='python', max_length=100)),
                ('style', models.CharField(choices=[('abap', 'abap'), ('algol', 'algol'), ('algol_nu', 'algol_nu'), ('arduino', 'arduino'), ('autumn', 'autumn'), ('borland', 'borland'), ('bw', 'bw'), ('colorful', 'colorful'), ('default', 'default'), ('dracula', 'dracula'), ('emacs', 'emacs'), ('friendly', 'friendly'), ('friendly_grayscale', 'friendly_grayscale'), ('fruity', 'fruity'), ('gruvbox-dark', 'gruvbox-dark'), ('gruvbox-light', 'gruvbox-light'), ('igor', 'igor'), ('inkpot', 'inkpot'), ('lilypond', 'lilypond'), ('lovelace', 'lovelace'), ('manni', 'manni'), ('material', 'material'), ('monokai', 'monokai'), ('murphy', 'murphy'), ('native', 'native'), ('one-dark', 'one-dark'), ('paraiso-dark', 'paraiso-dark'), ('paraiso-light', 'paraiso-light'), ('pastie', 'pastie'), ('perldoc', 'perldoc'), ('rainbow_dash', 'rainbow_dash'), ('rrt', 'rrt'), ('sas', 'sas'), ('solarized-dark', 'solarized-dark'), ('solarized-light', 'solarized-light'), ('stata', 'stata'), ('stata-dark', 'stata-dark'), ('stata-light', 'stata-light'), ('tango', 'tango'), ('trac', 'trac'), ('vim', 'vim'), ('vs', 'vs'), ('xcode', 'xcode'), ('zenburn', 'zenburn')], default='friendly', max_length=100)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fragmentos', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
    ]
