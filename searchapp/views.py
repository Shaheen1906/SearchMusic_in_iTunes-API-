from django.shortcuts import render
import requests
# Create your views here.


def search(request):
    if request.method == 'GET':
        search_query = request.GET.get('search')
        if search_query:
            # Call iTunes API and get search results
            url = f'https://itunes.apple.com/search?term={search_query}&media=music&entity=album'
            response = requests.get(url)
            search_results = response.json()['results']
            return render(request, 'search_results.html', {'search_results': search_results})
    return render(request, 'search.html')