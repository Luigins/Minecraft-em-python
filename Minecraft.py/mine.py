from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import random

# 1. Inicializa a aplicação Ursina
app = Ursina()

# Configurações da janela
window.fps_counter.enabled = True
window.exit_button.enabled = False  # Oculta o botão 'X' padrão da interface para usarmos o nosso menu

# 2. Classe do Bloco (Voxel)
class Voxel(Button):
    def __init__(self, position=(0, 0, 0), color_val=None):
        if color_val is None:
            color_val = color.hsv(0, 0, random.uniform(0.85, 1.0))

        super().__init__(
            parent=scene,
            position=position,
            model='cube',
            origin_y=0.5,
            texture='white_cube',
            color=color_val,
            highlight_color=color.lime
        )

    def input(self, key):
        # Se o menu estiver aberto, não permite colocar nem destruir blocos
        if menu_panel.enabled:
            return

        if self.hovered:
            if key == 'left mouse down':
                Voxel(position=self.position + mouse.normal)
            elif key == 'right mouse down':
                destroy(self)

# 3. Geração do mapa inicial (Grelha 16x16)
for z in range(16):
    for x in range(16):
        voxel = Voxel(position=(x, 0, z))

# 4. Jogador em primeira pessoa
player = FirstPersonController()

# 5. --- INTERFACE DO MENU DE PAUSA (UI) ---

# Painel principal do menu (desativado por padrão)
menu_panel = Entity(parent=camera.ui, enabled=False)

# Fundo escuro semitransparente para cobrir o ecrã
background = Entity(
    parent=menu_panel,
    model='quad',
    scale=(2, 2),
    color=color.rgba(0, 0, 0, 0.7)
)

# Título do Menu
title = Text(
    parent=menu_panel,
    text='MENU DE PAUSA',
    origin=(0, 0),
    scale=2,
    position=(0, 0.2)
)

# Função para alternar o estado do menu (Abrir / Fechar)
def toggle_menu():
    # Inverte o estado de visibilidade do menu
    menu_panel.enabled = not menu_panel.enabled
    
    # Liberta ou bloqueia o cursor do rato conforme o menu está aberto ou fechado
    mouse.locked = not menu_panel.enabled
    
    # Pausa ou ativa a movimentação do jogador
    player.enabled = not menu_panel.enabled

# Botão "Continuar"
btn_resume = Button(
    parent=menu_panel,
    text='Continuar',
    color=color.azure,
    scale=(0.3, 0.08),
    position=(0, 0.05),
    on_click=toggle_menu  # Executa a função toggle_menu ao clicar
)

# Botão "Sair do Jogo"
btn_quit = Button(
    parent=menu_panel,
    text='Sair do Jogo',
    color=color.red,
    scale=(0.3, 0.08),
    position=(0, -0.08),
    on_click=application.quit  # Fecha a janela do jogo e encerra o script no terminal
)

# Função global que escuta a tecla 'ESC' para abrir/fechar o menu
def input(key):
    if key == 'escape':
        toggle_menu()

# 6. Executa o jogo
app.run()