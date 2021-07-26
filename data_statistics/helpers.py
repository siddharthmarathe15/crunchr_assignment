from django.db.models import Avg, Count, F, Q, Subquery, OuterRef, IntegerField

from data_statistics.models import Employee


def get_companies_by_location_and_percentage(continent, percentage):
    """
    :return: the list of companies by their location and percentage of employees by location
    [{"company_name": "ABC", "percentage": 89}]
    """
    if not (continent and percentage):
        continent, percentage = 'Europe', 80

    q_filter = Q(location__continent=continent)
    if '/' in continent:
        continent, country = continent.split('/')
        q_filter = Q(location__continent=continent) & Q(location__country=country)

    subquery = Subquery(Employee.objects.filter(company__name=OuterRef('company__name'))
                        .values('company__name')
                        .annotate(total=Count('company__name'))
                        .values('total')[:1])

    result = Employee.objects.filter(q_filter).values(company_name=F('company__name')) \
        .annotate(percentage=Count('company__name') * 100 / subquery) \
        .filter(percentage__gt=percentage)
    return result


def get_companies_by_their_average_age(age):
    """
    :return: the list of companies by their age and percentage of employees older than average
    [{"company_name": "ABC", "percentage": 89, "average_age": 39}]
    """
    result = list()
    queryset = Employee.objects.values(company_name=F('company__name')) \
        .annotate(average_age=Avg('age', output_field=IntegerField()))

    if age is None:
        return list(queryset)

    for item in queryset:
        subquery = Subquery(Employee.objects.filter(company__name=OuterRef('company_name'))
                            .values('company__name')
                            .annotate(total=Count('company__name'))
                            .values('total')[:1])
        company_avg_age_data = list(
            Employee.objects.filter(company__name=item['company_name'], age__gte=item['average_age'] + int(age))
                .values(company_name=F('company__name'))
                .annotate(percentage=Count('company_name') * 100 / subquery))
        company_avg_age_data[0].update(average_age=item['average_age'])
        result.extend(company_avg_age_data)
    return result
