from rest_framework.decorators import api_view
from rest_framework.response import Response
from django_countries import countries
from main.serializers import CountrySerializer
from main.functions import paginate_instances  


@api_view(['GET'])
def country_list(request):
    search_query = request.query_params.get('search', None)

    if search_query:
        filtered_countries = [
            c for c in countries
            if search_query.lower() in c.name.lower()
        ]
    else:
        filtered_countries = list(countries)

    paginated_results, pagination_info = paginate_instances(request, filtered_countries, per_page=10)

    serializer = CountrySerializer(paginated_results, many=True)

    response_data = {
        'results': serializer.data,
        'pagination_info': pagination_info,  
    }

    return Response(response_data)