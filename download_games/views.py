from django.shortcuts import render, redirect, get_object_or_404
from . import models, forms
from django.views import generic


#create games
class CreateGameView(generic.CreateView):
    template_name = 'crud/create_game.html'
    form_class = forms.GamesForm
    model = models.Games
    success_url = '/games_list/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateGameView, self).form_valid(form=form)


# def create_game_view(request):
#     if request.method == 'POST':
#         form = forms.GamesForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('/games_list/')
#     else:
#         form = forms.GamesForm()
    
#     context = {
#         'form': form
#     }
#     return render(request, template_name='crud/create_game.html', context=context)


#read
def games_list_view(request):
    if request.method == 'GET':
        game = models.Games.objects.all().order_by('-id')
        context = {
            'game': game
        }
    return render(request, template_name='crud/games_list.html', context=context)


#Update
class UpdateGamesView(generic.UpdateView):
    template_name = 'crud/update_game.html'
    form_class = forms.GamesForm
    success_url = '/games_list/'
    model = models.Games

    def get_object(self, **kwargs):
        game_id = self.kwargs.get('id')
        return get_object_or_404(self.model, id=game_id)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(UpdateGamesView, self).form_valid(form=form)
    





# def update_games_view(request, id):
#     game_id = get_object_or_404(models.Games, id=id)
#     if request.method == 'POST':
#         form = forms.GamesForm(request.POST, instance=game_id)
#         if form.is_valid():
#             form.save()
#             return redirect('/games_list/')
#     else:
#         form = forms.GamesForm(instance=game_id)
#     context = {
#         'form': form,
#         'game_id': game_id
#     }
#     return render(request, template_name='crud/update_game.html', context=context)



#delete
class DeleteGameView(generic.DeleteView):
    template_name = 'crud/confirm_delete.html'
    success_url = '/games_list/'
    context_object_name = 'game_id'
    model = models.Games

    def get_object(self, **kwargs):
        game_id = self.kwargs.get('id')
        return get_object_or_404(self.model, id=game_id)




# def delete_game_view(request, id):
#     game_id = get_object_or_404(models.Games, id=id)
#     game_id.delete()
#     return redirect('/games_list/')