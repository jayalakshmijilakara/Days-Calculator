
from django.shortcuts import render
from .forms import DateForm
from datetime import datetime

def days_calculator(request):
    days_difference = None
    if request.method == 'POST':
        form = DateForm(request.POST)
        if form.is_valid():
            date1 = form.cleaned_data['date1']
            date2 = form.cleaned_data['date2']

            
            days_difference = (date2 - date1).days

           
            years = days_difference // 365
            months = (days_difference % 365) // 30
            days = (days_difference % 365) % 30

            if years != 0 and years == 1:
                days_difference = f"{years} year {months} months {days} days"
            elif years == 0 :
                days_difference = f"{months} months {days} days"
            else:
                days_difference = f"{years} years {months} months {days} days"


            
            
    else:
        form = DateForm()

    return render(request, 'calculator/days_calculator.html', {'form': form, 'days_difference': days_difference})
