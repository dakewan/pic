from django.shortcuts import render
from app01 import models
from django.http import JsonResponse

# Create your views here.
def index(request):
    return render(request,'index.html')

def get_imgs(request):
    nid=request.GET.get('nid')
    img_list=models.Img.objects.filter(id__gt=nid)[0:10].values('id','src','title')
    img_list=list(img_list)
    ret={
        'status':True,
        'data':img_list,
    }
    return JsonResponse(ret)



