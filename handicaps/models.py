from django.db import models
from django.utils import timezone

class Golfer(models.Model):
    first = models.CharField(max_length=25)
    last = models.CharField(max_length=25)
    suffix = models.CharField(max_length=8, blank=True, null=True)
    tees = models.CharField(max_length=1, choices=[('M','Male'),('F','Female')])
    status = models.CharField(max_length=12, choices=[('Team','Team'),('Substitute','Substitute'),('Inactive','Inactive')], default='Team')
    team = models.ForeignKey('Team', on_delete=models.CASCADE, blank=True, null=True)
    role = models.CharField(max_length=12, blank=True, null=True, default='Member', choices=[('Member','Member'),('Captain','Captain')])
    email = models.CharField(max_length=60, blank=True, null=True)
    phone = models.CharField(max_length=10, blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(default=timezone.now)
#    updated_by = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def update(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        if self.suffix == None:
            suf = ''
        else:
            suf = f' {self.suffix}'
        return f'{self.last}, {self.first}{suf}'

class Team(models.Model):
    name = models.CharField(max_length=40)
    status = models.CharField(max_length=12, choices=[('Active','Active'),('Bye','Bye Team'),('Inactive','Inactive')])

    def __str__(self):
        return self.name
