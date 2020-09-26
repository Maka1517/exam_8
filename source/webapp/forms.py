from django import forms
from django.core.exceptions import ValidationError

from webapp.models import Product


class ProductForm(forms.ModelForm):
    # summary = forms.CharField(max_length=200, required=True, label='Заголовок')
    # description = forms.CharField(max_length=3000, required=False, label='Описание', widget=forms.Textarea)
    # status = forms.ChoiceField(choices=STATUS_CHOICES, initial=default_status, label='Статус')
    # issue_type = forms.ChoiceField(choices=TYPE_CHOICES, initial=default_type, label='Тип')
    # created_at = forms.DateTimeField(required=False, label='Время записи',
    #                                  input_formats=['%Y-%m-%d', BROWSER_DATETIME_FORMAT,
    #                                                 '%Y-%m-%dT%H:%M:%S', '%Y-%m-%d %H:%M',
    #                                                 '%Y-%m-%d %H:%M:%S'],
    #                                  widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    class Meta:
        model = Product
        exclude = []

    def clean_title(self):
        name = self.cleaned_data['name']
        if len(name) < 5:
            raise ValidationError('Title is too short!')
        return name

    def clean(self):
        cleaned_data = super().clean()
        errors = []
        description = cleaned_data.get('description')
        name = cleaned_data.get('name')
        if description and name and description == name:
            errors.append(ValidationError("Text of the description should not duplicate it's name!"))
        if errors:
            raise ValidationError(errors)
        return cleaned_data