from django import forms;

from .models import Entry, Topic;

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic;
        fields = ['text'];
        labels = {'text':''};

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry;
        fields = ['text'];
        lables = {'ttext':''};
        widgets = {'text':forms.Textarea(attrs = {'cols':80})};


