from difflib import SequenceMatcher


def calculaMediaFinal(ac, Prova):
    media = 0.6 * ac + 0.4 * Prova
    return media



def verificaCopia(texto1, texto2):
    var = int(SequenceMatcher(None, texto1, texto2).ratio())

    if(var >= 0.8):
       return True
    else:
       return False
        




print(verificaCopia('Tassio','Tassio'))