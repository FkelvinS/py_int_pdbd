import sys
import os
from pynput import keyboard
from rich.console import Console

from aventura_pkg.labirinto import criar_labirinto, imprimir_labirinto
from aventura_pkg.jogador import iniciar_jogador, mover
from aventura_pkg.utils import (
    limpar_tela,
    pausar,
    mostrar_menu,
    mostrar_instrucoes,
    mensagem_vitoria,
    pedir_nome
)

console = Console()

# Variável global para capturar o último comando pressionado
ultima_tecla = None


def ao_pressionar(tecla):
    """
    Função chamada automaticamente quando o usuário pressiona uma tecla.
    Ela guarda a tecla em uma variável global.
    """
    global ultima_tecla
    try:
        ultima_tecla = tecla.char  # teclas como w, a, s, d
    except AttributeError:
        pass  # ignora teclas especiais (shift, ctrl, etc)


def iniciar_jogo(nome_jogador):
    """
    Função principal que roda o loop da aventura.
    """

    # Criar labirinto + jogador
    lab = criar_labirinto()
    jogador = iniciar_jogador()

    # Iniciar listener do teclado
    listener = keyboard.Listener(on_press=ao_pressionar)
    listener.start()

    jogando = True

    while jogando:
        limpar_tela()
        console.print(f"[bold cyan]Jogador: {nome_jogador}[/]")
        imprimir_labirinto(lab)

        # Verificar se chegou na saída
        if lab[jogador["linha"]][jogador["coluna"]] == "S":
            mensagem_vitoria()
            listener.stop()
            return

        # Espera tecla
        pausar(0.15)

        global ultima_tecla
        if ultima_tecla in ["w", "a", "s", "d"]:
            mover(jogador, lab, ultima_tecla)

        ultima_tecla = None


def main():
    """
    Esta função é a primeira a rodar.
    Ela processa argumentos, chama o menu e inicia o jogo.
    """

    # Argumentos da linha de comando
    # Exemplo:
    # python -m aventura_pkg.main Fernando
    if len(sys.argv) > 1:
        nome = sys.argv[1]
    else:
        nome = pedir_nome()

    while True:
        limpar_tela()
        escolha = mostrar_menu()

        if escolha == 1:
            iniciar_jogo(nome)
            pausar(2)

        elif escolha == 2:
            limpar_tela()
            mostrar_instrucoes()
            console.input("\nPressione ENTER para voltar ao menu...")

        elif escolha == 3:
            console.print("[bold red]Saindo do jogo...[/]")
            pausar(1)
            break

        else:
            console.print("[yellow]Tente novamente.[/]")
            pausar(1)


if __name__ == "__main__":
    main()
