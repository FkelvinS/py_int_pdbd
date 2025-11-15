from rich.console import Console

console = Console()


def iniciar_jogador():
    """
    Cria e retorna o estado inicial do jogador.
    Representado por um dicionário simples.
    """
    return {
        "linha": 1,
        "coluna": 1,
        "pontos": 0,
        "venceu": False
    }


def pode_mover_para(labirinto, nova_linha, nova_coluna):
    """
    Verifica se o jogador pode se mover para a posição desejada.
    Não pode atravessar paredes (#).
    """
    if labirinto[nova_linha][nova_coluna] == "#":
        return False
    return True


def mover(jogador, labirinto, direcao):
    """
    Move o jogador na direção escolhida, se possível.
    Direções:
        w = cima
        s = baixo
        a = esquerda
        d = direita
    """

    linha_atual = jogador["linha"]
    coluna_atual = jogador["coluna"]

    if direcao == "w":
        nova_linha = linha_atual - 1
        nova_coluna = coluna_atual
    elif direcao == "s":
        nova_linha = linha_atual + 1
        nova_coluna = coluna_atual
    elif direcao == "a":
        nova_linha = linha_atual
        nova_coluna = coluna_atual - 1
    elif direcao == "d":
        nova_linha = linha_atual
        nova_coluna = coluna_atual + 1
    else:
        console.print("[red]Direção inválida![/]")
        return False

    if not pode_mover_para(labirinto, nova_linha, nova_coluna):
        console.print("[yellow]Você bateu em uma parede![/]")
        return False

    # Verifica se chegou na saída S
    if labirinto[nova_linha][nova_coluna] == "S":
        jogador["venceu"] = True

    # Remove o P da posição anterior
    labirinto[linha_atual][coluna_atual] = " "

    # Atualiza posição
    jogador["linha"] = nova_linha
    jogador["coluna"] = nova_coluna

    # Coloca P na nova posição somente se ainda não venceu
    if not jogador["venceu"]:
        labirinto[nova_linha][nova_coluna] = "P"

    return True


def pontuar(jogador, quantidade=1):
    """
    Aumenta pontos do jogador.
    """
    jogador["pontos"] += quantidade


if __name__ == "__main__":
    from aventura_pkg.labirinto import criar_labirinto, imprimir_labirinto

    lab = criar_labirinto()
    jogador = iniciar_jogador()

    imprimir_labirinto(lab)

    while True:
        direcao = input("Movimento (w/a/s/d): ").lower()

        mover(jogador, lab, direcao)
        imprimir_labirinto(lab)

        if jogador["venceu"]:
            console.print("[green]Você chegou à saída![/]")
            break

