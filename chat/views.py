from django.shortcuts import render

# Create your views here.
def peer(request, room_name):
    # get numb turn info
    # context = get_turn_info()
    context = {'room_name': room_name}
    # print(dir(get_turn_info))
    return render(request, 'chat/chat.html', context=context)