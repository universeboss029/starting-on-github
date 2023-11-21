from django.shortcuts import render, redirect
from django.http import HttpResponse
from appzz.models import studentsinfo
# Create your views here.

def hello (request):
    print("hiiiiiiiiiii")
    return HttpResponse("i am a good devloper...")


def done (request):
    return HttpResponse("we all are fine...")


def ok (request):
    return HttpResponse("we all are okkk...")


def showpage (request):
    return render(request, 'abc.html')


def dataform (request):
    return render(request, 'savedata.html' )


def savedata (request):
    if request.method == "POST":
        id = request.POST.get('stud')
        first_name  = request.POST.get('fname')
        lst_name = request.POST.get('lname')
        number = request.POST.get('phone')
        msg = request.POST.get('msg')

        print(id, first_name, lst_name, number, msg)

        # saveda = studentsinfo(stu_id = id, stu_f_name = first_name, stu_l_name = lst_name,
        # phone_number = number, stu_message = msg) 
        # saveda.save()  

        return redirect('dataform')
                                                  


    return HttpResponse("i am a good devloper...")



    
def first(request):
    return render(request, 'first.html')


def second(request):
    return render(request, 'second.html')


