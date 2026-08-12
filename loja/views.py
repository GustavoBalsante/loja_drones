from django.shortcuts import render, redirect, get_object_or_404
from .models import Drone, Pedido  # Importamos o Pedido aqui

# (Mantenha as funções index, detalhe_drone, adicionar_carrinho, ver_carrinho, remover_carrinho...)

def checkout(request):
    carrinho = request.session.get('carrinho', {})
    if not carrinho:
        return redirect('index')  # Se o carrinho estiver vazio, volta para a home

    total = 0
    for drone_id, quantidade in carrinho.items():
        drone = get_object_or_404(Drone, id=drone_id)
        total += drone.preco * quantidade

    if request.method == 'POST':
        # Salva o pedido com as informações enviadas pelo formulário
        pedido = Pedido.objects.create(
            nome=request.POST.get('nome'),
            email=request.POST.get('email'),
            endereco=request.POST.get('endereco'),
            cidade=request.POST.get('cidade'),
            total=total
        )
        # Limpa o carrinho após fechar o pedido
        request.session['carrinho'] = {}
        return render(request, 'loja/sucesso.html', {'pedido': pedido})

    return render(request, 'loja/checkout.html', {'total': total})

def index(request):
    drones = Drone.objects.all()
    return render(request, 'loja/index.html', {'drones': drones})


def detalhe_drone(request, drone_id):
    drone = get_object_or_404(Drone, id=drone_id)
    return render(request, 'loja/detalhe.html', {'drone': drone})


# --- FUNÇÕES DO CARRINHO ---

def adicionar_carrinho(request, drone_id):
    carrinho = request.session.get('carrinho', {})
    drone_id_str = str(drone_id)

    # Soma +1 na quantidade do drone escolhido
    carrinho[drone_id_str] = carrinho.get(drone_id_str, 0) + 1
    request.session['carrinho'] = carrinho
    return redirect('ver_carrinho')


def ver_carrinho(request):
    carrinho = request.session.get('carrinho', {})
    itens = []
    total = 0

    for drone_id, quantidade in carrinho.items():
        drone = get_object_or_404(Drone, id=drone_id)
        subtotal = drone.preco * quantidade
        total += subtotal
        itens.append({'drone': drone, 'quantidade': quantidade, 'subtotal': subtotal})

    return render(request, 'loja/carrinho.html', {'itens': itens, 'total': total})


def remover_carrinho(request, drone_id):
    carrinho = request.session.get('carrinho', {})
    drone_id_str = str(drone_id)

    if drone_id_str in carrinho:
        del carrinho[drone_id_str]
        request.session['carrinho'] = carrinho

    return redirect('ver_carrinho')