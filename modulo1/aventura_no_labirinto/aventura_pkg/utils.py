import os
import time
from rich.console import Console

console = Console()


def limpar_tela():
    """
    Limpa a tela do terminal.
    Funciona tanto no Windows quanto no Linux.
    """
    os.system("cls" if os.name == "nt" else "clear")


def pausar(segundos=1):
    """
    Pausa a execução por alguns segundos.
    """
    time.sleep(segundos)


def mostrar_menu():
    """
    Exibe o menu principal do jogo.
    Retorna a escolha feita pelo usuário.
    """
    console.print("[bold cyan]\n=== MENU PRINCIPAL ===[/]")
    console.print("[green]1.[/] Jogar")
    console.print("[yellow]2.[/] Ver instruções")
    console.print("[red]3.[/] Sair")

    escolha = console.input("\nEscolha uma opção: ")

    # processando escolha com match-case como exigido no trabalho
    match escolha:
        case "1":
            return 1
        case "2":
            return 2
        case "3":
            return 3
        case _:
            console.print("[red]Opção inválida![/]")
            return 0


def mostrar_instrucoes():
    """
    Exibe as regras do jogo.
    """
    console.print("\n[bold yellow]INSTRUÇÕES[/]")
    console.print("- Use W A S D para mover o jogador.")
    console.print("- Evite paredes (#).")
    console.print("- Alcance o objetivo (S).")
    console.print("- Feito por Fernando para o trabalho do curso PDBD.\n")


def mensagem_vitoria():
    """
    Mensagem de vitória.
    """
    console.print("[bold green]\n🎉 Você alcançou a saída! Parabéns!\n[/]")


def mensagem_derrota():
    """
    Mensagem caso futuramente exista derrota.
    """
    console.print("[bold red]\n☠ Você perdeu![/]")


def pedir_nome():
    """
    Pede o nome do jogador e retorna.
    """
    nome = console.input("[cyan]Digite seu nome: [/]")
    return nome

if __name__ == "__main__":
    limpar_tela()
    escolha = mostrar_menu()
    print("Você escolheu:", escolha)
    pausar(1)
    mostrar_instrucoes()
