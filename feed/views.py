from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CreatePostForm

# Create your views here.

@login_required()
def postCreateView(request):
    if request.method == 'POST':
        form = CreatePostForm(data=request.POST)
        if form.is_valid():
            gt = form.cleaned_data
            newComponent = form.save(commit=False)
            newComponent.user = request.user
            newComponent.save()
            messages.success(request,' Pomyślnie dodano obraz.')
            return redirect(newComponent.get_absolute_url())
        else:
            form = CreatePostForm(data=request.GET)
        return render(request, '')
