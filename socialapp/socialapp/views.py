from django.shortcuts import render,redirect
from .models import Profile,Rweet
from .forms import RweetForm

# Create your views here.


def dashboard(request):
    form = RweetForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            rweet = form.save(commit=False)
            rweet.user = request.user
            rweet.save()
            return redirect("socialapp:dashboard")
        
    followed_rweets = Rweet.objects.filter(
        user__profile__in=request.user.profile.follows.all()
    ).order_by("-created_at")

    return render(request, 'socialapp/dashboard.html',{"form": form,"rweets": followed_rweets})


def profile_list(request):
    profiles = Profile.objects.exclude(user=request.user)
    return render(request, "socialapp/profile_list.html", {"profiles": profiles})


def profile_page(request, pk):
    if not hasattr(request.user, 'profile'):
        missing_profile = Profile(user=request.user)
        missing_profile.save()

    profile = Profile.objects.get(pk=pk)
    if request.method == "POST":
        current_user_profile = request.user.profile
        data = request.POST
        action = data.get("follow")
        if action == "follow":
            current_user_profile.follows.add(profile)
        elif action == "unfollow":
            current_user_profile.follows.remove(profile)
        current_user_profile.save()

    return render(request, "socialapp/profile.html", {"profile": profile})
