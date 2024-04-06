from django.shortcuts import render, redirect
from student.forms import FoundItemForm
from django.shortcuts import get_object_or_404, redirect

# Create your views here.


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


# organization/views.py


from student.models import Found_Item, Lost_Item

def not_received_items(request):
    # Query items that are not yet received by their owners
    not_received_items = Found_Item.objects.filter(status='not_submitted')
    return render(request, 'organization_not_received_items.html', {'not_received_items': not_received_items})

def not_found_items(request):
    query = request.GET.get('query')
    if query:
        not_found_items = Lost_Item.objects.filter(item_name__icontains=query) | Lost_Item.objects.filter(item_description__icontains=query)
    else:
        not_found_items = Lost_Item.objects.all()
    return render(request, 'organization_not_found_items.html', {'not_found_items': not_found_items, 'query': query})


def toggle_status(request, lost_item_id):
    lost_item = get_object_or_404(Lost_Item, pk=lost_item_id)
    if request.method == 'POST':
        new_status = request.POST.get('new_status')
        lost_item.status = new_status
        lost_item.save()
    return redirect('not_found_items')



def search_items(request):
    query = request.GET.get('query')
    if query:
        # Perform a case-insensitive search on item_name and item_description fields
        found_items = Lost_Item.objects.filter(item_name__icontains=query) | Lost_Item.objects.filter(item_description__icontains=query)
    else:
        found_items = Lost_Item.objects.all()  # Show all items if no query provided
    return render(request, 'organization_not_found_items.html', {'found_items': found_items})
