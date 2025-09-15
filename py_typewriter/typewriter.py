import sys
import time

def write(texto: str, duracao: float = 1):
    """
    Exibe um texto no terminal caractere por caractere, simulando o efeito
    de máquina de escrever.

    @param texto: (str) Texto a ser exibido.
    @param duracao: (float) Tempo total em segundos que a exibição completa
                    do texto deve levar. Por padrão, é 1 segundo.
    @raises ValueError: Se 'texto' estiver vazio ou se 'duracao' for menor ou igual a zero.
    """

    if not texto:
        raise ValueError("O parâmetro 'texto' não pode estar vazio.")
    if duracao <= 0:
        raise ValueError("O parâmetro 'duracao' deve ser maior que zero.")

    tempo_por_caracter = duracao / len(texto)
    for char in texto:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(tempo_por_caracter)
    print()

def blink(texto, duracao=3, intervalo=0.5):
    """
    Pisca o texto no terminal por um tempo total de 'duracao' segundos.

    @param texto: Texto a ser exibido
    @param duracao: Tempo total que o texto vai piscar
    @param intervalo: Intervalo entre aparecer e sumir
    """
    import sys, time, os
    fim = time.time() + duracao
    while time.time() < fim:
        sys.stdout.write(texto)
        sys.stdout.flush()
        time.sleep(intervalo)
        sys.stdout.write('\r' + ' ' * len(texto) + '\r')  # limpa
        sys.stdout.flush()
        time.sleep(intervalo)


def loading(texto="Carregando", duracao=5, intervalo=0.5):
    import sys, time
    fim = time.time() + duracao
    while time.time() < fim:
        for i in range(4):
            sys.stdout.write(f"\r{texto}{'.'*i}{' '*(3-i)}")
            sys.stdout.flush()
            time.sleep(intervalo)
    print()


import sys
import time

def fade_text(texto, duracao=3, passos=10):
    """
    Mostra o texto gradualmente (fade in e fade out) no terminal.

    @param texto: Texto a ser exibido
    @param duracao: Tempo total em segundos do efeito
    @param passos: Quantidade de passos do fade
    """
    tempo_por_passos = duracao / (2 * passos)  # metade fade in, metade fade out

    # Fade in
    for i in range(1, passos + 1):
        sys.stdout.write('\r' + texto[:int(len(texto) * i / passos)])
        sys.stdout.flush()
        time.sleep(tempo_por_passos)

    # Fade out
    for i in range(passos, 0, -1):
        sys.stdout.write('\r' + texto[:int(len(texto) * i / passos)] + ' ' * (len(texto) - int(len(texto) * i / passos)))
        sys.stdout.flush()
        time.sleep(tempo_por_passos)
    print()


def scroll_text(texto, largura=20, duracao=5):
    """
    Faz o texto rolar horizontalmente no terminal.

    @param texto: Texto a ser rolado
    @param largura: Quantos caracteres aparecem na tela de cada vez
    @param duracao: Tempo total em segundos
    """
    import sys, time
    texto = ' ' * largura + texto + ' ' * largura
    intervalo = duracao / len(texto)
    for i in range(len(texto) - largura + 1):
        sys.stdout.write('\r' + texto[i:i+largura])
        sys.stdout.flush()
        time.sleep(intervalo)
    print()


def color_text(texto, cor="red"):
    """
    Mostra texto colorido no terminal.

    @param texto: Texto a ser exibido
    @param cor: Cor do texto (red, green, yellow, blue, magenta, cyan, white)
    """
    cores = {
        "red": "\033[91m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "blue": "\033[94m",
        "magenta": "\033[95m",
        "cyan": "\033[96m",
        "white": "\033[97m",
        "reset": "\033[0m"
    }
    sys.stdout.write(cores.get(cor, cores["white"]) + texto + cores["reset"] + "\n")


