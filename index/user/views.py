from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ProfilePicEdit, UserRegisterForm, ProfileEdit
from .decorations import unauthenticated_user

@unauthenticated_user
def register(request):
    if request.meothod == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'welcome {username}')
            return redirect('login')

    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form':form})

@login_required
def profile_update(request):
    if request.method == 'POST':
        pic_update = ProfilePicEdit(request.POST, request.FILES,
                                    instance=request.user.profile)
        prof_update = ProfileEdit(request.POST, instance=request.user)

        if pic_update.is_valid() and prof_update.is_valid():
            pic_update.save()
            prof_update.save()
            messages.success(request, f'your profile has been updated')
            return redirect('profile')
        else:
            pic_update = ProfilePicEdit()
            prof_update = ProfileEdit()
        
        context = {
            'pic_update':pic_update,
            'prof_update':prof_update
        }
        return render(request, 'user/profile.html', context)
            