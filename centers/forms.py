from django.forms import ModelForm

# Models
from centers.models import Center


class CenterForm(ModelForm):
    class Meta:
        model = Center
        fields = ['name']
