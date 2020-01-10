"""Tradutor para morsecode."""
from morsealphabet import MORSE_ALPHABET
import functools
import winsound


def beepType(character):
    """Seleciona o beep de acordo com o simbolo.
    
    Parameters
    ----------
    character: str
        Caractere representando o ponto ou hifen.

    """
    return {
        '.': functools.partial(winsound.Beep, duration=90),
        '-': functools.partial(winsound.Beep, duration=900)
    }.get(character, lambda x: None)(2700)


def textToMorse(text) -> None:
    """Traduzir um texto qualquer para morsecode.
    
    Parameters
    ----------
    text: str
        Texto qualquer.
    
    """
    if not isinstance(text, str):
        raise TypeError

    if not set(text.upper()) <= set(MORSE_ALPHABET):
        raise ValueError
    
    morse_text = [MORSE_ALPHABET[char] for char in text.upper()]
    size_morse_text = len(' '.join(morse_text))

    # Reserva um espaco com o tamanho do morse code
    print(" "*size_morse_text, end='', flush=True)
    print("\b"*size_morse_text, end='')

    for morse in morse_text:
        for character in morse:
            beepType(character)
            print(character, end='', flush=True)
        print(" ", end='')
