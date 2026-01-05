import flet as ft
import traceback # <--- ADICIONE ISSO NO TOPO

# NÃO importe o yt_dlp aqui em cima. Vamos importar lá dentro.

def main(page: ft.Page):
    # Configuração básica da página para garantir que o erro apareça
    page.title = "Meu Player"
    page.scroll = "adaptive" 

    try:
        # --- AQUI COMEÇA O SEU CÓDIGO ---
        
        # 1. Importe o yt_dlp AQUI DENTRO (Isso evita tela preta imediata)
        import yt_dlp 

        # 2. Cole aqui todo o resto do seu código original que estava na função main.
        # Lembre-se de selecionar o seu código e apertar TAB para empurrar para a direita.
        
        page.add(ft.Text("O App iniciou com sucesso!", color="green"))
        
        # Exemplo (seu código deve estar aqui):
        # url_input = ft.TextField(label="URL do YouTube")
        # page.add(url_input)
        # ... resto do seu código ...

        # --- AQUI TERMINA O SEU CÓDIGO ---

    except Exception as e:
        # SE DER ERRO, ELE VAI CAIR AQUI E MOSTRAR NA TELA
        page.clean()
        page.bgcolor = "black"
        page.add(
            ft.Column([
                ft.Text("ERRO FATAL ENCONTRADO:", size=20, weight="bold", color="red"),
                ft.Text(f"Erro: {str(e)}", size=16, color="white"),
                ft.Divider(color="white"),
                ft.Text("Detalhes técnicos:", color="yellow"),
                ft.Text(traceback.format_exc(), size=12, color="yellow", font_family="monospace")
            ])
        )
        page.update()

ft.app(target=main)
