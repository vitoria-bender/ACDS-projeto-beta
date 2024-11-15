define bgm = "audio/vitz.wav"


image sala1 = im.Scale("images/sala1.png", 1748, 1087)
image sala2 = im.Scale("images/sala2", 1748, 1087)
image psique = im.Scale("images/psique.png", 1748, 1087)
image psique2 = im.Scale("images/psique2.png", 1748, 1087)


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
    

scene sala1 with fade

# Definindo as cenas na ordem de navegação
define cenas = [
    "sala1", "sala2", "sala3", "sala4",
    "cozinha1", "cozinha2", "cozinha3",
    "corredor",
    "quarto1", "quarto2", "quarto3",
    "banheiro1", "banheiro2"
]

# Variável para controlar o índice da cena atual
default current_scene_index = 0

# Função para atualizar a cena conforme o índice atual
label update_scene():
    $ current_scene = cenas[current_scene_index]
    show expression current_scene
    call screen explorar_cena
    return

# Tela com hotspots nas setas para navegação
screen explorar_cena():
    # Exibe a imagem da cena atual
    add current_scene + ".png"  # Certifique-se de que os arquivos de imagem estão nomeados como "sala1.png", etc.

    # Hotspot para a seta da esquerda (volta para a cena anterior)
    hotspot (20, 250, 50, 50) action [
        SetVariable("current_scene_index", (current_scene_index - 1) % len(cenas)),
        Jump("update_scene")
    ]

    # Hotspot para a seta da direita (avança para a próxima cena)
    hotspot (730, 250, 50, 50) action [
        SetVariable("current_scene_index", (current_scene_index + 1) % len(cenas)),
        Jump("update_scene")
    ]
