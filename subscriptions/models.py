from django.db.models import Model, BooleanField, CharField,  ForeignKey, DateTimeField
from datetime import datetime, timedelta
import pytz

class Frequency(Model):
    AVAILABLE_FREQUENCIES = (
        ('0', 'dzienna'),
        ('1', 'tygodniowa'),
        ('2', 'miesięczna'),
        ('3', 'roczna'),
    )

    frequency = CharField(max_length=1, choices=AVAILABLE_FREQUENCIES)
    interval = CharField(max_length=100, default='')

    def __str__(self):
        name = '{frequency} {interval}'.format(frequency=self.get_frequency_display(), interval=self.interval)
        return name


class Animal(Model):
    is_cat = BooleanField(default=False)
    is_dog = BooleanField(default=False)

    def __str__(self):
        animals = []
        if self.is_cat:
            animals.append('koty')
        if self.is_dog:
            animals.append('psy')
        return ', '.join(animals)


class Subscription(Model):
    user = ForeignKey('auth.User')
    frequency = ForeignKey(Frequency)
    animals = ForeignKey(Animal)
    created_date = DateTimeField(default=datetime.now())
    expiration_date = DateTimeField(default=datetime.now() + timedelta(days=30))
    is_active = BooleanField(default=True)

    def delete_subscription(self):
        self.is_active = False
        self.save()

    def __str__(self):
        days = (self.expiration_date - datetime.now(pytz.utc)).days
        day = 'dni'
        if days is 1:
            day = 'dzień'
        name = '{user}: {frequency} - {animals}. Wygaśnie za {days} {day}.'.format(user=self.user, frequency=self.frequency,                                                        animals=self.animals, days=days, day=day)
        return name

    def get_days(self):
        days = (self.expiration_date - datetime.now(pytz.utc)).days
        day = 'dni'
        if days is 1:
            day = 'dzień'
        name = '{days} {day}'.format(days=days, day=day)
        return name