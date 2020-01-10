"""Tradutor para morsecode."""
from morsealphabet import MORSE_ALPHABET
from winsound import Beep

def beepType(character):
    """Seleciona o beep de acordo com o simbolo.
    
    Parameters
    ----------
    character: str
        Caractere representando o ponto ou hifen.

    """
    if character == ".":
        Beep(2700, 90)
    if character == "-":
        Beep(2700, 900)

def textToMorse(text) -> None:
    """Traduzir um texto qualquer para morsecode.
    
    Parameters
    ----------
    text: str
        Texto qualquer.
    
    """
    text = text.upper()
    morse_text = list(map(lambda c: MORSE_ALPHABET.get(c, "unknown"), text))
    print("Morse Code: ", end="")
    for morse in morse_text:
        print(morse, end=" ")
        for character in morse:
            beepType(character)
    print()
        
if __name__ == "__main__":
    textToMorse("OlaMundo")
    textToMorse("Ola Mundo")
