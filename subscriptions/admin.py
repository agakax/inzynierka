from django.contrib import admin
from .models import Frequency
from .models import Animal
from .models import Subscription


admin.site.register(Subscription)
admin.site.register(Frequency)
admin.site.register(Animal)
