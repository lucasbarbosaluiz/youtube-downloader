import os
from tkinter import Tk, Label, Entry, Button, filedialog, StringVar, messagebox
from pytube import YouTube

class YouTubeDownloaderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Downloader do YouTube")
        self.root.geometry("400x300")
        self.root.resizable(False, False)
        
        # Elementos da Interface Gráfica
        Label(root, text="Downloader do YouTube", font=("Arial", 16, "bold")).pack(pady=10)
        
        Label(root, text="Insira a URL do YouTube:", font=("Arial", 12)).pack(pady=5)
        self.url_var = StringVar()
        Entry(root, textvariable=self.url_var, width=40).pack(pady=5)
        
        Button(root, text="Escolher Local para Salvar", command=self.escolher_local).pack(pady=5)
        self.caminho_salvar = StringVar()
        Label(root, textvariable=self.caminho_salvar, font=("Arial", 10), fg="blue").pack(pady=5)
        
        Button(root, text="Baixar Vídeo", command=self.baixar_video).pack(pady=10)
        Button(root, text="Baixar Áudio", command=self.baixar_audio).pack(pady=5)
    
    def escolher_local(self):
        local = filedialog.askdirectory()
        if local:
            self.caminho_salvar.set(local)
    
    def baixar_video(self):
        self.baixar_conteudo(video=True)
    
    def baixar_audio(self):
        self.baixar_conteudo(video=False)
    
    def baixar_conteudo(self, video=True):
        url = self.url_var.get().strip()
        caminho_salvar = self.caminho_salvar.get().strip()
        
        if not url:
            messagebox.showerror("Erro", "Por favor, insira uma URL válida do YouTube.")
            return
        if not caminho_salvar:
            messagebox.showerror("Erro", "Por favor, selecione um local para salvar o arquivo.")
            return
        
        try:
            yt = YouTube(url)
            stream = yt.streams.get_highest_resolution() if video else yt.streams.filter(only_audio=True).first()
            stream.download(caminho_salvar)
            
            tipo_conteudo = "Vídeo" if video else "Áudio"
            messagebox.showinfo("Sucesso", f"{tipo_conteudo} baixado com sucesso!\nSalvo em: {caminho_salvar}")
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao baixar o conteúdo. ({e})")

# Aplicação Principal
if __name__ == "__main__":
    root = Tk()
    app = YouTubeDownloaderApp(root)
    root.mainloop()
