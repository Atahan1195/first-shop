from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from users.models import User


class UserLoginForm(AuthenticationForm):

    """
    It is a form for user login. It is used to authenticate the user.
    """

    username = forms.CharField()
    password = forms.CharField()

    class Meta:
        model = User
        fields = ('username', 'password')


class UserRegisterForm(UserCreationForm):

    """
    It is a form for user registration. It is used to create a new user.
    """

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

        """
        It is used to check if the passwords match.
        :return: password2
        """

        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Passwords do not match')
        return password2

    def save(self, commit=True):

        """
        It is used to save the user.
        :param commit: save the user
        :return: user
        """

        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class ProfileForm(UserChangeForm):

    """
    It is a form for user profile. It is used to update the user information.
    """

    name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['name', 'last_name', 'username', 'email']

