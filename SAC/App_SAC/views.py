from django.shortcuts import render, get_object_or_404, redirect
from .models import Cliente, Atendente
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, InvalidPage, EmptyPage

# Create your views here.
def abre_index(request):
    return render(request, 'index.html')


@login_required
def cad_cliente(request):
    return render(request, 'Cad_Cliente.html')

@login_required
def salvar_cliente_novo(request):
    if (request.method == 'POST'):
        nome = request.POST.get('nome')
        telefone = request.POST.get('telefone')
        email = request.POST.get('email')
        observacao = request.POST.get('observacao')
        grava_cliente = Cliente(
            nome=nome,
            telefone=telefone,
            email=email,
            observacao=observacao
        )
        grava_cliente.save()
        messages.info(request, 'Cliente ' + nome + ' cadastrado com sucesso')
        return render(request, 'Cad_Cliente.html')


@login_required
def cons_cliente(request):
    dado_pesquisa_nome = request.POST.get('cliente')
    teste = request.GET.get('name')
    paget = request.GET.get('page')
    if teste != None:
        clientes = Cliente.objects.filter(nome__icontains=teste)
        paginator = Paginator(clientes, 1)
        try:
            cliente = paginator.page(paget)
        except (EmptyPage, InvalidPage):
            cliente = paginator.page(paginator.num_pages)
        return render(request, 'Cons_Cliente_Lista.html', {'dados_clientes': cliente, 'nome': teste})


    if dado_pesquisa_nome != None and dado_pesquisa_nome != '':
        clientes = Cliente.objects.filter(nome__icontains=dado_pesquisa_nome)
        paginator = Paginator(clientes, 1)
        try:
            page = int(request.GET.get('page', '1'))
        except ValueError:
            page = 1
        try:
            cliente = paginator.page(page)
        except (EmptyPage, InvalidPage):
            cliente = paginator.page(paginator.num_pages)
        return render(request, 'Cons_Cliente_Lista.html', {'dados_clientes': cliente, 'nome': dado_pesquisa_nome})
    else:
        return render(request, 'Cons_Cliente_Lista.html')




@login_required
def salvar_cliente_editado(request):
    if (request.method == 'POST'):
        id_cliente = request.POST.get('id_cliente')
        nome = request.POST.get('nome')
        telefone = request.POST.get('telefone')
        email = request.POST.get('email')
        observacao = request.POST.get('observacao')

        Cliente_Editado = Cliente.objects.get(id=id_cliente)

        Cliente_Editado.nome = nome
        Cliente_Editado.telefone = telefone
        Cliente_Editado.email = email
        Cliente_Editado.observacao = observacao

        Cliente_Editado.save()

        messages.info(request, 'Cliente ' + nome + ' editado com sucesso.')
        return render(request, 'Cons_Cliente_Lista.html')



@login_required
def edit_cliente(request, id):
    dados_editar = get_object_or_404(Cliente, pk=id)
    return render(request, 'Edit_Cliente.html', {'dados_do_cliente': dados_editar})

@login_required
def delete_cliente(request, id):
    cliente_deletado = get_object_or_404(Cliente, pk=id)
    nome = cliente_deletado.nome
    cliente_deletado.delete()

    messages.info(request, 'Cliente ' + nome + ' excluido com sucesso.')
    return redirect('cons_cliente')
#   render(request, 'Cons_Cliente_Lista.html')

@login_required
def cad_atend(request):
    cons_users = User.objects.all()
    usuario_logado = request.user.username
    return render(request, 'Cad_Atendente.html', {'usuario_logado': usuario_logado})

def salvar_atend_novo(request):
    usuario_logado = request.user.username
    if(request.method == 'POST'):
        nome_atend = request.POST.get('nome_atend')
        telefone_atend = request.POST.get('telefone_atend')
        user_atend = request.POST.get('user_atend')
        observacao_atend = request.POST.get('observacao_atend')
        if user_atend:
            user_atend = User.objects.get(username=user_atend)
        else:
            user_atend = None

        grava_atend = Atendente(
            nome_atend=nome_atend,
            telefone_atend=telefone_atend,
            observacao_atend=observacao_atend,
            ativo_atend=1,
            user_atend=user_atend
        )
        grava_atend.save()
        messages.info(request, 'Atendente ' + nome_atend + ' cadastrado com sucesso')
        cons_users = User.objects.all()
        return render(request, 'Cad_Atendente.html', {'usuario_logado': usuario_logado, 'cons_users': cons_users})


@login_required
def cons_atendente(request):
    usuario_logado = request.user.username
    dado_pesquisa_nome = request.POST.get('atendente')
    atendentes = Atendente.objects.filter(nome_atend__icontains=dado_pesquisa_nome)
    print(atendentes)
    print(dado_pesquisa_nome)
    return render(request, 'Cons_Atendente.html', {'usuario_logado': usuario_logado, 'atendentes': atendentes})

