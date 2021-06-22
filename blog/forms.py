from django import forms
from .models import BlogPost

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title','slug','content','image', 'publish_date']
    
    def clean_title(self,*args, **kwargs):
        '''
        Validating unique case insensitive title field
        '''
        instance = self.instance
        # print(dir(self))
        # print(self.instance)
        title = self.cleaned_data.get('title')
        queryset = BlogPost.objects.filter(title__iexact=title)
        if instance is not None:
            queryset = queryset.exclude(pk=instance.id)
        if queryset.exists():
            raise forms.ValidationError('This Title already been used, Please Enter different Title for your Post')
        return title