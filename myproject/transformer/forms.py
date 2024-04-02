from django import forms

class TranslationForm(forms.Form):
    text_to_translate = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={'placeholder': 'Çevirilecek metni buraya yazın...', 'rows': 4, 'class': 'form-control'}),
    )