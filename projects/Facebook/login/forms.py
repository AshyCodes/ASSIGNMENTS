from django import forms
from login.models import Profile
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('photo', 'birth_date', 'gender',)