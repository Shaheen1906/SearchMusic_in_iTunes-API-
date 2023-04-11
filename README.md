# SearchMusic_in_iTunes-API-
 
1. A Django app named "searchapp", which contains a single view function and a template for rendering search results.

2. A URL pattern that maps the root URL of the website to the "search" view.

3. A search form in the "search.html" template, which allows users to search for music by submitting a search term.

4. A view function named "search" in "views.py", which handles incoming requests to search for music and retrieves results from the iTunes API.

5. A template named "search_results.html" that displays the search results returned by the iTunes API.

Steps to run the project:
1. Go to the folder where manage.py is their.
2. Run the project by "python manage.py runserver" command.
3. It will show you the first page on this url: http://127.0.0.1:8000/
4. You have to the search keyword in the url to go the html page like this: http://127.0.0.1:8000/search/
5. Now, you can enter whaterver song you want to search and hit enter or click on sumbit button, it will show you the list of all the related results.
