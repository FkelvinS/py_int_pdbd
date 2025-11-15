from rich.console import Console
import random

console = Console()

def criar_labirinto(linhas=10, colunas=20):
    """
    Cria um labirinto com bordas fixas e obstáculos internos.
    """
    labirinto = []

    for i in range(linhas):
        linha = []
        for j in range(colunas):
            # Bordas fixas como paredes
            if i == 0 or i == linhas - 1 or j == 0 or j == colunas - 1:
                linha.append("#")
            else:
                # 15% de chance de virar parede interna
                if random.random() < 0.15:
                    linha.append("#")
                else:
                    linha.append(" ")
        labirinto.append(linha)

    # Definir início e saída
    labirinto[1][1] = "P"  # início do jogador
    labirinto[linhas - 2][colunas - 2] = "S"  # saída

    return labirinto


def imprimir_labirinto(labirinto):
    """
    Mostra o labirinto no terminal com cores usando Rich.
    """
    for linha in labirinto:
        texto_formatado = ""
        for celula in linha:
            if celula == "#":
                texto_formatado += "[bold blue]#[/]"  # parede
            elif celula == "P":
                texto_formatado += "[bold green]P[/]"  # jogador
            elif celula == "S":
                texto_formatado += "[bold red]S[/]"  # saída
            else:
                texto_formatado += " "
        console.print(texto_formatado)


# Teste rápido
if __name__ == "__main__":
    lab = criar_labirinto()
    imprimir_labirinto(lab)



