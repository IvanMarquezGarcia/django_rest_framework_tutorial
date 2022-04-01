from django.db import models

from pygments import highlight

from pygments.lexers import get_all_lexers, get_lexer_by_name

from pygments.formatters.html import HtmlFormatter

from pygments.styles import get_all_styles

# Create your models here.

LEXERS = [item for item in get_all_lexers() if item[1]]
LENGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])

class Fragmento(models.Model):
    owner = models.ForeignKey('auth.User', related_name = 'fragmentos', on_delete = models.CASCADE)
    highlighted = models.TextField()
    created = models.DateTimeField(auto_now_add = True)
    title = models.CharField(max_length = 100, blank = True, default = '')
    code = models.TextField(null = False)
    linenos = models.BooleanField(default = False)
    lenguage = models.CharField(choices = STYLE_CHOICES, default = 'python', max_length = 100)
    style = models.CharField(choices = STYLE_CHOICES, default = 'friendly', max_length = 100)

    def save(self, *args, **kwargs):
        # Añade código a la función save() de models.Model
	# para crear una representación coloreada del fragmento
	# de código a través de la librería 'pygments'
        lexer = get_lexer_by_name(self.lenguage)
        linenos = 'table' if self.linenos else False
        options = {'title': self.title} if self.title else {}
        formatter = HtmlFormatter(style = self.style, linenos = linenos, full = True, **options)
        self.highlighted = highlight(self.code, lexer, formatter)

        super().save(*args, **kwargs)

    class Meta:
        ordering = ['created']
