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
                    'form-control border '
                    'p-0 bg-gray-200 text-gray-700 border rounded '
                    'py-1 px-4 leading-tight focus-outline-none '
                    'focus-bg-white focus-border-gray-500'
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
                    'form-control border-top-0 border-right-0 border-left-0 '
                    'p-0 bg-gray-200 text-gray-700 border rounded '
                    'py-3 px-4 leading-tight focus-outline-none '
                    'focus-bg-white focus-border-gray-500'
                ) 
            })
