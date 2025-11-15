Aventura no Labirinto é um jogo em modo texto desenvolvido em Python. O objetivo do jogador é navegar por um labirinto utilizando as teclas W, A, S e D até encontrar a saída. O projeto foi criado como prática de programação, aplicando modularização, organização de pacotes, interação via terminal e uso da biblioteca Rich para deixar a interface mais clara e formatada.

O projeto está organizado na seguinte estrutura:

aventura_no_labirinto/

aventura_pkg/

init.py

main.py

jogador.py

labirinto.py

utils.py

venv/

README.md

Descrição dos arquivos:
main.py é o arquivo principal que controla o fluxo do jogo, o menu, o loop de execução e a interface.
jogador.py contém toda a lógica de movimentação do jogador, validação dos passos, sistema de pontuação e identificação da chegada à saída.
labirinto.py é responsável por gerar a matriz do labirinto e exibir o mapa no terminal.
utils.py possui funções auxiliares usadas pelo restante do projeto.
init.py indica ao Python que a pasta é um pacote importável.

Para instalar o projeto, é necessário ter Python 3 instalado. No terminal, dentro da pasta do projeto, execute o comando para criar um ambiente virtual:

python -m venv venv

Depois ative o ambiente virtual:

No Windows:
venv\Scripts\activate

No Linux ou macOS:
source venv/bin/activate

Com o ambiente ativado, instale as dependências executando:

pip install -r requirements.txt

Para iniciar o jogo, execute o comando:

python -m aventura_pkg.main SeuNome

Caso o nome não seja informado no comando, o programa solicitará o nome ao iniciar.

Controles do jogo:
W move para cima
S move para baixo
A move para a esquerda
D move para a direita

Elementos do labirinto:
O caractere # representa uma parede.
O caractere P representa a posição inicial do jogador.
O caractere S representa a saída.
O espaço vazio representa um caminho passável.

O funcionamento interno segue esta lógica: o labirinto é gerado como uma matriz de caracteres, o jogador é posicionado automaticamente no ponto inicial, e cada tentativa de movimento é validada pela lógica do módulo jogador.py. Se o movimento for válido, a posição é atualizada e a pontuação aumenta. Quando o jogador alcança a saída, o jogo encerra a partida, mostra a pontuação final e retorna ao menu principal.

A Renderização do labirinto, do status do jogador e das mensagens é feita usando o Rich, para melhorar a visualização em terminal.

As dependências necessárias já estão listadas no arquivo requirements.txt.