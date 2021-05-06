from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=50)
    rank = models.PositiveSmallIntegerField()
    population = models.PositiveIntegerField()
    
    total_cases = models.PositiveIntegerField()
    new_cases = models.PositiveIntegerField()
    active_cases = models.PositiveIntegerField()
    cases_1m_pop = models.PositiveIntegerField()
    
    total_deaths = models.PositiveIntegerField()
    new_deaths = models.PositiveIntegerField()
    deaths_1m_pop = models.PositiveIntegerField()
    
    total_recovered = models.PositiveIntegerField()
    new_recovered = models.PositiveIntegerField()
    
    infection_risk = models.FloatField()
    case_fatality_rate = models.FloatField()
    recovery_proportion = models.FloatField()
    
    total_vaccinated = models.PositiveIntegerField()
    vaccinated_proportion = models.FloatField()
    vaccinated_1m_pop = models.PositiveIntegerField()
    
    def __str__(self):
        return f'{self.id}. {self.name}'