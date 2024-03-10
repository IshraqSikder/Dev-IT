from django import forms
from .models import Course, Comment

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        exclude = ['author']
        
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
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']
        
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

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     if self.instance and self.instance.user:
    #         self.fields['name'].initial = self.instance.user.get_full_name()
    #         self.fields['email'].initial = self.instance.user.email
            
    #     elif self.instance and not self.instance.user:
    #         user = self.initial.get('user')
    #         if user and user.is_authenticated:
    #             self.fields['name'].initial = user.get_full_name()
    #             self.fields['email'].initial = user.email