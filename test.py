# test_typewriter.py

from py_typewriter import write, blink, fade_text, scroll_text, loading, color_text
import time

def test_write():
    print("Teste write:")
    write("Escrevendo devagar...", 3)
    time.sleep(1)

def test_blink():
    print("Teste blink:")
    blink("Pisca-pisca!", duracao=3, intervalo=0.3)
    time.sleep(1)

def test_fade_text():
    print("Teste fade_text:")
    fade_text("Fade in/out", duracao=4)
    time.sleep(1)

def test_scroll_text():
    print("Teste scroll_text:")
    scroll_text("Rolagem de texto legal!", largura=15, duracao=5)
    time.sleep(1)

def test_loading():
    print("Teste loading:")
    loading("Carregando", duracao=3, intervalo=0.4)
    time.sleep(1)

def test_color_text():
    print("Teste color_text:")
    color_text("Vermelho", cor="red")
    color_text("Verde", cor="green")
    color_text("Azul", cor="blue")
    color_text("Amarelo", cor="yellow")
    time.sleep(1)

if __name__ == "__main__":
    test_write()
    test_blink()
    test_fade_text()
    test_scroll_text()
    test_loading()
    test_color_text()
    print("\nTodos os testes concluídos!")
