from datetime import datetime
from django import forms
from django.contrib.sites import requests
from dogsite.settings import env
import requests

class ContactForm(forms.Form):
    name = forms.CharField(label='Name', max_length=255, widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    content = forms.CharField(label='Message', widget=forms.Textarea(attrs={'cols': 60, 'rows': 3}))

    def send_message_to_telegram(self):
        token = env('TOKEN')
        chat_id = env('CHAT_ID')
        current_time = datetime.now().strftime("%H:%M, %d %b %Y")
        message = f"{current_time}\nContact:\nName: {self.cleaned_data['name']}\nEmail: {self.cleaned_data['email']}\nMessage: {self.cleaned_data['content']}"

        url = f"https://api.telegram.org/bot{token}/sendMessage"
        data = {'chat_id': chat_id, 'text': message}

        response = requests.post(url, data=data)
        return response

    def process_form(self):
        self.send_message_to_telegram()
