from django.shortcuts import render
from django import views
from number.forms import NumWordForm
from num2words import num2words
from django.contrib import messages
# Create your views here.



class NumWordView(views.View):
    def get(self,request,*args,**kwargs):

        form = NumWordForm(request.GET)
        result=""
        if form.is_valid():
            num = request.GET.get("number", "")
            if int(num) < 0:
                messages.error(request, "number must be +ve integer")
            else:
                result = num2words(num)

        return render(request, "home.html", {"result": result,"form":form})
