from django.shortcuts import render

# Create your views here.


from .models import Question,Answer




def list_question(request):

    data = Question.objects.all()
    return render(request,'forumXO/forum_list.html',{'data':data})




def detail_question(request,id):
    
    question= Question.objects.get(id=id)
    return render (request,'forumXO/detail_list.html',{'question':question})



