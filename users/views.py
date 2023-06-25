from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import CustomUserCreationForm


def post_signup_view(request):
    if request.POST:
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            for atr in request.POST:
                if atr == 'username':
                    user = form.save(commit=False)
                    user.username = user.username.lower()
                    user.save()
                    login(request=request, user=user, )
                    return redirect(to='home')
                elif atr == 'phone_number':
                    return render(
                        request=request,
                        template_name='registration/signup.html',
                        context={
                            'script': """alert(`Warning! Phone number verification not working!`)"""
                        }
                    )
                elif atr == 'email':
                    return render(
                        request=request,
                        template_name='registration/signup.html',
                        context={
                            'script': """alert(`Warning! Email verification not working!`)"""
                        }
                    )
            return HttpResponse(f'<h1>502 bad gateway message</h1>')

        return render(
            request=request,
            template_name='registration/signup.html',
            context={
                'script': """alert(`Set a stronger password or choose a different username!`)"""
            }
        )
    return HttpResponse('<h1>404 not found</h1>')


def signup_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    return render(
        request=request,
        template_name='registration/signup.html',
        context={
            'script': 'alert(`Warning! Currently, you can only sign up using your username`)'
        }
    )


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    return render(
        request=request,
        template_name='registration/login.html',
        context={
            'script': 'alert(`Warning! Currently, you can only log in using your username`)'
        }
    )


def post_login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    elif request.POST:
        try:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request=request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(to='home')
            else:
                return render(
                    request=request,
                    template_name='registration/login.html',
                    context={
                        'script': """alert(`Warning! Username or password is incorrect`)"""
                    }
                )
        except Exception as E:
            return render(
                request=request,
                template_name='registration/login.html',
                context={
                    'script': f"""alert(`Warning! Currently, you can only log in using your username`)"""
                }
            )
