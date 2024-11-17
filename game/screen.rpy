# Tela para navegar entre salas
screen navegar_salas():
    # Mostra a imagem da sala atual
    add current_room

    # Botão para navegar para a esquerda
    imagebutton:
        idle "botaoEsquerda.png"
        hover "botaoEsquerda.png"
        action Function(mudar_sala, "esquerda")
        xpos 50
        ypos 530

    # Botão para navegar para a direita
    imagebutton:
        idle "botaoDireita.png"
        hover "botaoDireita.png"
        action Function(mudar_sala, "direita")
        xpos 1700
        ypos 530
    
