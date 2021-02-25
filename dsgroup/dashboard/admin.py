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

from .models import InternAttendance
admin.site.register(InternAttendance)


from .models import Employee_attendence
admin.site.register(Employee_attendence)






from .models import Salary
admin.site.register(Salary)



