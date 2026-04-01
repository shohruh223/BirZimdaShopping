from django.forms.models import ModelForm
from app.models import Contact

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'