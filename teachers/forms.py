from django.contrib.auth.forms import UserCreationForm
from django import forms
from .constants import GENDER_TYPE, PROFESSION_TYPE
from django.contrib.auth.models import User
from .models import UserAccount, UserAddress

class UserRegistrationForm(UserCreationForm):
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    gender = forms.ChoiceField(choices=GENDER_TYPE)
    profession = forms.ChoiceField(choices=PROFESSION_TYPE)
    street_address = forms.CharField(max_length=100)
    postal_code = forms.IntegerField()
    city = forms.CharField(max_length= 100)
    country = forms.CharField(max_length=100)
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'email', 'birth_date', 'gender', 'profession', 'street_address', 'postal_code', 'city', 'country']

    def save(self, commit=True):
        our_user = super().save(commit=False)
        if commit:
            our_user.save()
            birth_date = self.cleaned_data.get('birth_date')
            gender = self.cleaned_data.get('gender')
            profession = self.cleaned_data.get('profession')
            street_address = self.cleaned_data.get('street_address')
            postal_code = self.cleaned_data.get('postal_code')
            city = self.cleaned_data.get('city')
            country = self.cleaned_data.get('country')
            
            UserAccount.objects.create(
                user = our_user,
                birth_date =birth_date,
                gender = gender,
                profession = profession,
                account_no = 100000 + our_user.id
            )
            UserAddress.objects.create(
                user = our_user,
                street_address = street_address,
                postal_code = postal_code,
                city = city,
                country = country
            )
                
        account = our_user
        print(account)
        # account.set_password(password)
        account.is_active = False
        account.save()  
         
        return account
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for field in self.fields:
            self.fields[field].widget.attrs.update({     
                'class' : (
                    'appearance-none block w-full bg-gray-200 '
                    'text-gray-700 border border-gray-200 rounded '
                    'py-3 px-4 leading-tight focus:outline-none '
                    'focus:bg-white focus:border-gray-500'
                ) 
            })

class UserUpdateForm(forms.ModelForm):
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    gender = forms.ChoiceField(choices=GENDER_TYPE)
    profession = forms.ChoiceField(choices=PROFESSION_TYPE)
    street_address = forms.CharField(max_length=100)
    city = forms.CharField(max_length= 100)
    postal_code = forms.IntegerField()
    country = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': (
                    'appearance-none block w-full bg-gray-200 '
                    'text-gray-700 border border-gray-200 rounded '
                    'py-3 px-4 leading-tight focus:outline-none '
                    'focus:bg-white focus:border-gray-500'
                )
            })
        if self.instance:
            try:
                user_account = self.instance.account
                user_address = self.instance.address
            except UserAccount.DoesNotExist:
                user_account = None
                user_address = None

            if user_account:
                self.fields['birth_date'].initial = user_account.birth_date
                self.fields['gender'].initial = user_account.gender
                self.fields['profession'].initial = user_account.profession
                self.fields['street_address'].initial = user_address.street_address
                self.fields['city'].initial = user_address.city
                self.fields['postal_code'].initial = user_address.postal_code
                self.fields['country'].initial = user_address.country

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            
            user_account, created = UserAccount.objects.get_or_create(user=user)
            user_address, created = UserAddress.objects.get_or_create(user=user) 
            user_account.gender = self.cleaned_data['gender']
            user_account.profession = self.cleaned_data['profession']
            user_account.birth_date = self.cleaned_data['birth_date']
            user_account.save()
            
            user_address.street_address = self.cleaned_data['street_address']
            user_address.city = self.cleaned_data['city']
            user_address.postal_code = self.cleaned_data['postal_code']
            user_address.country = self.cleaned_data['country']
            user_address.save()

        return user