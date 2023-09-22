from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
import requests
from django.http import JsonResponse
from django.core.paginator import Paginator

# Add function decorator,authentication and permission for authenticated users
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])

def country(request):
    # Make a GET request to the API
    url = 'https://restcountries.com/v3.1/all'
    response = requests.get(url)

    if response.status_code == 200:
        # Parse the JSON response
        countries_data = response.json()
        # Extract population, area, and language data
        country_data_list = []

        #Loop through the json data for retrieving name, population, area and languages
        for country in countries_data:
            name = country['name']['common'] #Retrieve name of the country
            population = country.get('population', 0) # Retrieve population of the country, show 0 if not found
            area = country.get('area', 0) #Retrieve area of the country, show 0 if not found
            languages = ', '.join(country.get('languages', {}).values()) #Retrieve languages of the country as values and join them together 

            country_data = { #Make a dictionary of all the retrieved Data
                'name': name,
                'population': population,
                'area': area,
                'languages': languages
            }
            country_data_list.append(country_data)# Add the above dictionary to country_data_list

        # Sort the data by population in ascending order
        sorted_country_data = sorted(country_data_list, key=lambda x: x['population'])
        
        # Pagination
        page_number = request.GET.get('page', 1)  # Get the page number from the request query parameters
        paginator = Paginator(sorted_country_data, 30)  # 30 countries per page

        try: #Making sure that user has requested for correct and available page number
            page = paginator.page(page_number)
        except EmptyPage:
            return JsonResponse({'error': 'Page not found'}, status=404) # Show error if user requested page number not found 

        return JsonResponse({ # Make dictionary of countries , current page and total number of pages remaining
            'countries': list(page),
            'total_pages': paginator.num_pages,
            'current_page': page.number,
        })
    else:
        return JsonResponse({'error': 'API request failed'}, status=500) # Return error message if request fails.

        
 

    
       


        