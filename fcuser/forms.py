from django import forms
from django.contrib.auth.hashers import check_password
from .models import Fcuser
from django.core.exceptions import ObjectDoesNotExist

class LoginForm(forms.Form):
    username = forms.CharField(
        error_messages={ 'required': 'Username is required' }, max_length=32, label="Username")
    password = forms.CharField(
        error_messages={ 'required': 'Password is required' },widget=forms.PasswordInput, label="Password")

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            # 예외처리
            try :
                fcuser = Fcuser.objects.get(username=username)
            except Fcuser.DoesNotExist:
                self.add_error('username', 'Username does not exist')
                return

            # if not check_password(password, fcuser.password):
            if not password == fcuser.password :
                #지금까지 계속해서 check_password가 안 되고 있음. 이유를 모르네..
                self.add_error('password', 'Wrong Password')
            else :
                self.user_id = fcuser.id