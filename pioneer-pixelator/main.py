import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import ImageTk
import threading
import time
from converter import convert_to_pixel_gif

class PixelatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pioneer Pixelator - GIF Pixelado")
        self.root.geometry("600x500")
        
        # Variáveis
        self.frames = []
        self.preview_index = 0
        self.preview_running = False
        self.video_path = None
        self.gif_path = "output/pioneer_pixel.gif"
        
        # Widgets
        self.btn_select = tk.Button(root, text="Selecionar Vídeo", command=self.select_video)
        self.btn_select.pack(pady=10)
        
        self.preview_label = tk.Label(root, text="Preview dos quadros pixelados")
        self.preview_label.pack()
        
        self.canvas = tk.Label(root)
        self.canvas.pack(pady=10)
        
        self.btn_convert = tk.Button(root, text="Converter para GIF Pixelado", command=self.convert_video)
        self.btn_convert.pack(pady=10)
        
        self.gif_label = tk.Label(root, text="GIF final aparecerá aqui após conversão")
        self.gif_label.pack()
        
        self.gif_canvas = tk.Label(root)
        self.gif_canvas.pack(pady=10)
        
    def select_video(self):
        path = filedialog.askopenfilename(title="Selecione o vídeo", filetypes=[("Vídeos", "*.mp4 *.avi *.mov *.mkv")])
        if path:
            self.video_path = path
            self.load_preview()
    
    def load_preview(self):
        self.frames = convert_to_pixel_gif(self.video_path, "temp_preview.gif", max_duration=2, fps=6)
        self.preview_index = 0
        if self.frames:
            self.preview_running = True
            self.show_preview()
    
    def show_preview(self):
        if not self.preview_running or not self.frames:
            return
        
        frame = self.frames[self.preview_index]
        img_tk = ImageTk.PhotoImage(frame.resize((320, 240), Image.NEAREST))
        self.canvas.config(image=img_tk)
        self.canvas.image = img_tk
        
        self.preview_index = (self.preview_index + 1) % len(self.frames)
        self.root.after(150, self.show_preview)
    
    def convert_video(self):
        if not self.video_path:
            messagebox.showwarning("Aviso", "Selecione um vídeo antes de converter!")
            return
        
        self.btn_convert.config(state=tk.DISABLED)
        self.gif_label.config(text="Convertendo... Aguarde!")
        
        def task():
            frames = convert_to_pixel_gif(self.video_path, self.gif_path, max_duration=5, fps=10)
            self.show_final_gif()
            self.btn_convert.config(state=tk.NORMAL)
            self.gif_label.config(text=f"GIF salvo em {self.gif_path}")
        
        threading.Thread(target=task).start()
    
    def show_final_gif(self):
        # Carrega o GIF final para mostrar no label
        gif_img = ImageTk.PhotoImage(file=self.gif_path)
        self.gif_canvas.config(image=gif_img)
        self.gif_canvas.image = gif_img

if __name__ == "__main__":
    import os
    if not os.path.exists("output"):
        os.makedirs("output")
    
    root = tk.Tk()
    app = PixelatorApp(root)
    root.mainloop()
