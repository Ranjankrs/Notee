from django.forms import ModelForm

from noteapp.models import TODO
class TODOForm(ModelForm):
    class Meta:
        model = TODO
        fields = ['title' , 'status' ]