from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from users.models import User


class UserLoginForm(AuthenticationForm):

    username = forms.CharField()
    password = forms.CharField()

    class Meta:
        model = User
        fields = ('username', 'password')

    # username = forms.CharField(widget=forms.TextInput(attrs={'autofocus': True,
    #                                                          'class': 'form-control',
    #                                                          'placeholder': 'Enter username'}))
    # password = forms.CharField(widget=forms.PasswordInput(attrs={'autocomplete': 'current-password',
    #                                                              'class': 'form-control',
    #                                                              'placeholder': "Enter your password"}))


class UserRegisterForm(UserCreationForm):

    name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField()
    password2 = forms.CharField()

    class Meta:
        model = User
        fields = ('name', 'last_name', 'username', 'email', 'password1', 'password2')

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Passwords do not match')
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

    # name = forms.CharField(widget=forms.TextInput(attrs={'autofocus': True,
    #                                                     'class': 'form-control',
    #                                                     'placeholder': 'Enter name'}))
    # surname = forms.CharField(widget=forms.TextInput(attrs={'autofocus': True,
    #                                                        'class': 'form-control',
    #                                                        'placeholder': 'Enter surname'}))
    # username = forms.CharField(widget=forms.TextInput(attrs={'autofocus': True,
    #                                                          'class': 'form-control',
    #                                                          'placeholder': 'Enter username'}))
    # email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control',
    #                                                        'placeholder': 'Enter email'}))
    # password1 = forms.CharField(widget=forms.PasswordInput(attrs={'autocomplete': 'new-password',
    #                                                              'class': 'form-control',
    #                                                              'placeholder': 'Enter password'}))
    # password2 = forms.CharField(widget=forms.PasswordInput(attrs={'autocomplete': 'new-password',
    #                                                              'class': 'form-control',
    #                                                              'placeholder': 'Enter password again'}))


class ProfileForm(UserChangeForm):

    name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['name', 'last_name', 'username', 'email']

