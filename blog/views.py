from django.shortcuts import render

# Create your views here.

def post_list(request):
    return render(request, 'blog/post_list.html', {})   #render関数 requestを引数に受け取り、post_list.htmlを組み立てる
