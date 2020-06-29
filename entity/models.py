from model_utils.models import TimeStampedModel

from django.contrib.postgres.fields import ArrayField
from django.db import models


class Entity(TimeStampedModel):
    """
    Entity Model extended from the abstract TimeStampedModel
    which provides fields `created` and `modified` to store
    timestamps of creation and modification of the instance.
    """

    name = models.CharField(max_length=255, null=False, blank=False)
    image_url = models.URLField(null=False)
    width = models.PositiveIntegerField(null=False)
    height = models.PositiveIntegerField(null=False)
    tags = ArrayField(models.CharField(max_length=200), blank=False, null=False)

    def __str__(self):
        return f"Entity with name: {self.name} with tags: {self.tags}"
