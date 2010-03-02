from django import forms
from pytask.taskapp.models import Task, Claim

class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'desc', 'tags_field', 'credits']
    #publish = forms.BooleanField(required=False)

    def clean_desc(self):
        data = self.cleaned_data['desc'].strip()
        if not data:
            raise forms.ValidationError("Enter some description for the task")

        return data

def EditTaskForm(task, instance=None):
    class myForm(forms.ModelForm):
        class Meta:
            model = Task
            fields = ['title', 'desc', 'tags_field', 'credits']

        def clean_desc(self):
            data = self.cleaned_data['desc'].strip()
            if not data:
                raise forms.ValidationError("Enter some description for the task")

            return data

    data = {
        'title': task.title,
        'desc': task.desc,
        'tags_field': task.tags_field,
        'credits': task.credits,
    }
    return myForm(instance) if instance else myForm(data)

def AddMentorForm(choices,instance=None):
    """ return a form object with appropriate choices """
    
    class myform(forms.Form):
        mentor = forms.ChoiceField(choices=choices, required=True)
    form = myform(instance) if instance else myform()
    return form

class ClaimTaskForm(forms.ModelForm):
    class Meta:
        model = Claim
        fields = ['message']

def ChoiceForm(choices, instance=None):
    """ return a form object with appropriate choices """
    
    class myform(forms.Form):
        choice = forms.ChoiceField(choices=choices, required=True)
    form = myform(instance) if instance else myform()
    return form

def AddTaskForm(task_choices, is_plain=False):
    """ if is_plain is true, it means the task has no subs/deps.
    so we also give a radio button to choose between subs and dependencies.
    else we only give choices.
    """

    class myForm(forms.Form):
        if is_plain:
            type_choices = [('S','Subtasks'),('D','Dependencies')]
            type = forms.ChoiceField(type_choices, widget=forms.RadioSelect)

        task = forms.ChoiceField(choices=task_choices)
    return myForm()

def AssignCreditForm(choices, instance=None):
    
    class myForm(forms.Form):
        user = forms.ChoiceField(choices=choices, required=True)
        pynts = forms.IntegerField(min_value=0, required=True, help_text="Choose wisely since it cannot be undone.")
    return myForm(instance) if instance else myForm()

def RemoveUserForm(choices, instance=None):

    class myForm(forms.Form):
        user = forms.ChoiceField(choices=choices, required=True)
        reason = forms.CharField(min_length=1, required=True)
    return myForm(instance) if instance else myForm()

