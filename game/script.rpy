define bgm = "audio/vitz.wav"

image corredor = im.Scale("images/corredor.png", 1748, 1087)
image cozinha1 = im.Scale("images/cozinha1.png", 1748, 1087)
image cozinha2 = im.Scale("images/cozinha2.png", 1748, 1087)
image cozinha3 = im.Scale("images/cozinha3.png", 1748, 1087)
image quarto1 = im.Scale("images/quarto1.png", 1748, 1087)
image quarto2 = im.Scale("images/quarto2.png", 1748, 1087)
image quarto3 = im.Scale("images/quarto3.png", 1748, 1087)
image sala1 = im.Scale("images/sala1.png", 1748, 1087)
image sala2 = im.Scale("images/sala2.png", 1748, 1087)
image sala3 = im.Scale("images/sala3.png", 1748, 1087)
image sala4 = im.Scale("images/sala4.png", 1748, 1087)
image psique = im.Scale("images/psique.png", 1748, 1087)
image psique2 = im.Scale("images/psique2.png", 1748, 1087)
image BotaoPorta = im.Scale("images/BotaoPorta.png", 800, 800)


label splashscreen:
    play movie "initGameOK.webm"
    $ renpy.pause(29.0, hard=True)
    window hide
    pause
    
    stop movie
    return

label start:
    play music bgm loop
    scene psique with fade
    "novamente aqui"


    scene psique2
  
    
    # Pergunta 1
    "Por que você continua voltando aqui?"
    menu:
      

        "Eu preciso entender.":
            pass
        "Eu não consigo seguir em frente.":
            pass

    # Pergunta 2
    "Entender não trará de volta o que foi perdido."
    menu:
        

        "Mas eu sinto que devo tentar.":
            pass
        "Nada parece real.":
            pass

    # Pergunta 3
    "Você acha que poderia ter feito algo diferente?"
    menu:
       

        "Sim, talvez eu pudesse.":
            pass
        "Não, mas eu ainda me culpo.":
            pass

    # Pergunta 4
    "A culpa é um peso que você carrega sozinho."
    menu:

        "Eu não sei como deixar ir.":
            pass
        "Eu preciso de tempo.":
            pass

    # Pergunta 5
    "O tempo pode curar, mas as cicatrizes sempre estarão lá."
    menu:

        "Eu não sei se estou pronto para isso.":
            pass
        "Acho que preciso seguir em frente.":
            pass

    "Talvez, com o tempo, tudo se torne mais claro."

python:
    def sala_interacao(mensagem):
        renpy.say(None, mensagem) 
    
scene sala1 with fade


image botaoEsquerda = "botaoEsquerda.png"
image botaoDireita = "botaoDireita.png"

# Variável para controlar a sala atual
default current_room = "sala1"

# Lista de salas disponíveis
define salas = ["sala1", "sala2", "sala3", "sala4"]

python:
    def mudar_sala(direcao):
        global current_room
        current_index = salas.index(current_room)
        if direcao == "esquerda":
            current_room = salas[(current_index - 1) % len(salas)]
        elif direcao == "direita":
            current_room = salas[(current_index + 1) % len(salas)]

while True: 
    call screen navegar_salas
return


label corredor:
    scene corredor with fade 
    call screen corredor


# Variável para controlar o quarto atual
default current_quarto = "quarto1"

# Lista de quartos disponíveis
define quartos = ["quarto1", "quarto2", "quarto3"]

python early:
    def mudar_quarto(direcao):
        global current_quarto
        if current_quarto in quartos:  # Verifica se current_quarto é válido
            current_index = quartos.index(current_quarto)
            if direcao == "esquerda":  # Vai para o quarto anterior
                current_quarto = quartos[(current_index - 1) % len(quartos)]
            elif direcao == "direita":  # Vai para o próximo quarto
                current_quarto = quartos[(current_index + 1) % len(quartos)]
        else:
            # Caso esteja fora da lista, redefine para o primeiro quarto
            current_quarto = "quarto1"

scene quarto1 with fade

label quartos_navegacao:
    scene quarto1 with fade
    while True:
        call screen navegar_quartos
    return

label sala3: 
    scene sala3 with fade
    call screen navegar_salas
    return

label play_video:
    
    play movie "dia.webm"
    window hide
    $ renpy.pause(21.0, hard=True)  
    stop movie
    jump quartos_navegacao  



default current_cozinha = "cozinha1"

define cozinhas = ["cozinha1", "cozinha2", "cozinha3"]

python early:
    def mudar_cozinha(direcao):
        global current_cozinha
        if current_cozinha in cozinhas:  # Verifica se current_cozinha é válido
            current_index = cozinhas.index(current_cozinha)
            if direcao == "esquerda":  # Vai para a sala anterior
                current_cozinha = cozinhas[(current_index - 1) % len(cozinhas)]
            elif direcao == "direita":  # Vai para a próxima sala
                current_cozinha = cozinhas[(current_index + 1) % len(cozinhas)]
        else:
            # Caso esteja fora da lista, redefine para a primeira sala
            current_cozinha = "cozinha1"


label cozinha_navegacao:
    scene cozinha1 with fade
    while True:
        call screen navegar_cozinha
    return
