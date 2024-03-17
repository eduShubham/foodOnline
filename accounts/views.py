from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserForms
from .models import User
from django.contrib import messages

def registerUser(request):
    if request.method == 'POST':
        # print('request.post')
        form = UserForms(request.POST)
        if form.is_valid():
            # user = form.save(commit=False)
            # user.role = User.CUSTOEMER
            # user.save()
            # return redirect('registerUser')

            # create the user using create_user method.
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            print('working')
            user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
            user.role = User.CUSTOEMER
            user.save()

            messages.success(request, "Your accounts is successfully registered!!")
            return redirect('registerUser')
        else:
            print('invalid forms')
            print(form.errors)



    else:
        form = UserForms()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/registerUser.html', context)
    # return HttpResponse('registration form..')

