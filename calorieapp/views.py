from django.shortcuts import render, redirect
from .models import FoodItem
from django.utils import timezone
# Create your views here.
def home(request): 
    food_items = FoodItem.objects.filter(entry_date__date=timezone.now().date())
    total_calories = sum(item.calories for item in food_items)
    context = {'food_items': food_items, 'total_calories': total_calories}
    return render(request, 'home.html', context)

def add_food_item(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        calories = request.POST.get('calories')
        if name and calories:
         FoodItem.objects.create(name=name, calories=int(calories))
        return redirect('home')
 
def reset_calorie_count( request):
    FoodItem.objects.filter(entry_date__date=timezone.now().date()).delete()
    return redirect('home')  

def delete_food_item(request, pk):
    FoodItem.objects.filter(pk=pk).delete()
    return redirect('home')                                               