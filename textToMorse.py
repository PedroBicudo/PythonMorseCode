"""Tradutor para morsecode."""
from morsealphabet import MORSE_ALPHABET
from functools import partial
from winsound import Beep

def beepType(character):
    """Seleciona o beep de acordo com o simbolo.
    
    Parameters
    ----------
    character: str
        Caractere representando o ponto ou hifen.

    """
    return {
        '.': partial(Beep, duration=90),
        '-': partial(Beep, duration=900)
    }.get(character, lambda x: None)(2700)


def textToMorse(text) -> None:
    """Traduzir um texto qualquer para morsecode.
    
    Parameters
    ----------
    text: str
        Texto qualquer.
    
    """
    morse_text = [MORSE_ALPHABET.get(char, "unknown") for char in text.upper()]
    print("Morse Code: ", end="")
    for morse in morse_text:
        print(morse, end=" ")
        for character in morse:
            beepType(character)
    print()
        
if __name__ == "__main__":
    textToMorse("OlaMundo")
    textToMorse("Ola Mundo")
