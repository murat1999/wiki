from django.shortcuts import render
import markdown2

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def wiki(request, title):
    return render(request, "encyclopedia/wiki.html", {
        "entries": markdown2.markdown(util.get_entry(title)), "title": title.capitalize()
    })

def search(request):
    if request.method == "POST":
        query = request.POST.get('q')
        entries = util.list_entries()
        if query in entries:
            return render(request, "encyclopedia/search.html", {
                "content": markdown2.markdown(util.get_entry(query)),
                "title": query
            })