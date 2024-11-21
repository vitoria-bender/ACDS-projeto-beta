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
    

    if current_room == "sala2":
        imagebutton:
            idle "transparente.png"   
            action Jump("sala2_interacao")
            xpos 450  
            ypos 520  
            ysize 150  

    if current_room == "sala3":
        imagebutton:
            idle "BotaoPorta.png"
            hover "BotaoPorta.png"
            action Jump("corredor")
            xpos 450
            ypos 300

        imagebutton: 
            idle "transparente.png"
            hover"transparente.png"
            action Jump("sala3_interacao")
            xpos 1000
            ypos 250   

    if current_room == "sala4":
        imagebutton:
            idle "transparente.png"   
            action Jump("cozinha_navegacao")
            xpos 450  
            ypos 520  
            xsize 900
            ysize 1000  
    
screen sala2_interacao:
    add "sala2_interacao"

screen sala3_interacao:
    add "sala3_interacao"


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
        idle "BotaoPorta.png"  
        hover "BotaoPorta.png" 
        action Jump("quartos_navegacao") 
        xpos 700
        ypos 400
        focus_mask True

 
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
            idle "transparente.png"
            hover "transparente.png"
            action Jump("play_video")
            xpos 720
            ypos 190
            xsize 500
            ysize 300

    if current_quarto == "quarto3":
        imagebutton:
            idle "transparente.png"
            action Jump("corredor")
            xpos 450
            ypos 300
            xsize 400
            ysize 700


# Tela para navegar entre as salas da cozinha
screen navegar_cozinha():
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

    if current_cozinha == "cozinha1":
        imagebutton:
            idle "transparente.png" 
            action Function(sala_interacao_safe, "guardei aquele último bilhete que foi deixado")
            xpos 300  
            ypos 400
            xsize 200  
            ysize 400 



    if current_cozinha == "cozinha4":
        imagebutton:
            idle "transparente.png"   
            action Jump("sala2")
            xpos 450  
            ypos 520  
            xsize 900
            ysize 1000  



screen ending_screen:

    vbox:
        xalign 0.5  # Centraliza horizontalmente
        yalign 0.5  # Centraliza verticalmente
        spacing 20  # Espaçamento entre as linhas de texto

        # Agradecimento ao jogador
        text "Obrigado por jogar 'As Cores da Saudade'.":
            size 40
            color "#FFFFFF"
            bold True

        # Espaçamento extra entre as seções
        null height 30

        # Créditos de produção
        text "Produção: Vitória Daris Bender":
            size 30
            color "#CCCCCC"

        # Créditos de trilha sonora
        text "Trilha Sonora: Guilherme Reinehr":
            size 30
            color "#CCCCCC"

        # Encerramento
        null height 30
        text "Nos vemos na próxima jornada.":
            size 25
            color "#AAAAAA"

    
