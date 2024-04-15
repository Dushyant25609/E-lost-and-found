from django.shortcuts import render, redirect
from .models import Lost_Item, Found_Item
from .forms import FoundItemForm, LostItemForm
from .similar import query
from .score import score_calculator
from django.urls import reverse
from static.images.image import img_query_lost,img_query_found
from static.images.api import prompt,clean_query


def home(request):
    context = {}
    return render(request, 'index.html', context)

def max_index_2(points):
    if len(points) <= 3:
        max_num = max(points)
        return [points.index(max_num)]
    else:
        num_index = []
        for _ in range(3):
            max_num = max(points)
            index = points.index(max_num)
            num_index.append(index)
            points[index] = float('-inf')# Set the found max to negative infinity to avoid re-selecting it
        return num_index


    


def max_index(points):
    max_num = 0
    index = 0 
    for i in range(len(points)):
        if points[i] > max_num:
            max_num = points[i]
            index = i
    return index

def lost(request):
    match_name = match_des = match_loc = match_date = match_item = ""

    if request.method == 'POST':
        lost_form = LostItemForm(request.POST, request.FILES)
        if lost_form.is_valid():
            
            lost_item = lost_form.save(commit=False)
            lost_item.status = 'not_received'
            lost_item.save()
            all_items_l = Lost_Item.objects.all()
            all_item_ids_l = [item.id for item in all_items_l]
            all_item_name_l = [item.name for item in all_items_l]
            all_item_img_l = [item.image for item in all_items_l]
            print("name: ",all_item_name_l[-1])
            print("ids: ",all_item_ids_l[-1])
            print("Img: ",all_item_img_l[-1])
            img_des = img_query_lost(all_item_img_l[-1])
            prompt_text = prompt(img_des[0]['generated_text'])
            payload = {"inputs": prompt_text}
            generated_text = clean_query(payload)

            question_index = generated_text.find(img_des[0]['generated_text'])
            if question_index != -1:
                answer = generated_text[question_index + len(img_des[0]['generated_text']):].strip()
            else:
                answer = generated_text
            print("img description: ",img_des)
            print("Clean query: ",answer)
            lost_items_img = Lost_Item.objects.get(id=all_item_ids_l[-1])
            lost_items_img.image_description = answer
            lost_items_img.save()
            return redirect('dashboard')
        else:
            print(lost_form.errors)
    else:
        lost_form = LostItemForm()

    context = {
    }
    return render(request, 'lost.html', context)

def foundform(request):
    if request.method == 'POST':
        found_form = FoundItemForm(request.POST, request.FILES)
        if found_form.is_valid():
            found_item = found_form.save(commit=False)
            found_item.status = 'not_received'
            found_item.save()
            all_items = Found_Item.objects.all()
            all_item_ids = [item.id for item in all_items]
            all_item_img = [item.image for item in all_items]
            img_des = img_query_found(all_item_img[-1])
            prompt_text = prompt(img_des[0]['generated_text'])
            payload = {"inputs": prompt_text}
            generated_text = clean_query(payload)

            question_index = generated_text.find(img_des[0]['generated_text'])
            if question_index != -1:
                answer = generated_text[question_index + len(img_des[0]['generated_text']):].strip()
            else:
                answer = generated_text
            print("img description: ",img_des)
            print("Clean query: ",answer)
            found_items_img = Found_Item.objects.get(id=all_item_ids[-1])
            found_items_img.image_description = answer
            found_items_img.save()
            return redirect('home')
        else:
            print(found_form.errors)
    else:
        found_form = FoundItemForm()
    
    context = {'found_form': found_form}
    return render(request, 'found.html', context)

def about(request):
    return render(request, 'aboutUs.html')

def contact(request):
    return render(request, 'contactUs.html')


def student_dashboard(request):
    matched_items = []
    all_items = Found_Item.objects.all()
    all_item_ids = [item.id for item in all_items]
    all_item_name = [item.item_name for item in all_items]
    all_item_des = [item.item_description for item in all_items]
    all_loc = [item.location for item in all_items]
    all_img_des = [item.image_description for item in all_items]

    all_items_l = Lost_Item.objects.all()
    all_item_ids_l = [item.id for item in all_items_l]
    all_item_name_l = [item.name for item in all_items_l]
    all_item_des_l = [item.item_description for item in all_items_l]
    all_item_loc_l = [item.location for item in all_items_l]
    all_item_img_des_l = [item.image_description for item in all_items_l]

    item_name = all_item_name_l[-1]
    item_des = all_item_des_l[-1]
    loc = all_item_loc_l[-1]
    image_des = all_item_img_des_l[-1]

    print("Lost last: ",item_name)

    print("found items: ",all_item_name[0])
    print("found item id: ",all_item_ids[0])
    print("found item name: ",all_item_des[0])

    name_out = query({"inputs": {"source_sentence": item_name, "sentences": all_item_name}})
    des_out = query({"inputs": {"source_sentence": item_des, "sentences": all_item_des}})
    loc_out = query({"inputs": {"source_sentence": loc, "sentences": all_loc}})
    img_out = query({"inputs": {"source_sentence": image_des, "sentences": all_img_des}})

    print("img_out: ",img_out)

    print("name_out:",name_out)
    print("des_out:",des_out)
    print("loc_out:",loc_out)

    points = []
    for i in range(len(name_out)):
        points.append(score_calculator(name_out[i], des_out[i], loc_out[i], img_out[i])) 

    match_id_2 = max_index_2(points)

    match_index = []
    for i in match_id_2:
        match_index.append(all_item_ids[i])
    
    for i in match_index:
        try:
            item = Found_Item.objects.get(id=i)
            matched_items.append(item)
        except Found_Item.DoesNotExist:
            print(f"Item with ID {i} does not exist.")
        
    print("Matched_items: ", matched_items)
    
    context = {
        'matched_items': matched_items
    }

    return render(request, 'dashboard.html', context)



def slogged_in(request):
    return render(request, 'slogged.html')