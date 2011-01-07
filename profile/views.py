from django.shortcuts import render_to_response, redirect

from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_protect

from pytask.profile.forms import EditProfileForm

@login_required
def view_profile(request):

    user = request.user
    profile = user.get_profile()

    context = {"user": user,
               "profile": profile,
              }
    return render_to_response("profile/view.html", context)

@login_required
def edit_profile(request):

    user = request.user
    profile = user.get_profile()

    context = {"user": user,
               "profile": profile,
              }

    context.update(csrf(request))

    if request.method == "POST":
        form = EditProfileForm(request.POST, instance=profile)

        if form.is_valid():
            form.save()
            return redirect("/accounts/profile/view")
        else:
            context.update({"form":form})
            return render_to_response("profile/edit.html", context)
    else:
        form = EditProfileForm(instance=profile)
        context.update({"form":form})
        return render_to_response("profile/edit.html", context)

@login_required
def browse_notifications(request):
    """ get the list of notifications that are not deleted and display in
    datetime order."""

    user = get_user(request.user)

    active_notifications = user.notification_sent_to.filter(is_deleted=False).order_by('sent_date').reverse()

    context = {'user':user,
               'notifications':active_notifications,
              }                               

    return render_to_response('profile/browse_notifications.html', context)
