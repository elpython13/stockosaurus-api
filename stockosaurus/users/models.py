from django.db import models

owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE)
