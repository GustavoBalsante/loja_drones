def carrinho_counter(request):
    carrinho = request.session.get('carrinho', {})
    total_itens = sum(carrinho.values())
    return {'carrinho_qtd': total_itens}