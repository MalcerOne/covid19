# Site de estatísticas de COVID-19 usando APIs

Site com estatísticas atualizadas de infecção, tratamento e vacinação de COVID-19 mundialmente, feito para o Projeto 2 de Tecnologias Web.

Back-end feito com Django REST Framework.

APIs utilizadas:
- VACCOVID: https://rapidapi.com/vaccovidlive-vaccovidlive-default/api/vaccovid-coronavirus-vaccine-and-treatment-tracker
- Country Flags: https://www.countryflags.io/
- Data on COVID-19 (coronavirus) vaccinations by Our World in Data: https://github.com/owid/covid-19-data/tree/master/public/data/vaccinations

## Se quiser rodar sua própria versão localmente ##

- Pelo cmd, entre em covid19/env/Scripts e execute o arquivo activate.bat
- No arquivo views.py (covid19/stats/views.py):
- Na primeira vez que for rodar o arquivo, deixe a função initialpopulate() — linha 128 — descomentada e a função update() — linha 129 — comentada.
- Após rodar pela primeira vez, inverta as funções comentadas e descomentadas.
- Após ativar o ambiente virtual e checar se a função correta está descomentada, volte para a raíz do projeto, e, no cmd. digite ```python manage.py runserver```
