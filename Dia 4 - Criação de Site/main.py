# Importa o módulo do flet para criar interfaces de usuário
import flet as ft
# Importa o módulo datetime para trabalhar com datas e horas
from datetime import datetime

# Função principal do app
def main(page: ft.Page):
    # Configurações da página
    page.title = "Hashzap"  # Define o título da aba no navegador
    page.scroll = True  # Permite que a página tenha rolagem caso o conteúdo ultrapasse o tamanho da tela
    page.bgcolor = ft.colors.BLACK  # Define o fundo da página como preto
    page.theme_mode = ft.ThemeMode.DARK  # Define o modo escuro para a interface

    # Cria a área do chat onde as mensagens vão aparecer
    chat = ft.Column(auto_scroll=True, expand=True)

    # Variável para armazenar o nome do usuário
    nome_usuario = ""

    # Função chamada quando uma nova mensagem é recebida
    def enviar_mensagem_tunel(mensagem):
        # Divide a mensagem em duas partes: nome e conteúdo
        nome_msg, conteudo = mensagem.split(":", 1)

        # Pega a hora atual no formato HH:MM
        hora = datetime.now().strftime("%H:%M")

        # Verifica se a mensagem é do próprio usuário
        is_me = nome_msg.strip() == nome_usuario.strip()

        # Cria a bolha da mensagem com o nome do usuário, conteúdo da mensagem e horário
        bolha = ft.Container(
            content=ft.Column([
                ft.Text(nome_msg.strip(), size=12, weight=ft.FontWeight.BOLD, color=ft.colors.BLUE_100),  # Nome do usuário
                ft.Text(conteudo.strip(), size=14, color=ft.colors.WHITE),  # Conteúdo da mensagem
                ft.Text(hora, size=10, italic=True, color=ft.colors.GREY_400)  # Hora da mensagem
            ], spacing=2),
            # Alinha a bolha da mensagem à direita se for do próprio usuário, senão à esquerda
            alignment=ft.alignment.center_right if is_me else ft.alignment.center_left,
            # Define a cor de fundo da bolha de mensagem dependendo de quem enviou
            bgcolor=ft.colors.GREEN_900 if is_me else ft.colors.BLUE_GREY_900,
            padding=10,  # Adiciona espaçamento interno
            border_radius=10,  # Deixa os cantos arredondados
            margin=5,  # Espaçamento entre as bolhas
            width=300,  # Define a largura das bolhas de mensagem
        )

        # Cria a linha que vai posicionar a bolha corretamente
        alinhamento = ft.Row([bolha], alignment="end" if is_me else "start")
        chat.controls.append(alinhamento)  # Adiciona a bolha de mensagem ao chat
        page.update()  # Atualiza a página para exibir a nova mensagem

    # Inscreve a função enviar_mensagem_tunel para escutar as mensagens recebidas
    page.pubsub.subscribe(enviar_mensagem_tunel)

    # Função chamada quando o botão de enviar é clicado ou o Enter é pressionado
    def enviar_mensagem(evento):
        if campo_mensagem.value.strip() != "":
            # Formata a mensagem com o nome do usuário e o conteúdo
            mensagem = f"{nome_usuario}: {campo_mensagem.value}"
            page.pubsub.send_all(mensagem)  # Envia a mensagem para todos os usuários conectados
            campo_mensagem.value = ""  # Limpa o campo de mensagem
            page.update()  # Atualiza a página para limpar o campo de mensagem

    # Cria o campo onde o usuário digita a mensagem
    campo_mensagem = ft.TextField(
        label="Digite sua mensagem",
        on_submit=enviar_mensagem,  # Envia a mensagem ao apertar Enter
        expand=True,  # Faz o campo ocupar todo o espaço disponível
        bgcolor=ft.colors.GREY_900,  # Cor de fundo do campo
        color=ft.colors.WHITE  # Cor do texto
    )

    # Cria o botão de enviar mensagem
    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)

    # Cria a linha com o campo de mensagem e o botão de enviar
    linha_mensagem = ft.Row([campo_mensagem, botao_enviar])

    # Função chamada quando o usuário entra no chat (digita o nome)
    def entrar_chat(evento):
        nonlocal nome_usuario
        nome_usuario = campo_nome.value.strip()  # Salva o nome digitado pelo usuário

        if nome_usuario == "":
            return  # Se o nome estiver vazio, não faz nada

        # Envia para todos os usuários que o usuário entrou no chat
        page.pubsub.send_all(f"{nome_usuario} entrou no chat")
        dialog.open = False  # Fecha a janela de boas-vindas
        page.update()  # Atualiza a página

        # Remove o título e o botão de iniciar da tela
        page.remove(titulo)
        page.remove(botao_iniciar)

        # Adiciona o chat e o campo de mensagens à tela
        page.add(chat)
        page.add(linha_mensagem)

    # Cria o campo onde o usuário digita o nome
    campo_nome = ft.TextField(
        label="Digite seu nome",
        autofocus=True,  # Faz o campo receber foco automaticamente ao abrir a janela
        on_submit=entrar_chat,  # Envia o nome ao apertar Enter
        bgcolor=ft.colors.GREY_900,  # Cor de fundo do campo
        color=ft.colors.WHITE  # Cor do texto
    )

    # Cria o botão de entrar no chat
    botao_entrar = ft.ElevatedButton("Entrar no chat", on_click=entrar_chat)

    # Cria a janela de boas-vindas (popup)
    dialog = ft.AlertDialog(
        modal=True,  # A janela é modal, ou seja, impede que o usuário interaja com o resto da página até fechá-la
        title=ft.Text("Bem-vindo ao Hashzap!", color=ft.colors.WHITE),
        content=campo_nome,  # O conteúdo da janela é o campo onde o usuário digita o nome
        actions=[botao_entrar],  # Ação que fecha a janela e entra no chat
        actions_alignment="end"  # Alinha o botão de ação à direita
    )

    # Adiciona a janela à camada superior da interface (sobreposta aos outros elementos)
    page.overlay.append(dialog)

    # Função chamada quando o botão "Iniciar Chat" é clicado
    def abrir_dialog(evento):
        dialog.open = True  # Abre a janela de boas-vindas
        page.update()  # Atualiza a página para exibir a janela

    # Título da página e botão de iniciar chat
    titulo = ft.Text("Hashzap", size=30, weight=ft.FontWeight.BOLD, color=ft.colors.GREEN_ACCENT)
    botao_iniciar = ft.ElevatedButton("Iniciar Chat", on_click=abrir_dialog)

    # Adiciona o título e o botão na tela
    page.add(titulo)
    page.add(botao_iniciar)

# Roda o app no navegador
ft.app(target=main, view=ft.WEB_BROWSER)
