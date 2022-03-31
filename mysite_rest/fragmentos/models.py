from django.db import models

from pygments.lexers import get_all_lexers

from pygments.styles import get_all_styles

# Create your models here.

LEXERS = [item for item in get_all_lexers() if item[1]]
LENGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])

class Fragmento(models.Model):
    created = models.DateTimeField(auto_now_add = True)
    title = models.CharField(max_length = 100, blank = True, default = '')
    code = models.TextField(null = False)
    linenos = models.BooleanField(default = False)
    lenguage = models.CharField(choices = STYLE_CHOICES, default = 'python', max_length = 100)
    style = models.CharField(choices = STYLE_CHOICES, default = 'friendly', max_length = 100)

    class Meta:
        ordering = ['created']
