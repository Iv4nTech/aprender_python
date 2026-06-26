"""
================================================================
 DUNDER METHODS · CONTENEDORES  (__len__, __getitem__, __contains__)
================================================================
App de música. Tu clase Playlist debe comportarse como una lista:
saber cuántas canciones tiene, acceder por índice y comprobar si
una canción está dentro con 'in'.

1- Crea Playlist(canciones) guardando la lista internamente y
   define __len__ para devolver el número de canciones.
   (Solución len(playlist) con 3 canciones:  3)

2- Define __getitem__ para acceder por índice: playlist[0].
   (Solución playlist[0]:  'Bohemian Rhapsody')

3- Define __contains__ para usar 'in'.
   (Solución 'Imagine' in playlist:  True)
   (Solución 'XXX' in playlist:      False)
================================================================
"""

class Playlist():
    def __init__(self):
        self.lista = ["Wakawaka", "La luna", "Juramento de sal"]

    def __len__(self):
        return len(self.lista)

    def __getitem__(self, key):
        return self.lista[key]

    def __contains__(self, item):
        return item in self.lista


p = Playlist()
print(len(p))
print(p[1])
print("Wakowako" in p)
print("Wakawaka" in p)