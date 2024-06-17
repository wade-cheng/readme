from django.shortcuts import render
import markdown

# Create your views here.

from django.http import HttpResponseRedirect
from articles.forms import CommentForm, ArticleForm
from articles.models import Post, Comment, Author, Issue, Category
from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


def article_index(request):
    posts = Post.objects.all().order_by("-created_on")
    context = {
        "posts": posts,
    }
    return render(request, "article/index.html", context)

def article_author_index(request):
    authors = Author.objects.all()
    context = {
        "authors": authors,
    }
    return render(request, "article/authorlist.html", context)

def article_category_index(request):
    categories = Category.objects.all()
    context = {
        "categories": categories,
    }
    return render(request, "article/categorylist.html", context)


def article_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category

    ).order_by("-created_on")
    context = {
        "category": category,
        "posts": posts,
    }
    return render(request, "article/category.html", context)

def article_author(request, author):
    posts = Post.objects.filter(
        authors__name__contains=author
    ).order_by("-created_on")
    aut = Author.objects.filter(
        name__contains=author
    ).first()
    context = {
        "a": aut,
        "author":author,
        "posts": posts,
    }
    return render(request, "article/author.html", context)

def article_issue(request, issue):
    posts = Post.objects.filter(
        issues__name__contains=issue
    ).order_by("-created_on")
    issue_info = Issue.objects.filter(
        name__contains=issue
    ).first()
    context = {
        "i": issue_info,
        "issue": issue,
        "posts": posts,
    }
    return render(request, "article/issue.html", context)

def article_detail(request, slug, pk):
    post = Post.objects.get(slug=slug, pk=pk)
    comments = Comment.objects.filter(post=post)
    form = CommentForm()
    md = markdown.Markdown(extensions=["fenced_code"])
    content = md.convert(post.body)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author = form.cleaned_data["author"],
                body = form.cleaned_data["body"],
                post = post,
            )
            comment.save()
            return HttpResponseRedirect(request.path_info)
        
    context = {
        "post": post,
        "comments": comments,
        "form": CommentForm(),
        "content": content,
    }

    

    return render(request, "article/detail.html", context)


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('create_article')
        else:
            return render(request, 'article/login.html', {'error': 'Invalid credentials'})
    return render(request, 'article/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'article/signup.html', {'form': form})

@login_required
def home_view(request):
    user = request.user
    context = {
        "user" : user
    }
    
    return render(request, 'article/create-article.html', context)


def create_article_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('article_success')
    else:
        form = ArticleForm()
    return render(request, 'article/create_article.html', {'form': form})

def article_success_view(request):
    return render(request, 'article/article_success.html')