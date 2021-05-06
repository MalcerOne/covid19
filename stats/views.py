from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
import requests
from .models import Country
from .serializers import CountrySerializer

def getcountryinfo(country):
    url='https://vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com/api/npm-covid-data/countries-name-ordered'
    headers = {'x-rapidapi-key': 'be83437380msh3697003aab41f1ap1d95ffjsnad2327d68470','x-rapidapi-host': 'vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com'}
    response = requests.request('GET', url, headers=headers)
    for dictionary in response.text:
        if country.capitalize() == dictionary['Country']:
            return dictionary['ThreeLetterSymbol']

def getstats(country=None):
    fullstatsurl='https://vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com/api/npm-covid-data/'
    vacurl='https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/vaccinations.json'
    headers = {'x-rapidapi-key': 'be83437380msh3697003aab41f1ap1d95ffjsnad2327d68470','x-rapidapi-host': 'vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com'}
    if not country:
        response1 = (requests.request('GET', fullstatsurl, headers=headers)).text
        response2 = (requests.request('GET', vacurl)).text
        return (response1, response2)
    else:
        url=f'https://vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com/api/npm-covid-data/country-report-iso-based/{country.capitalize()}/{getcountryinfo(country)}'
        response1 = (requests.request('GET', url, headers=headers)).text
        response2 = requests.request('GET', vacurl).json()
        for d in response2:
            if d['country'] == country:
                response2 = d['data'][-1]
        return (response1, response2)

def getflag(country, style='flat', size='16'):
    sizes=['16','24','32','48','64']
    styles=['flat','shiny']
    codes={}
    if (size not in sizes) or (style not in styles):
        raise ValueError('Argumento inválido.')
    country_code=codes[country]
    url=f'https://www.countryflags.io/{country_code}/{style}/{size}.png'
    return url

def index(request):
    if request.method == 'GET':
        try:
            countries=Country.objects.all()
            return render(request, 'stats/index.html', {'countries': countries})
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