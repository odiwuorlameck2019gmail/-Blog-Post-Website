from django.shortcuts import render,redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            # loging the user into the blog
            return redirect("articles:list")
    else:
        form=UserCreationForm()
    return render(request,'signup.html',{'form':form})



def login_view(request):
    if request.method == 'POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
               return redirect('articles:list')
    else:
        form=AuthenticationForm()

    return render(request,"login.html",{'form':form})



def hompage_view(request):
    return render(request,'homepage.html')

def logout_view(request):
    if request.method=='POST':
        logout(request)
        return redirect('articles:list')