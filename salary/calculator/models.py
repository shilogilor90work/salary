from django.db import models


class Salary(models.Model):
    """Salary
    """
    HELP_CODE = 'needs to change'

    name = models.CharField(max_length=128, help_text=HELP_CODE)
    salary = models.DecimalField(default=0.0, max_digits=20, decimal_places=4, help_text=HELP_CODE)
    salary_net = models.DecimalField(default=0.0, max_digits=20, decimal_places=4, help_text=HELP_CODE)
    day_hours = models.DecimalField(default=0.0, max_digits=20, decimal_places=4, help_text=HELP_CODE)
    vacation_days = models.DecimalField(default=0.0, max_digits=20, decimal_places=4, help_text=HELP_CODE)
    travel_time = models.DecimalField(default=0.0, max_digits=20, decimal_places=4, help_text=HELP_CODE)
    sickdays_value = models.CharField(max_length=128, help_text=HELP_CODE)
    pension = models.DecimalField(default=0.0, max_digits=20, decimal_places=4, help_text=HELP_CODE)
    pitzuim = models.DecimalField(default=0.0, max_digits=20, decimal_places=4, help_text=HELP_CODE)
    hishtalmut = models.DecimalField(default=0.0, max_digits=20, decimal_places=4, help_text=HELP_CODE)
    nesiot_income = models.DecimalField(default=0.0, max_digits=20, decimal_places=4, help_text=HELP_CODE)
    gas_cost = models.DecimalField(default=0.0, max_digits=20, decimal_places=4, help_text=HELP_CODE)
    lunch = models.DecimalField(default=0.0, max_digits=20, decimal_places=4, help_text=HELP_CODE)
    holidays_like_friday = models.CharField(max_length=128, help_text=HELP_CODE)
    chol_hamoed = models.DecimalField(default=0.0, max_digits=20, decimal_places=4, help_text=HELP_CODE)
    minimum_hours_aday = models.DecimalField(default=0.0, max_digits=20, decimal_places=4, help_text=HELP_CODE)
    parking = models.DecimalField(default=0.0, max_digits=20, decimal_places=4, help_text=HELP_CODE)
    flexable_hours = models.CharField(max_length=128, help_text=HELP_CODE)

    def __str__(self):
            return f"{self.salary}"
