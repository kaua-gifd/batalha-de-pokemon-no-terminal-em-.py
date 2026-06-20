import time
import os
import random
#area dos modelos

hpe = 430
turno = 0
ataque = 20

time.sleep(1)
print ("Bem vindo ao mundo pokémon water blue")
time.sleep(1)
nome = input("Qual vai ser seu nome?: ")
print (f"apartir de agora vc vai se chamar {nome}")
print ("vamos vamos logo,o professor está te chamando para escolher um pokémon para sua jornada")
time.sleep(1)
print ("indo até o professor....")
time.sleep(5)
os.system('clear')
time.sleep(2)
print (f"Oi {nome} finalmente vc veio escolher seu pokémon para sua jornada,vc tem apenas 3 opções")
time.sleep(2.40)
os.system('clear')
pk = input("Me diga qual ira ser seu pokémon,vc pode escolher um tortokal,lapras ou um garchomp: ")
while pk != "tortokal" and pk != "lapras" and pk != "garchomp":
    print ("escholha apenas os Pokemons que eu te ofereci seu teimoso")
    time.sleep(2.40)
    os.system('clear')
    pk = input("Me diga qual ira ser seu pokémon,vc pode escolher um tortokal,lapras ou um garchomp: ")
time.sleep(1)
print (f"Otima escholha,o seu {pk} já está em sua mochila/team é está pronto para batalhas")
time.sleep(1)
print (f"Vamos {nome} até a rota 15 para explorar um pouco")
time.sleep(0.60)
s = input("Vc quer ir?.s/n: ")
time.sleep(0.20)
if s == "s" or s == "sim":
    print ("Vamoss")
else:
    print ("só br")
print("indo até o parque....")
time.sleep(2)
os.system('clear')
print ("Chegamos finalmente ao parque")
time.sleep(2.70)
print (" - Ei vcs dois,eu quero batalhar com alguém, pelo visto vcs podem ser uma ótima escolha")
time.sleep(2.50)
print (f"Vai {nome} mostre seu potencial")
time.sleep(2.50)
print ("entrando em batalha")
time.sleep(2.50)
os.system('clear')
if pk == "tortokal":
    moves = ["lava plume", "eruption", "heat wave", "scratch"]
    mv = "lava plume,eruption,heat wave,scratch"
    hp = 70
    attack = 85
    speed = 20
elif pk == "lapras":
    moves = ["rain dance", "surf", "water gun", "brine"]
    mv = "rain dance,surf,water gun,brine"
    hp = 130
    attack = 90
    speed = 60
elif pk == "garchomp":
    moves = ["earthquake", "outrage", "bite", "scratch"]
    mv = "earthquake,outrage,bite,scratch"
    hp = 108
    attack = 130
    speed = 102
def battle():
    print (f"VIDA ATUAL DO POKE INIMIGO: {hpe}")
    print (" ==== BATTLE ====")
    print (f"SEUS GOLPES SÃO: {mv}")
    print (f"HP DO SEU POKE: {hp}")
    print (f"ATTACK DO SEU POKE: {attack}")
    print (f"SPEED DO SEU POKE: {speed}")
def attack1(hpe):
    m = random.randint(1,200)
    dano = (m + attack)
    hpe = hpe - dano
    return hpe, dano
def ataque(hp):
    n2 = random.randint(1,50)
    hp = (hp - n2)
    return hp, n2
pn = ["charizard", "gardevoair", "galade"]
pok = random.choice(pn)
print (f"UM PODEROSO(A) {pok} ESTÁ EM CAMPO")
time.sleep(2)
print (f"VÁ {pk}")
time.sleep(1)
battle()
while hpe >=1:
    os.system('clear')

    turno += 1

    print(f"TURNO {turno}")

    battle()

    move_escolha = input("Me diga qual move vc deseja usar: ")

    while move_escolha not in moves:
        print("ESCOLHA UM MOVE VALIDO")
        move_escolha = input("Me diga qual move vc deseja usar: ")

    hpe, dano = attack1(hpe)

    if dano >= 120:
        print(f"O {pk} USOU {move_escolha} É DEU UM ATAQUE CRÍTICO QUE TIROU {dano} DE VIDA DO {pok}")

    else:
        print(f"O {pk} usou {move_escolha} é o {pok} perdeu {dano} de vida")

    time.sleep(2.40)

    hp, n2 = ataque(hp)

    mk = random.choice(moves)

    print(f"o {pok} usou um {mk} e tirou {n2} da vida do seu {pk}")
    time.sleep(3.07)
