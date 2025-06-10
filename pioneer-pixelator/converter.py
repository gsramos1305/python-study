# converter.py
from moviepy.editor import VideoFileClip
from PIL import Image, ImagePalette
import numpy as np
import os

# Paleta azul-esverdeada estilo Pioneer (simplificada)
PIONEER_PALETTE = [
    0, 0, 0,         # preto
    0, 64, 64,       # azul petróleo escuro
    0, 128, 128,     # azul-esverdeado
    64, 255, 255,    # ciano claro
    255, 255, 255    # branco
] + [0] * (256 * 3 - 15)  # Preenche o resto da paleta com zeros

def apply_pioneer_palette(image: Image.Image):
    pal_img = Image.new("P", (16, 16))
    pal_img.putpalette(PIONEER_PALETTE)
    return image.convert("RGB").quantize(palette=pal_img)

def process_frame(frame, size=(80, 60)):
    img = Image.fromarray(frame)
    img = img.resize(size, Image.NEAREST)
    img = apply_pioneer_palette(img)
    return img

def convert_to_pixel_gif(input_path, output_path, pixel_size=(80, 60), palette_colors=16):
    clip = VideoFileClip(input_path)
    frames = []
    
    for frame in clip.iter_frames():
        image = Image.fromarray(frame)
        # Reduz resolução para pixelizar
        image_small = image.resize(pixel_size, Image.NEAREST)
        # Aplica paleta limitada (usaremos adaptativa para exemplo)
        image_small = image_small.convert("P", palette=Image.ADAPTIVE, colors=palette_colors)
        # Volta para RGB para salvar corretamente
        image_small = image_small.convert("RGB")
        # Volta ao tamanho original para efeito pixelado
        image_pixelated = image_small.resize(frame.shape[1::-1], Image.NEAREST)
        frames.append(np.array(image_pixelated))
    
    # Salva como GIF animado
    imageio.mimsave(output_path, frames, fps=clip.fps)
