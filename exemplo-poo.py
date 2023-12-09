

class Programa:

    def __init__( self, nome, ano ): # inicializador da classe Programa.
        self._nome = nome.title() # nome com a primeira letra sempre maiúscula. 
        self.ano = ano # ano do programa.
        self._likes = 0 # quantidade de likes recebidos.

    @property # criando propriedade para visualizar a quantidade de likes.
    def likes( self ):
        return self._likes

    def dar_likes( self ): # método para dar like. 
        self._likes += 1

    @property # criando propriedade para visualizar o nome do programa.
    def nome( self ):
        return self._nome

    @nome.setter # criando setter para alterar o nome do programa.
    def nome( self, nome ):
        self._nome = nome

    def __str__( self ): # python data model de string para print, por exemplo.
        return f'Nome: {self.nome} Likes: {self.likes}'


class Filme( Programa ): 

    def __init__( self, nome, ano, duracao ): # inicializador da classe Filme com herança (pai) Programa. Herdando coisas da classe pai.
        super().__init__( nome, ano ) # pegando os atributos nome e ano da classe pai (Programa).
        self.duracao = duracao
    
    def __str__( self ): # python data model de string para print, por exemplo.
        return f'Nome: {self.nome} - {self.duracao} min - Likes: {self.likes}'


class Serie( Programa ):

    def __init__( self, nome, ano, temporadas ): # inicializador da classe Serie com herança (pai) Programa. Herdando coisas da classe pai.
        super().__init__( nome, ano ) # pegando os atributos nome e ano da classe pai (Programa).
        self.temporadas = temporadas

    def __str__( self ): # python data model de string para print, por exemplo.
        return f'Nome: {self.nome} - {self.temporadas} temporadas - Likes: {self.likes}'


class Playlist():

    def __init__( self, nome, programas ): # inicializador da classe Playlist.
        self.nome = nome
        self._programas = programas

    def __getitem__( self, item ): # python data model de getitem, com características iteráveis.
        return self._programas[ item ]

    def __len__( self ): # python data model de len, com características size.
        return len( self._programas ) 


vingadores = Filme( 'vingadores - guerra infinita', 2018, 160 )
atlanta = Serie( 'atlanta', 2018, 2 )
tmep = Filme( 'todo mundo em panico', 1999, 100 )
demolidor = Serie( 'demolidor', 2016, 2 )

vingadores.dar_likes() # dando like.
vingadores.dar_likes() # dando like.
vingadores.dar_likes() # dando like.
atlanta.dar_likes() # dando like.
atlanta.dar_likes() # dando like.
tmep.dar_likes() # dando like.
tmep.dar_likes() # dando like.
demolidor.dar_likes() # dando like.
demolidor.dar_likes() # dando like.

listinha = [ atlanta, vingadores, demolidor, tmep ] # lista para a playlist.
minha_playlist = Playlist( 'fim de semana', listinha ) # criando a playlist 'fim de semana'.

for programa in minha_playlist:
    print( programa )

print( f'Tamanho: { len( minha_playlist ) }' )

