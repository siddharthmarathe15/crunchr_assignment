from django.http import JsonResponse

from data_statistics.helpers import get_companies_by_location_and_percentage, get_companies_by_their_average_age


def search_by_location(request):
    continent = request.GET.get('location')
    percentage = int(request.GET.get('percentage', 0))

    result = get_companies_by_location_and_percentage(continent, percentage)

    if not result:
        return JsonResponse({'message': 'No data found for passed criteria'}, safe=False)
    return JsonResponse(list(result), safe=False)


def search_by_age(request):
    age = request.GET.get('age')

    result = get_companies_by_their_average_age(age)

    if not result:
        return JsonResponse({'message': 'No data found for passed criteria'}, safe=False)
    return JsonResponse(result, safe=False)
