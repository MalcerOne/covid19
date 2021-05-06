from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
import requests
from .models import Country
from .serializers import CountrySerializer

def getcountryinfo(country):
    url="https://vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com/api/npm-covid-data/countries-name-ordered"
    headers = {'x-rapidapi-key': "be83437380msh3697003aab41f1ap1d95ffjsnad2327d68470",'x-rapidapi-host': "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com"}
    response = requests.request("GET", url, headers=headers)
    for dictionary in response.text:
        if country.capitalize() == dictionary['Country']:
            return dictionary['ThreeLetterSymbol']

def getstats(country=None):
    fullstatsurl="https://vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com/api/npm-covid-data/"
    if not country:
        headers = {'x-rapidapi-key': "be83437380msh3697003aab41f1ap1d95ffjsnad2327d68470",'x-rapidapi-host': "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com"}
        response = requests.request("GET", fullstatsurl, headers=headers)
        return response.text
    else:
        url=f"https://vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com/api/npm-covid-data/country-report-iso-based/{country.capitalize()}/{getcountryinfo(country)}"

def index(request):
    if request.method == 'POST':
        try:
            return render(request, 'stats/index.html')
        except:
            raise Http404
        
@api_view(['GET', 'POST'])
def api_country(request, country_id):
    try:
        country = Country.objects.get(id=country_id)
    except Country.DoesNotExist:
        raise Http404()
    serialized_country = CountrySerializer(country)
    return Response(serialized_country.data)