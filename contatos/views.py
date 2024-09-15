from django.shortcuts import render,get_object_or_404,redirect
from .models import Contato
from .forms import ContatoForm
from django.contrib.auth.decorators import login_required

@login_required
def adicionar_contato(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            contato = form.save(commit=False)
            contato.user = request.user
            contato.save()
            return redirect('listar_contato')
    else:
        form = ContatoForm()
    return render (request,'contatos/adicionar.html',{'form':form})

@login_required
def listar_contato(request):
    contatos = Contato.objects.filter(user=request.user)
    context = {'contatos':contatos}
    return render (request,'contatos/listar.html',context)

@login_required
def excluir_contato(request,id):
    contato = get_object_or_404(Contato,id=id,user=request.user)
    if request.method == 'POST':
        contato.delete()
        return redirect('listar_contato')
    return render(request,'contatos/excluir.html',{'contato':contato})

@login_required
def editar_contato(request,id):
    contato = get_object_or_404(Contato,id=id,user =request.user)
    if request.method == 'POST':
        form = ContatoForm(request.POST,instance=contato)
        if form.is_valid():
            form.save()
            return redirect ('listar_contato')
    else: 
        form = ContatoForm(instance=contato)
    return render (request,'contatos/editar.html',{'form':form})