from django import forms

class TaskForm():
    title = forms.CharField(label="Título Label",max_length=100)
    description = forms.Textarea(label="Título Label")