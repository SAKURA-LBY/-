from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,JsonResponse
from django.views import View
from .models import book_heroinfo,book_bookinfo
from datetime import date
import json
from django.db.models import Q
from django.db.models import Sum

class UpdateDb(View):
    def get(self,request):
        id=request.GET.get('id')
        if id:

            print([book.title for book in book_bookinfo.objects.filter(id=id)])
            return JsonResponse([book.title for book in book_bookinfo.objects.filter(id=id)],safe=False)
        return JsonResponse({"data": [book.title for book in book_bookinfo.objects.all()]})
    def post(self,request):

        book = book_bookinfo.objects.create(
            title='西游记1',
            bpub_date=date(2019, 11, 10),
            bread=100,
            bcomment=100,
            isDelete=0,
        )

        book_heroinfo.objects.create(
            hname='沙悟净1',
            hgender=0,
            isDelete=0,
            hbook_id=book,
        )

        return HttpResponse('增加数据成功')
    def delete(self,request):

        book_bookinfo.objects.filter(title='西游记').delete()

        return HttpResponse('删除成功')

    def put(self,request):
        book_heroinfo.objects.filter(hname='沙悟净').update(hname='沙吊')


        return HttpResponse('修改成功')

def book(request):
    json_str=request.body.decode()
    req_data = json.loads(json_str)
    # req_data.id
    book_bookinfo.objects.filter(id=req_data.id)
    return HttpResponse('ok')
def hero(request):
    json_str=request.body.decode()
    req_data = json.loads(json_str)
    # req_data.id
    book_heroinfo.objects.filter(id=req_data.id)
    return HttpResponse('ok')
def select(request):
    # print(book_heroinfo.objects.filter(hgender=1))
    # print(book_heroinfo.objects.filter(hname__contains='黄'))
    # print(book_heroinfo.objects.filter(hbook_id__title='天龙八部'))
    # print(book_heroinfo.objects.filter(Q(id__lt=5) | Q(hgender=1)))
    # print(book_heroinfo.objects.filter(hgender=1).count())
    # print(book_bookinfo.objects.all())
    # print(book_bookinfo.objects.all()[1:5])
    return JsonResponse({'1':[a.hname for a in book_heroinfo.objects.filter(hgender=1)],
                         '2':[a.hname for a in book_heroinfo.objects.filter(hname__contains='黄')],
                         '3':[a.hname for a in book_heroinfo.objects.filter(hbook_id__title='天龙八部')],
                         '4': [a.hname for a in book_heroinfo.objects.filter(Q(id__lt=5)|Q(hgender=1))],
                         '5':  book_heroinfo.objects.filter(hgender=1).count(),
                         '6':[a.title for a in book_bookinfo.objects.filter(book_heroinfo__hname='沙悟净1')]
                         })


    # book = book_bookinfo.objects.filter(book_heroinfo__hname='沙悟净1')

    # book1 = book_bookinfo.objects.filter(book_heroinfo__hname='郭靖')

    # dict =  {
    #
    # }
    #
    # return JsonResponse(dict)


