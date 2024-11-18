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
        xpos 1620
        ypos 530
    
    if current_room == "sala3":
        imagebutton:
            idle "BotaoPorta.png"
            hover "BotaoPorta.png"
            action Jump("corredor")
            xpos 450
            ypos 300

    
    
screen corredor():
    # Mostra a imagem do corredor
    add "corredor"

    imagebutton:
        idle "botaoInferior.png"
        hover "botaoInferior.png"
        action Jump("sala3")
        xpos 50
        ypos 1000
        focus_mask True

    
    imagebutton:
        idle "BotaoPorta.png"  # Imagem normal do botão
        hover "BotaoPorta.png"  # Imagem ao passar o mouse
        action Jump("quartos_navegacao")  # Vai para a cena da esquerda
        xpos 700
        ypos 400
        focus_mask True  # Define toda a imagem como clicável

 
screen navegar_quartos():
    # Mostra o quarto atual
    add current_quarto

    # Botão para ir à esquerda (quarto anterior)
    imagebutton:
        idle "botaoEsquerda.png"
        hover "botaoEsquerda.png"
        action Function(mudar_quarto, "esquerda")
        xpos 50
        ypos 500

    # Botão para ir à direita (próximo quarto)
    imagebutton:
        idle "botaoDireita.png"
        hover "botaoDireita.png"
        action Function(mudar_quarto, "direita")
        xpos 1600
        ypos 500

    if current_quarto == "quarto1":
        imagebutton:
            idle "BotaoPorta.png"
            hover "BotaoPorta.png"
            action Jump("play_video")
            xpos 720
            ypos 190

    if current_quarto == "quarto3":
        imagebutton:
            idle "BotaoPorta.png"
            hover "BotaoPorta.png"
            action Jump("corredor")
            xpos 450
            ypos 300


# Tela para navegar entre as salas da cozinha
screen navegar_cozinha():
    # Mostra a imagem da sala atual
    add current_cozinha


    # Botão para ir à sala anterior (esquerda)
    imagebutton:
        idle "botaoEsquerda.png"
        hover "botaoEsquerda.png"
        action Function(mudar_cozinha, "esquerda")
        xpos 50
        ypos 500

    # Botão para ir à próxima sala (direita)
    imagebutton:
        idle "botaoDireita.png"
        hover "botaoDireita.png"
        action Function(mudar_cozinha, "direita")
        xpos 1600
        ypos 500