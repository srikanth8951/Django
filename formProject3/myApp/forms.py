from django import forms
from django.core import validators

class SignupForm(forms.Form):
    name=forms.CharField()
    roll=forms.IntegerField()
    email=forms.EmailField()
    phone=forms.CharField()
    comments=forms.CharField(widget=forms.Textarea)
    AreUAnEngineeringStudent=forms.BooleanField()
    password=forms.CharField(widget=forms.PasswordInput)
    repassword=forms.CharField(label='Re-enter the password',widget=forms.PasswordInput)
    
    def clean(self):
        entire_data = super().clean()
        n=entire_data['name']
        if(len(n)>10): # To check the length of the name
            raise forms.ValidationError('Number of charecter should be less than 10 charechter!')
        r=entire_data['roll']
        if(r<0): # If the roll has not entered 
            raise forms.ValidationError('Negative rollno is invalid!')
        p=entire_data['password']
        rp=entire_data['repassword']
        if(p!=rp): #to check an correct password
            raise forms.ValidationError('Missmatch in password!')