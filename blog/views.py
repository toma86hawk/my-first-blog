from django.shortcuts import render
from .models import Post  #クエリセットを使ってポストの一覧を操作したい
from django.utils import timezone  #クエリセットでtimezoneを使用
from django.shortcuts import render, get_object_or_404
from .forms import PostForm   #formをテンプレートに渡す
from django.shortcuts import redirect   #post_detailページを表示するツール

# Create your views here.

#urls.pyからリクエスト時にmodels.pyのデータをpost_list.htmlに渡す
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date') #クエリセットを参照するメソッド
    return render(request, 'blog/post_list.html', {'posts': posts})   #renderでrequestを引数に受け取り、post_list.htmlを組み立てる {}は指定した情報をテンプレートが表示

#ビューを追加する
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

#フォームを追加する分岐
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

#編集機能
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})