from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Selling


class SellingForm(ModelForm):
    class Meta:
        model = Selling
        fields = '__all__'
        exclude = ['status',]