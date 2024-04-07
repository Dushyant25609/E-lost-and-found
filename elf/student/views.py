from django.shortcuts import render, redirect
from .models import Lost_Item, Found_Item
from .forms import FoundItemForm, LostItemForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    context = {}
    return render(request, 'home.html', context)

def lost(request):
    if request.method == 'POST':
        lost_form = LostItemForm(request.POST, request.FILES)
        if lost_form.is_valid():
            lost_item = lost_form.save(commit=False)
            lost_item.status = 'not_recieved'
            lost_item.save()
            return redirect('home')  # Redirect to 'home' URL after successful submission
        else:
            print(lost_form.errors)  # Print form errors to console for debugging
    else:
        lost_form = LostItemForm()
    
    context = {'lost_form': lost_form}
    return render(request, 'lost.html', context)

def found(request):
    if request.method == 'POST':
        found_form = FoundItemForm(request.POST, request.FILES)
        if found_form.is_valid():
            found_item = found_form.save(commit=False)
            found_item.status = 'not_recieved'
            found_item.save()
            return redirect('home')  # Redirect to 'home' URL after successful submission
        else:
            print(found_form.errors)  # Print form errors to console for debugging
    else:
        found_form = FoundItemForm()  # Instantiate FoundItemForm
    
    context = {'found_form': found_form}
    return render(request, 'found.html', context)

@login_required
def user_requested_items(request):
    requested_items = Lost_Item.objects.filter(user=request.user)
    return render(request, 'user_requested_items.html', {'requested_items': requested_items})