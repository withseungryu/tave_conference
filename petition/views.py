from django.shortcuts import render
from petition.forms import *
import subprocess
import os
import sys
from datetime import datetime
from imp import reload



# Create your views here.
def main(request):
    return render(request, 'main.html')

def write(request):
    if request.method == 'POST':
        form = Form(request.POST)
        
        if form.is_valid():
            form.save()
    else:
        form = Form()
    
    num = Article.objects.latest('id').id
    id = num
    
    print(id)
    #subprocess.Popen(['python','manage.py','runscript','crawling2.py'])

    return render(request, 'write.html', {'form' : form, 'id':num})

def analize(request):
   
    return redirect(request, 'list.html', {'squestion': squestion })

def list(request):
	
	#os.system('python test.py')
	articleList = Article.objects.all()
	return render(request, 'list.html', {'articleList': articleList})

def view(request, num="1"):
    import crawling2
    import test2

    a={}
    article = Article.objects.get(id=num)
    a = crawling2.similar_list
    df = crawling2.df
    c1=[]
    c2=[]
    c3=[]
    c4=[]
    
    bad1 = test2.bad1
    bad2 = test2.bad2
    bad3 = test2.bad3
    bad4 = test2.bad4
    coment1 = test2.comment1
    coment2 = test2.comment2
    coment3 = test2.comment3
    coment4 = test2.comment4 
    for v_index,v_sum in a[0:11]:
        if(crawling2.same_content!=df["content"][v_index]):
            c1.append(round(v_sum,2))
            c2.append(df["votes"][v_index])
            c3.append(df["start"][v_index])
            c4.append(df["article_id"][v_index])
    if(len(c1)>0 & len(c2)>0 & len(c3)>0&len(c4)):
        del c1
        del c2
        del c3
        del c4
        c1=[]
        c2=[]
        c3=[]
        c4=[]
    
   
    return render(request, 'view.html', {'article' : article, 'list' : a, 'df' :df, 'c1' : c1, 'c2' : c2, 'c3':c3, 'c4':c4, 'bad1' :bad1, 'bad2' :bad2,'bad3' :bad3,'bad4' :bad4, 'comment1' :coment1, 'comment2' :coment2,'comment3' :coment3,'comment4' :coment4,})

# Create your views here.
def word(request):
    # import petiword
    
    return render(request, 'word.html')
