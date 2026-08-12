def carrinho_counter(request):
    carrinho = request.session.get('carrinho', {})
    # Soma a quantidade total de todos os drones no carrinho
    total_itens = sum(carrinho.values())
    return {'carrinho_qtd': total_itens}