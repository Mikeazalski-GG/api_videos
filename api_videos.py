from fastapi import FastAPI, Query
import os
import uvicorn

app = FastAPI(title="API de Busca de Vídeos Suporte")

# Simulação da sua base de dados ou pasta do OneDrive
# Aqui você pode manter a lógica que já tem no seu app.py
videos_db = [
    {"titulo": "Associar produtos - Ammo", "url": "https://link_do_video_1.mp4"},
    {"titulo": "Cancelamento de Venda - Empresa X", "url": "https://link_do_video_2.mp4"},
    {"titulo": "Devolução de Mercadoria", "url": "https://link_do_video_3.mp4"},
]

@app.get("/buscar")
def buscar_video(termo: str = Query(..., description="O termo que o usuário digitou no chat")):
    """
    Esta função faz a busca inteligente que a IA nativa do Copilot está falhando em fazer.
    """
    termo_search = termo.lower()
    resultados = []

    for video in videos_db:
        # Lógica de 70% de similaridade ou busca simples por palavra-chave
        if termo_search in video["titulo"].lower():
            resultados.append(video)

    if not resultados:
        return {"mensagem": "Nenhum vídeo encontrado", "sucesso": False}

    return {"resultados": resultados, "sucesso": True}

if __name__ == "__main__":
    # Roda o servidor localmente para teste
    uvicorn.run(app, host="0.0.0.0", port=8000)