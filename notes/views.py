from django.shortcuts import render, redirect
from .models import Note


def index(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        # TAREFA: Utilize o title e content para criar um novo Note no banco de dados

        if not title or not content:
            return redirect('index')
        
        note = Note(title=title, content=content)
        note.save()
        return redirect('index')

    else:
        all_notes = Note.objects.all()
        return render(request, 'notes/index.html', {'notes': all_notes})

def delete(request):
    if request.method == 'POST':
        id = request.POST.get('id-delete')

        Note.objects.filter(id=id).delete()
        return redirect('index')

    else:
        all_notes = Note.objects.all()
        return render(request, 'notes/index.html', {'notes': all_notes})

def update(request):
    if request.method == 'POST':
        id = request.POST.get('id-update')
        title = request.POST.get('title')
        content = request.POST.get('content')

        Note.objects.filter(id=id).update(title=title, content=content)
        return redirect('index')

    else:
        all_notes = Note.objects.all()
        return render(request, 'notes/index.html', {'notes': all_notes})