from django.shortcuts import render, redirect, get_object_or_404
from webapp.models import Stufs
from django.http import HttpResponseRedirect
from webapp.forms import StufsForm

def index_views(request):
    stufs = Stufs.objects.order_by('stuf')
    context = {
        'stufs': stufs
    }
    return render(request, "index.html",  context)

def stufs_view(request, pk):
    stufs = Stufs.objects.get(pk=pk)
    context = {'stufs': stufs}
    return render(request, 'stufs_view.html', context)

def stuf_create(request):
    if request.method == "GET":
        form = StufsForm()
        return render(request, "stufs_create.html", {'form': form})
    if request.method == "POST":
        form = StufsForm(data=request.POST)
        if form.is_valid():
            form = Stufs.objects.create(
                stuf=form.cleaned_data['stuf'],
                description=form.cleaned_data['description'],
                categories=form.cleaned_data['categories'],
                remainder=form.cleaned_data['remainder'],
                price=form.cleaned_data['price']
            )
            return redirect('index')
        else:
            return render(request, "stufs_create.html", {'form': form})

def stuf_update_view(request, pk):
    stuf = get_object_or_404(Stufs, pk=pk)
    if request.method == 'GET':
        form = StufsForm(initial={
            'stuf': stuf.stuf,
            'description': stuf.description,
            'categories': stuf.categories,
            'remainder': stuf.remainder,
            'price': stuf.price
        })
        return render(request, "update.html", {'form': form})
    elif request.method == 'POST':
        form = StufsForm(data=request.POST)
        if form.is_valid():
            stuf.stuf = form.cleaned_data.get('stuf')
            stuf.description = form.cleaned_data.get('description')
            stuf.categories = form.cleaned_data.get('categories')
            stuf.remainder = form.cleaned_data.get('remainder')
            stuf.price = form.cleaned_data.get('price')
            stuf.save()
            return redirect('index')
        else:
            return render(request, "update.html", {'form': form})


def stuf_delete_view(request, pk):
    stuf = get_object_or_404(Stufs, pk=pk)
    if request.method == 'GET':
        return render(request, 'delete.html', context={'stuf': stuf})
    elif request.method == 'POST':
        stuf.delete()
        return redirect('index')