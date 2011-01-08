from pytask.taskapp.models import Task
from django.http import Http404

def getTask(tid):

    try:
        task = Task.objects.get(uniq_key=tid)
        return task
    except Task.DoesNotExist:
        raise Http404

