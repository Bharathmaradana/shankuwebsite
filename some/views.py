#from django.shortcuts import render

#from .models import post_id

from django.shortcuts import redirect, render
from .models import post_id

#def createpost(request):
     #   if request.method == 'POST':
     #       if request.POST.get('title') and request.POST.get('content') and request.POST.get('summary'):
       #         post=post_id()
       #         post.title= request.POST.get('title')
      #          post.content= request.POST.get('content')
      #          post.summary= request.POST.get('summary')
      #          post.save()
      #          
       #         return render(request, 'three.html')  
#
      #  else:
       #         return render(request,'three.html')

# Create your views here.
def createpost(request):
        if request.method == 'POST':
          title = request.POST.get('title')
          content = request.POST.get('content')
          summary = request.POST.get('summary')

          new_user = post_id(title=title , content=content, summary=summary)
          new_user.save()
        return render(request, 'three.html',{})
        
