from combate import batalha
from personagens import Personagem

heroi = Personagem("Chris", 100, 15, pocoes=1)
monstro = Personagem("Internet da casa", 150, 20)

batalha(heroi, monstro)