#language: pt
@bug
Funcionalidade: Testar pesquisar google

    @event
    Cenario: Testar o campo de pesquisa google
        Dado entro no google
        Quando pesquiso "receitas de bolo"
        E abro o Firefox
        E coloco meu login
        E aguardo um minuto
        # E entro no gmail
        # Quando digito no campo pesquisar "<browser>"
        # E clico no botao pesquisar "analise_conta"
        # Entao vou para o url definido
