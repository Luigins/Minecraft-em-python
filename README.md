# # ⛏️ Minecraft.py

Um clone simples e funcional de **Minecraft** desenvolvido em **Python**. O projeto recria a experiência clássica de um jogo sandbox 3D baseado em blocos (voxels), permitindo explorar o cenário, construir estruturas e minerar blocos em tempo real.

---

## 📌 Funcionalidades

- **Mundo 3D em Voxel:** Renderização de blocos em um ambiente tridimensional.
- **Mecânicas de Construção:**
  - **Colocar blocos:** Clique com o botão direito do mouse para posicionar novos blocos no mundo.
  - **Quebrar blocos:** Clique com o botão esquerdo do mouse para remover blocos existentes.
- **Movimentação do Jogador:**
  - Controle de câmera estilo em primeira pessoa (FPS).
  - Andar, correr e pular com detecção de colisão básica e gravidade.
- **Seleção de Blocos:** Alternância entre diferentes tipos de blocos (como terra, grama, pedra, madeira e tijolos).

---

## 🛠️ Tecnologias e Dependências

- **Linguagem:** [Python 3.8+](https://www.python.org/)
- **Biblioteca principal:**
  - [`ursina`](https://www.ursinaengine.org/) ou [`pyglet`](https://pyglet.org/) *(Verifique qual engine de jogos 3D é utilizada no script `mine.py`)*

---

## 🚀 Como Executar o Projeto

### 1. Pré-requisitos
Certifique-se de ter o **Python 3** instalado na sua máquina. Você pode verificar executando:

```bash
python --version
```

### 2. Instalação das Dependências
Instale a biblioteca necessária via `pip`. Se o seu projeto utilizar a **Ursina Engine**, execute:

```bash
pip install ursina
```

*(Caso utilize outra biblioteca 3D como `pyglet` ou `PyOpenGL`, substitua pelo pacote correspondente)*.

### 3. Executando o Jogo
Navegue até a pasta do projeto e execute o arquivo principal `mine.py`:

```bash
python mine.py
```

---

## 🎮 Controles do Jogo

| Tecla / Ação | Funcionalidade |
| :--- | :--- |
| **W, A, S, D** | Movimentar o jogador (Frente, Esquerda, Trás, Direita) |
| **Espaço** | Pular |
| **Mouse** | Olhar ao redor (Controla a câmera em primeira pessoa) |
| **Clique Esquerdo** | Destruir / Quebrar bloco |
| **Clique Direito** | Adicionar / Colocar bloco |
| **1 - 9** ou **Roda do Mouse** | Selecionar tipo de bloco na barra rápida |
| **ESC** | Liberar o ponteiro do mouse / Pausar ou Sair |

---

## 📁 Estrutura de Arquivos

```text
Minecraft.py/
├── mine.py          # Arquivo principal contendo a lógica do jogo e da engine
├── assets/          # Texturas, modelos e efeitos sonoros (opcional)
└── README.md        # Documentação do projeto
```

---

## 💡 Futuras Melhorias

- [ ] Implementar ciclos de dia e noite com iluminação dinâmica.
- [ ] Adicionar novos tipos de blocos e ferramentas.
- [ ] Implementar cores aos blocos.

---

## 📜 Licença

Este projeto é de uso educacional e livre para modificações e aprendizado.
