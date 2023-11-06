from django.shortcuts import render, redirect
from .models import Article, Comment
from .forms import ArticleForm, CommentForm

# Create your views here.
def index(request):
    articles = Article.objects.all()

    context = {
        'articles': articles,
    }

    return render(request, 'index.html', context)

def detail(request, id):
    article =Article.objects.get(id=id)
    form = CommentForm()

    #Comment 목록 조회

    #첫번째 방법
    # comments = Comment.objects.filter(article=article)

    #두번째 방법
    # comments = article.comment_set.all()

    #세번째 방법
    # HTML코드에서 zrticle.comment_set.all을 사용

    context = {
        'article':article,
        'form' : form,
        # 'comments' : comments,
    }

    return render(request, 'detail.html', context)

def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', id=article.id)
    else:
        form = ArticleForm()

    context = {
        'form': form,
    }

    return render(request, 'form.html', context)

def comment_create(request, article_id):
    form = CommentForm(request.POST)

    if form.is_valid():
        comment = form.save(commit=False)

        # 첫번째 방법(객체를 저장하는 방법)
        # article= Article.objects.get(id=article_id)
        # comment.article = article
        # comment.save()

        #두번쨰 방법(integer를 저장하는 방법)
        comment.article_id = article_id
        comment.save()

        return redirect('articles:detail', id=article_id)
    
def comment_delete(request, article_id, id):
    comment = Comment.objects.get(id=id)
    comment.delete()

    return redirect('articles:detail', id=article_id)