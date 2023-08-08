from django.shortcuts import render

# Create your views here.


from .models import Question,Answer
from .forms import AnswerForm



def list_question(request):

    data = Question.objects.all()
    return render(request,'forumXO/forum_list.html',{'data':data})




def detail_question(request,id):
    
    question= Question.objects.get(id=id)


    if request.method == 'POST':
        form = AnswerForm(request.POST)

        if form.is_valid():
            myform = form.save(commit=False)
            myform.author = request.user
            myform.question= question
            myform.save() 
    else:
        form =AnswerForm()


        
    return render(request,'forumXO/detail_list.html',{'question':question,'form':form})



