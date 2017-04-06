from django.forms import ModelForm, Textarea
from RecruStu.models import Rules


class RulesModelForm(ModelForm):
    class Meta:
        model = Rules
        widgets = {
            'parameters': Textarea(attrs={'cols': 30, 'rows': 1}),
   }