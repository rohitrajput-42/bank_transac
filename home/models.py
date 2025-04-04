from django.db import models

class Bank(models.Model):
    description = models.TextField(null = True, blank = True)
    transaction_type = models.CharField(max_length = 100)
    credit = models.TextField(null = True, blank = True)
    debit = models.TextField(null = True, blank = True)
    running_balance = models.TextField(null = True, blank = True)
    created_ts = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.description