from django.shortcuts import render, redirect
import string
import random
import uuid 
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def peer(request, room_name):
    # get numb turn info
    # context = get_turn_info()
    context = {'room_name': room_name}
    # print(dir(get_turn_info))
    return render(request, 'chat/chat.html', context=context)


@login_required(login_url='login')
def live_class(request):
    room_name = generate_room_name()
    return redirect('peer', room_name)

def generate_room_name():
    S = 10 
    ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = S))    
    return ran