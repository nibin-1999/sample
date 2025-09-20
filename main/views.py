from rest_framework.decorators import api_view
from rest_framework.response import Response
from django_countries import countries
from .serializers import CountrySerializer


@api_view(['GET'])
def country_list(request):
    search_query = request.query_params.get('search', None)

    if search_query:
        filtered_countries = [
            c for c in countries
            if search_query.lower() in c.name.lower()
        ]
        serializer = CountrySerializer(filtered_countries, many=True)
    else:
        serializer = CountrySerializer(countries, many=True)

    return Response(serializer.data)
