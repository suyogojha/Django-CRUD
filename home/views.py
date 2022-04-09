from django.http import HttpResponseRedirect
from django.shortcuts import render
from home.forms import StudentRegestration
from home.models import User

# Create your views here.

# #this also save the form data to the database
# def add_show(request):
#     if request.method == 'POST':
#         fm = StudentRegestration(request.POST)
#         if fm.is_valid():
#             fm.save()
#     else:
#         fm = StudentRegestration()
#     return render(request, 'enroll/addandshow.html', {'form': fm})




def add_show(request):
    if request.method == 'POST':
        fm = StudentRegestration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name=nm, email=em, password=pw)
            reg.save()
            fm = StudentRegestration()
    else:
        fm = StudentRegestration()
    stud = User.objects.all()
    return render(request, 'enroll/addandshow.html', {'form': fm, 'stu': stud})


def delete_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
    
    
    
def update_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = StudentRegestration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm = StudentRegestration( instance=pi)
    return render(request, 'enroll/updatestudent.html', {'form': fm})