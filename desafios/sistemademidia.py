class midia:
    def __init__(self, titulo, duracao_seg):
        self.titulo = titulo
        self.duracao_seg = duracao_seg

        def exibir(self):
            print("A música que está tocando é {self.titulo} com a duração de {duracao_seg} ")

class musica(midia):
    def __init__(self, titulo, duracao_seg, artista):
        super().__init__(titulo, duracao_seg)
        self.artista = artista
        
    def exibir(self):
        print(f"{self.titulo} do artista {self.artista} com a duração de {self.duracao_seg}")

musica1 = musica("Hippie-Punk-Rejneesh", "2:42", "Os Replicantes")
musica2 = musica("Rock, luxuria e diabo", "4:37", "Os Replicantes")

class video(midia):
    def __init__(self, titulo, duracao_seg, resolucao):
        super().__init__(titulo, duracao_seg)
        self.resolucao = resolucao
    def exibir(self):
        print(f"O Video: {self.titulo} com a duração {self.duracao_seg} possui a resolução de {self.resolucao}")

video1 = video("Como dissolver um frango de 70kg com a altura de 1.72", "14:51", "1920x1080")

dicionario_midia:dict[str, list[midia]] = {"musicas":[], "videos":[]}
dicionario_midia["musicas"].append(musica1)
dicionario_midia["musicas"].append(musica2)
dicionario_midia["videos"].append(video1)

for item in dicionario_midia.values():
    for midia in item:
        midia.exibir()