import markdown2

from django.http import Http404
from django.shortcuts import redirect, render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, entry_name):
    content = util.get_entry(entry_name)
    if content:
        html_content = markdown2.markdown(content)
        return render(request, "encyclopedia/entry.html", {'entry': html_content})
    else:
        raise Http404("Entry does not exist")

def search(request):
    # Get query from request
    query = request.GET.get('q')

    # Get list of entries for comparison with query
    entries = util.list_entries()

    # If query exactly matches an entry name, redirect to entry's page
    if query in entries:
        return redirect('entry', entry_name=query)

    # If query not an exact match, search entries for partial matches
    else:
        matches = [entry for entry in entries if query in entry]

        # Render search results template with matches
        return render(request, 'search_results.html', {
            'matches': matches
        }) 