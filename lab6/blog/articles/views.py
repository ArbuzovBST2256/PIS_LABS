from django.http import Http404
from django.shortcuts import render, redirect
from .models import Article
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


def archive(request):
    return render(request, 'archive.html', {
        "posts": Article.objects.all()
    })

def get_article(request, article_id):
    try:
        post = Article.objects.get(id=article_id)
        return render(request, 'article.html', {"post": post})
    except Article.DoesNotExist:
        raise Http404


def create_post(request):
    if not request.user.is_anonymous:
        if request.method == "POST":
            form = {
                'text': request.POST.get("text", ""),
                'title': request.POST.get("title", "")
            }

            if form["text"] and form["title"]:
                if Article.objects.filter(title=form["title"]).exists():
                    form['errors'] = "Статья с таким названием уже существует"
                    return render(request, 'create_post.html', {'form': form})

                article = Article.objects.create(
                    text=form["text"],
                    title=form["title"],
                    author=request.user
                )
                return redirect('get_article', article_id=article.id)
            else:
                form['errors'] = "Не все поля заполнены"
                return render(request, 'create_post.html', {'form': form})
        else:
            return render(request, 'create_post.html', {})
    else:
        raise Http404

def register(request):
    if request.method == "POST":
        form = {
            'username': request.POST.get("username", ""),
            'email': request.POST.get("email", ""),
            'password': request.POST.get("password", "")
        }

        if form["username"] and form["email"] and form["password"]:
            try:
                User.objects.get(username=form["username"])
                form["errors"] = "Пользователь с таким именем уже существует"
                return render(request, "register.html", {"form": form})
            except User.DoesNotExist:
                User.objects.create_user(
                    form["username"],
                    form["email"],
                    form["password"]
                )
                return redirect("archive")
        else:
            form["errors"] = "Не все поля заполнены"
            return render(request, "register.html", {"form": form})
    else:
        return render(request, "register.html", {})

def user_login(request):
    if request.method == "POST":
        form = {
            'username': request.POST.get("username", ""),
            'password': request.POST.get("password", "")
        }

        if form["username"] and form["password"]:
            user = authenticate(
                username=form["username"],
                password=form["password"]
            )
            if user is not None:
                login(request, user)
                return redirect("archive")
            else:
                form["errors"] = "Нет аккаунта с таким сочетанием имени пользователя и пароля"
                return render(request, "login.html", {"form": form})
        else:
            form["errors"] = "Не все поля заполнены"
            return render(request, "login.html", {"form": form})
    else:
        return render(request, "login.html", {})