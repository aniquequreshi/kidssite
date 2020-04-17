from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import Permission, User
from kidsapp.models import Denial

# Create the form class.

class DenialForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(DenialForm, self).__init__(*args, **kwargs)
        # self.fields['visit_id'].disabled = True
        # self.fields['carrier_code'].disabled = True
        # self.fields['carrier'].disabled = True
        # self.fields['date_of_service'].disabled = True
        # self.fields['reason_code'].disabled = True
        # self.fields['reason'].disabled = True

    class Meta:
        model = Denial
        widgets = {
            # 'follow_up_date': forms.SelectDateWidget,
        }
        fields = [
                    'status',
                    'notes',
                    'follow_up_date',
                    # 'assign_to',
                    'reason_code',
                    'reason',
                    'date_of_service',
                    'carrier_code',
                    'carrier',


                    #'priority',


                    'visit_id'
                  ]
