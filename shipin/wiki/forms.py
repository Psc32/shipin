from django import forms
from wiki.models import Category, Page


class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128, label='分类名称', help_text='请输入视频分类名称')
    
    class Meta:
        model = Category
        fields = ('name', )
        
        
class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=128, label='网页标题', help_text='请输入网页标题')
    url = forms.URLField(max_length=128, label='网页网址', help_text='请输入网页网址')
    
    class Meta:
        model = Page
        exclude = ('category', 'views')
    def clean(self):
        cleanedData = self.cleaned_data
        url = cleanedData.get('url')
        if url and not url.startswith('http://'):
            url = 'http://' + url
            cleanedData['url'] = url
        return cleanedData