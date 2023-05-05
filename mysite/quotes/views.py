from django.db.models import Count
from django.shortcuts import render, redirect
from django.core.paginator import Paginator


from .utils import get_mongodb
from .models import Author, Quote, Tag
from .forms import QuoteForm, AuthorForm, TagForm


def main(request, page=1):
    db = get_mongodb()
    quotes = db.quote.find()
    per_page = 10
    paginator = Paginator(list(quotes), per_page)
    quotes_on_page = paginator.page(page)
    return render(request, "quotes/index.html", context={'quotes': quotes_on_page})

def author_about(request, _id):
    print(_id)
    author = Author.objects.get(pk=_id)
    print(author.fullname, type(author))

    return render(request, 'quotes/author.html', context={'author': author})

def add_quote(request):
    if request.method == "POST":
        form = QuoteForm(request.POST)
        if form.is_valid():
            new_quote = form.save()
            return redirect(to="quotes:root")
        else:
            return render(request, "quotes/add_quote.html",
                          context={'form': QuoteForm(), "message": "Form not valid"})
    return render(request, "quotes/add_quote.html", context={'form': QuoteForm()})

def add_author(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            new_quote = form.save()
            return redirect(to="quotes:root")
        else:
            return render(request, "quotes/add_author.html",
                          context={'form': AuthorForm(), "message": "Form not valid"})
    return render(request, "quotes/add_author.html", context={'form': AuthorForm()})







