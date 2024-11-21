define bgm = "audio/vitz.wav"

image ainda = im.Scale("images/ainda.png", 1748, 1087)
image corredor = im.Scale("images/corredor.png", 1748, 1087)
image cozinha1 = im.Scale("images/cozinha1.png", 1748, 1087)
image cozinha2 = im.Scale("images/cozinha2.png", 1748, 1087)
image cozinha3 = im.Scale("images/cozinha3.png", 1748, 1087)
image cozinha4 = im.Scale("images/cozinha4.png", 1748, 1087)
image quarto1 = im.Scale("images/quarto1.png", 1748, 1087)
image quarto2 = im.Scale("images/quarto2.png", 1748, 1087)
image quarto3 = im.Scale("images/quarto3.png", 1748, 1087)
image sala1 = im.Scale("images/sala1.png", 1748, 1087)
image sala2 = im.Scale("images/sala2.png", 1748, 1087)
image sala2_interacao = im.Scale("images/sala2_interacao.png", 1748, 1087)
image sala3 = im.Scale("images/sala3.png", 1748, 1087)
image sala3_interacao = im.Scale("images/sala3_interacao.png",1748, 1087)
image sala4 = im.Scale("images/sala4.png", 1748, 1087)
image psique = im.Scale("images/psique.png", 1748, 1087)
image psique2 = im.Scale("images/psique2.png", 1748, 1087)
image BotaoPorta = im.Scale("images/BotaoPorta.png", 800, 800)
default actions_completed = 0 
default total_actions = 4     
default sala2_interacao_done = False
default quarto1_interacao_done = False
default cozinha_interacao_done = False
default sala3_interacao_done = False


label splashscreen:
    play movie "initGameOK.webm"
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
    def sala_interacao_safe(mensagem):
        renpy.call_in_new_context("display_message", mensagem)

    
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

define cozinhas = ["cozinha1", "cozinha2", "cozinha3", "cozinha4"]

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

label sala3_interacao:

    scene sala3_interacao with fade

    "Por que você sente que ainda carrega essa dor com você?"
    menu:
        "Porque ela é parte do amor que eu sinto.":
            pass
        "Porque ainda estou aprendendo a lidar com isso.":
            pass

    "Você acha que é possível encontrar paz sem esquecer dela?"
    menu:
        "Sim, porque as memórias são parte de mim.":
            pass
        "Acho que sim, estou tentando entender como.":
            pass

    "Essas lembranças, o que elas significam para você agora?"
    menu:
        "São um conforto nos momentos difíceis.":
            pass
        "São minha forma de mantê-la presente.":
            pass

    "Se ela pudesse te ver agora, o que você acha que ela diria?"
    menu:
        "Que eu devo viver, mesmo sentindo saudade.":
            pass
        "Que eu encontre felicidade novamente.":
            pass

    "Você sente que está começando a transformar essa dor em algo maior?"
    menu:
        "Sim, acho que estou aprendendo a seguir em frente.":
            pass
        "Estou tentando, um passo de cada vez.":
            pass

    "O que te faz continuar caminhando apesar da saudade?"
    menu:
        "Saber que ela queria que eu fosse feliz.":
            pass
        "As memórias que me dão força para continuar.":
            pass

    "A aceitação não significa esquecer, mas sim encontrar um novo jeito de amar."

    $ renpy.pause(0.5)
    jump ending_scene

    return



label sala2_interacao:
 
    scene sala2_interacao with fade

    "Por que você guarda essas memórias tão perto do coração?"
    menu:
        "Elas são tudo o que me resta agora.":
            pass
        "Porque não quero esquecer. Nunca.":
            pass

    "Será que a saudade sempre vai te fazer chorar?"
    menu:
        "Acho que sim, por enquanto.":
            pass
        "Talvez, também mostra o quanto eu amava.":
            pass

    "Essas lembranças te confortam ou te machucam mais?"
    menu:
        "As duas coisas... depende do momento.":
            pass
        "Elas machucam, mas fazem sentir próximo.":
            pass

    "Você acha que conseguiria viver sem essas lembranças?"
    menu:
        "Não, elas fazem parte de quem eu sou agora.":
            pass
        "Eu não sei... isso me assusta.":
            pass

    "Você sente que está pronto para transformar a dor em algo positivo?"
    menu:
        "Ainda não, preciso de mais tempo.":
            pass
        "Talvez... mas não sei por onde começar.":
            pass
    
    scene ainda with fade
    "parece que ainda está aqui comigo"

    $ renpy.pause(0.2)
    jump sala2
    return

label sala2:
    scene sala2 with fade
    call screen navegar_salas
    return


label ending_scene:
    # Mostra um fundo preto
    scene black with fade

    show screen ending_screen

    $ renpy.pause(10)
    return
