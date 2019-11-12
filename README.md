# PythonMorseCode
Replicar o código morse em python, somente por diversão.

## Observações
Juntamente ao resultado textual será mostrado um som representando cada caractere no código morse.

## Como usar?
```
>> from textToMorse import textToMorse
>> textToMorse("OlaMundo")
Morse Code: --- .-.. .- -- ..- -. -.. ---
```

## Notas
- O script irá ignorar caracteres que não pertençam ao alfabeto morsecode;
- A função utilizada é o Beep do módulo winsound;
- A frequência dos Beeps é 2700.