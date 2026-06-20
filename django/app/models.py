from django.db import models
from uuid import UUID
import uuid
# Create your models here.
class UUIDMixin(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True

class DataAnalyze(UUIDMixin):
    data = models.CharField('data', null=False, blank=False, max_length=50)
    description = models.TextField('description', default='Обработаны данные', max_length=250)
    type = models.CharField('type', max_length=50, default='Таблица')
    analyzed = models.DateTimeField(auto_now_add=True)

    class Meta():
        db_table = 'past_year.data_analyze'
        verbose_name = 'Data Analyze'

    def __str__(self):
        return self.data

class Workers(UUIDMixin):
    name = models.CharField('name', max_length=50, null=False, blank=False)
    surname = models.CharField('surname', max_length=50, null=False, blank=False)
    data_checked_per_day = models.IntegerField('data_checked')
    profile_created = models.DateTimeField(auto_now_add=True)

    class Meta():
        db_table = 'past_year.workers'
        verbose_name = 'Worker'
        verbose_name_plural = 'Workers'

    def __str__(self):
        return self.name

class OnVacation(UUIDMixin):
    name = models.CharField('name', max_length=50, null=False, blank=False)
    surname = models.CharField('surname', max_length=50, null=False, blank=False)
    vacation_started = models.DateField('vacation_started', null=False, blank=False)
    vacation_endings = models.DateField('vacation_endings', null=False, blank=False)

    class Meta():
        db_table = 'past_year.on_vacation'
        verbose_name = 'Worker'
        verbose_name_plural = 'Workers'
    
    def __str__(self):
        return self.name