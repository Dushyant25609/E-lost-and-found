from django.shortcuts import render, redirect
from student.forms import FoundItemForm

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
    # Query items that are not found
    not_found_items = Lost_Item.objects.filter(status='not_recieved')  # Assuming 'not_submitted' means not found
    return render(request, 'organization_not_found_items.html', {'not_found_items': not_found_items})