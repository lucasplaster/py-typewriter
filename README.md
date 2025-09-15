# py_typewriter

`py_typewriter` é um módulo Python que permite exibir textos no terminal com **efeitos visuais**, como máquina de escrever, fade in/out, rolagem, piscar e cores. Ideal para adicionar estilo a scripts e aplicativos de terminal.

---

## Funcionalidades

- `write(texto, duracao=1)`: Exibe o texto **caractere por caractere**, simulando máquina de escrever.
- `blink(texto, duracao=3, interval=0.5)`: Faz o texto **piscar** no terminal.
- `fade_text(texto, duracao=3, passos=10)`: Mostra o texto gradualmente (fade in/out).
- `scroll_text(texto, largura=20, duracao=5)`: Faz o texto **rolar horizontalmente**.
- `loading(texto="Carregando", duracao=5, interval=0.5)`: Cria um efeito de **carregamento animado**.
- `color_text(texto, cor="red")`: Exibe o texto com cores usando ANSI codes (`red`, `green`, `yellow`, `blue`, `magenta`, `cyan`, `white`).

---

## Instalação

Basta clonar o repositório ou copiar a pasta `py_typewriter` para seu projeto:

```
git clone https://github.com/lucasplaster/py-typewriter.git
```
Para usar:

```python
from py_typewriter import write, blink, fade_text, scroll_text, loading, color_text
```
Estrutura do modulo:

```
py_typewriter/
│
├── __init__.py
├── typewriter.py

```
