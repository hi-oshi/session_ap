from django.shortcuts import render

# Create your views here.
from .models import Book

def listView(request):

    #Bookオブジェクトのリストを取得する
    bookList = Book.objects.all()

    #エラーの有無でフォワード先を呼び分ける
    params ={
        'bookList':bookList,
        }
    return render(request, 'list.html',params)