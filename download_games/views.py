from django.shortcuts import render, redirect, get_object_or_404
from . import models, forms


#create games
def create_game_view(request):
    if request.method == 'POST':
        form = forms.GamesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/games_list/')
    else:
        form = forms.GamesForm()
    
    context = {
        'form': form
    }
    return render(request, template_name='crud/create_game.html', context=context)


#read
def games_list_view(request):
    if request.method == 'GET':
        game = models.Games.objects.all().order_by('-id')
        context = {
            'game': game
        }
    return render(request, template_name='crud/games_list.html', context=context)


#Update
def update_games_view(request, id):
    game_id = get_object_or_404(models.Games, id=id)
    if request.method == 'POST':
        form = forms.GamesForm(request.POST, instance=game_id)
        if form.is_valid():
            form.save()
            return redirect('/games_list/')
    else:
        form = forms.GamesForm(instance=game_id)
    context = {
        'form': form,
        'game_id': game_id
    }
    return render(request, template_name='crud/update_game.html', context=context)



#delete
def delete_game_view(request, id):
    game_id = get_object_or_404(models.Games, id=id)
    game_id.delete()
    return redirect('/games_list/')