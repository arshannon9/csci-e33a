import markdown2
import random

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
        return render(request, "encyclopedia/entry.html", {'entry': html_content, "entry_name": entry_name})
    else:
        return render(request, 'encyclopedia/error.html', {'message':"404: Entry does not exist"})

def search(request):
    # Get query from request
    query = request.GET.get('q').lower()

    # Get list of entries for comparison with query
    entries = util.list_entries()

    # If query exactly matches an entry name, redirect to entry's page
    if query in (entry.lower() for entry in entries):
        return redirect('entry', entry_name=query)

    # If query not an exact match, search entries for partial matches
    else:
        matches = [entry for entry in entries if query in entry.lower()]

        # Render search results template with matches
        return render(request, 'encyclopedia/search_results.html', {
            'matches': matches
        }) 
    
def new_page(request):
    # Check if request method is POST (i.e., user has submitted the form)
    if request.method == "POST":
        # Retreive title and content from form
        title = request.POST.get('title')
        content = request.POST.get('content')

        # If entry already exists, return error message
        if util.get_entry(title):
            return render(request, 'encyclopedia/error.html', {'message':"Entry already exists"})
        # If entry doesn't exist, save entry and redirect to new entry's page
        else:
            util.save_entry(title, content)
            return redirect('entry', entry_name=title)
    # If request method is GET, render form for new entry
    else:
        return render(request, 'encyclopedia/new_page.html')
    

def edit_page(request, entry_name):
    # Check if entry exists; if not, return error message
    entry_content = util.get_entry(entry_name)
    if entry_content is None:
        return render(request, 'encyclopedia/error.html', {'message': "404: Entry does not exist"})
     
    # Check if request method is POST (i.e., user has submitted the form)
    if request.method == "POST":
        # Retreive new content from form
        new_content = request.POST.get('content')

        # Save new content and redirect user to updated entry page
        util.save_entry(entry_name, new_content)
        return redirect('entry', entry_name=entry_name)
    
    # If request method is GET, render edit entry form with content pre-populated
    else:
        content = util.get_entry(entry_name)
        return render(request, 'encyclopedia/edit_page.html', {'entry_name': entry_name, 'content': content})
    

def random_page(request):
    # Get all entries
    entries = util.list_entries()
    # Select a random entry
    random_entry = random.choice(entries)
    return redirect('entry', entry_name=random_entry)