# RestCountriesAPI
    This API view retrieves and paginates country data from an external API,
    sorts it by population in ascending order, and returns it in JSON format.

    Authentication:
    - Requires Token Authentication.
    - Users must be authenticated to access this data.

    Endpoint:
    - GET request to '/country/'

    Query Parameters:
    - 'page': Specify the page number to view (default is 1).
    
    Response:
    - Returns a JSON response with paginated country data, total pages, and current page.

    Example Usage:
    - GET '/country/?page=2' - Retrieves the second page of sorted country data.

     

****HOW TO SETUP, INSTALL AND RUN THE CODE****

First things FIRST, Here are some suggestions you might want to follow in order to run the code smoothly:

1.  Fork and Clone this repository on your machine.
  
2.  Use an IDE (VS code recommmended).

3.  Use the command line of the IDE to run commands (Not necessary but it will save you some time).

Now, Once you have the whole program on your machine. Below are the things you should look for.

**Prerequisites:**


1. You must have Python installed on your machine.(if not please download)

2. You must have Django installed on your machine.(if not run in your command; for windows:(pip install django), for linux 
   and Mac($ python -m pip install Django).

3. You must have django rest framework installed on your machine.(if not run in your command; for windows:(pip install 
   djangorestframework))

4. You must have "requests" installed on your machine.(if not run in your command: (pip install requests)).

5. You should have "httpie" installed on your machine.(if not run in your command:(pip install httpie))

So, Now when you have all the installations done. Its time for the real magic!. Follow along:

1.  Run this curl in your command **curl -H "Authorization: Token 223304fe845443009704f5fe9eca76cf971408fe" 
    http://localhost:8000/country/**

2.  OR Run using "httpie" in your command **http  http://127.0.0.1:8000/ 'Authorization: Token 
    223304fe845443009704f5fe9eca76cf971408fe'** (Recommended)

3.  You can see the code running.

                         **OR(if above steps fails)**

1.  Run **python manage.py migrate** in your command.For migrating all the changes.

2.  Then run **python manage.py createsuperuser**. Here you need to enter an username , email(although, you can skip this) 
    and a password.

3.  After that run **python manage.py drf_create_token {YOUR USERNAME}**

4.  Now, finally you can see your Auth Token in the command. Copy your Auth Token and run it with **curl -H "Authorization: Token 
    YOUR_TOKEN_HERE" http://localhost:8000/country/.**
 
5.  Or you can run your Auth token with "httpie" as:  **http  http://127.0.0.1:8000/ 'Authorization: Token YOUR_TOKEN_HERE**'(Recommended)

6.  You can see the code running.


P.S. Only Authorized users are allowed to see the API's Data that's why we are following above mentioned steps.
