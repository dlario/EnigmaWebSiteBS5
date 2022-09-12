from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field, Div, Fieldset, HTML
from crispy_forms.bootstrap import (
    PrependedText, AppendedText, PrependedAppendedText, FormActions)
from accounts.models import Person
from .models import *

class PersonForm(forms.ModelForm):
    # department = forms.ModelChoiceField(queryset=department.objects.all())
    class Meta:
        model = Person
        fields =['first_name',
                 'middle_name',
                 'last_name']

    def __init__(self, *args, **kwargs):
        super(PersonForm, self).__init__(*args, **kwargs)

        # Uni-form
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        #helper.form_id = 'id-project'
        #action = "{% url 'home' %}"
        self.helper.form_action = 'create'
        #helper.form_class = 'form-horizontal'
        self.helper.layout = Layout(
            Div(
                Div('first_name', css_class='.col-sm-4'),
                Div('middle_name', css_class='.col-sm-4'),
                Div('last_name', css_class='.col-sm-4'), css_class='row')
        )