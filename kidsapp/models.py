from django.db import models
from django.urls import reverse

# Create your models here.
class TaskUser(models.Model):
    name = models.CharField(max_length=50)
    inactive = models.BooleanField(default=False)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

class Task(models.Model):
    NS = 'Not Started'
    IP = 'In Progress'
    DN = 'Done'
    STATUS_OPTIONS = [
        (NS, 'Not Started'),
        (IP, 'In Progress'),
        (DN, 'Done'),
    ]
    status = models.CharField(max_length=30, choices=STATUS_OPTIONS, default= NS)
    follow_up_date = models.DateField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    assign_to = models.ForeignKey(TaskUser, null=True, blank=True, on_delete=models.SET_NULL)
    priority = models.IntegerField(default=0)

class Denial(Task):
    visit_id = models.CharField(max_length=30, null=True, blank=True)
    carrier_code = models.CharField(max_length=30, null=True, blank=True)
    carrier = models.CharField(max_length=150, null=True, blank=True)
    reason_code = models.CharField(max_length=10, null=True, blank=True)
    reason = models.TextField(null=True, blank=True)
    date_of_service = models.DateField(null=True, blank=True)

    # class Meta:
    #      permissions = (
    #                     ('kn_upload_denial', 'Upload Denial'),
    #                     ('kn_create_denial', 'Create Denial'),
    #                     ('kn_delete_denial', 'Delete Denial'),
    #                     ('kn_view_denial',   'View Denial'),
    #                     ('kn_update_denial', 'Update Denial'),
    #      )

    def get_absolute_url(self):
        #return reverse('kidsapp:detail', kwargs={'pk': self.pk})
        # return reverse('denial-list', kwargs={'pk': self.pk})
        return reverse('denial-list')

    def __str__(self):
        return self.visit_id
