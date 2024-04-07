from django import forms
from .models import Student

class StudentSignupForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'enrolment_no', 'password']

    # Add custom clean_password2 method to ensure password confirmation
    def clean_password2(self):
        password1 = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2
