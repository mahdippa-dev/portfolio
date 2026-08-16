from django import forms
from .models import ContactMessage
import re


class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = [
            'name',
            'email',
            'phone',
            'subject',
            'message',
        ]

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'نام شما'
                }
            ),

            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'ایمیل شما'
                }
            ),

            'phone': forms.TextInput(
                attrs={
                    'placeholder': '☓☓☓☓☓☓☓☓☓۰۹'
                }
            ),

            'subject': forms.TextInput(
                attrs={
                    'placeholder': 'موضوع پیام'
                }
            ),

            'message': forms.Textarea(
                attrs={
                    'placeholder': 'پیام خود را بنویسید...',
                    'rows': 6
                }
            ),
        }

    def clean(self):
        cleaned_data = super().clean()

        email = cleaned_data.get('email')
        phone = cleaned_data.get('phone')

        if not email and not phone:
            raise forms.ValidationError(
                'لطفاً ایمیل یا شماره موبایل خود را وارد کنید.'
            )

        return cleaned_data

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')

        if phone:
            if not re.fullmatch(r'09\d{9}', phone):
                raise forms.ValidationError(
                    'شماره موبایل باید به صورت 09123456789 وارد شود.'
                )

        return phone
