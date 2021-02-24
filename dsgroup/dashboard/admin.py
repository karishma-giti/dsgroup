from django.contrib import admin

# Register your models here.
from .models import Intern
admin.site.register(Intern)

from .models import Trainee
admin.site.register(Trainee)


from .models import Trainer
admin.site.register(Trainer)

from .models import Employee
admin.site.register(Employee)

from .models import Staff
admin.site.register(Staff)


