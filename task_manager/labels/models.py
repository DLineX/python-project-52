from django.db import models
from django.utils.translation import gettext


class Labels(models.Model):
    name = models.CharField(max_length=120, unique=True, blank=False,
                            verbose_name=gettext('Name'), )

    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name=gettext('Date of creation'))

    def __str__(self):
        return self.name
