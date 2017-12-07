from django.shortcuts import render,HttpResponse,redirect
from django.forms import Form,ModelForm
from django.forms import fields
from django.forms import widgets as wd
# Create your views here.
from app01 import models
def login(request):
    return render(request,'login.html')

def index(request):
    questionary_list=models.Questionary.objects.all()
    return render(request,'index.html',{'questionary_list':questionary_list})
class Foo(object):
    def __init__(self,data):
        self.data=data
    def __iter__(self):
        for item in self.data:
            yield item
def test(request):
    user_list=[
        {'id':1,'name':'alex','age':19},
        {'id':2,'name':'eric','age':18},
    ]
    obj=Foo(user_list)
    return render(request,'tset.html',{'user_list':obj})
from django.forms import ModelForm
class QuestionModelForm(ModelForm):
    class Meta:
        model=models.Quesion
        fields=['quesion','tp']
class OptionModelForm(ModelForm):
    class Meta:
        model=models.One_choice
        fields=['name','score']
def questionary(request,pid):
    def inner():
        que_list=models.Quesion.objects.filter(naire_id=pid)
        if not que_list:
            form=QuestionModelForm()
            yield {'form':form,'obj':None,'option_class':'hide','options':None}
        else:
            for que in que_list:
                form=QuestionModelForm(instance=que)
                temp={'form':form,'obj':que,'option_class':'hide','options':None}
                if que.tp ==2:
                    temp['option_class']=''
                    def inner_loop(quee):
                        option_list=models.One_choice.objects.filter(question=quee)
                        for v in option_list:
                            yield {'form':OptionModelForm(instance=v),'obj':v}
                        temp['options']=inner_loop(que)
                    yield temp
    return render(request,'Questionary.html',{'form_list':inner()})

