from django import forms
from .models import ContactMessage


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ["name", "phone", "subject", "city", "message", "notify_me"]

        widgets = {
            "name": forms.TextInput(attrs={
                "class": "input",
                "placeholder": "مثال: علی رضایی",
            }),
            "phone": forms.TextInput(attrs={
                "class": "input",
                "placeholder": "مثال: ۰۹۱۲۳۴۵۶۷۸۹",
            }),
            "subject": forms.Select(attrs={
                "class": "input",
            }),
            "city": forms.TextInput(attrs={
                "class": "input",
                "placeholder": "مثال: اصفهان",
            }),
            "message": forms.Textarea(attrs={
                "class": "input contact-textarea",
                "rows": 5,
                "placeholder": "سوال یا توضیح خود را بنویسید...",
            }),
            "notify_me": forms.CheckboxInput(),
        }

        labels = {
            "name": "نام و نام خانوادگی",
            "phone": "شماره تماس",
            "subject": "موضوع",
            "city": "شهر",
            "message": "متن پیام",
            "notify_me": "مایلم در صورت موجود شدن خودروهای مشابه، به من اطلاع داده شود.",
        }
