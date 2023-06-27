# carrega as imagens em um dataframe
# retorna o dataframe criado

import os
import pandas as pd
from PIL import Image

def load_images(dataset_path):
    # listas para receber as imagens e rotulos
    # os rotulos são divididos em COVID e non-COVID
    data = []
    labels = []
    
    # nomes das pastas
    categories = ['COVID', 'non-COVID']
    
    # varre as pastas
    for category in categories:
        path = os.path.join(dataset_path, category)
        
        # em cada pasta varre as imagens
        for img_name in os.listdir(path):
            img_path = os.path.join(path, img_name)
            
            try:
                # carrega a imagem na variavel img
                img = Image.open(img_path)                                
                
                # adiciona a imagem e o rotulo as listas
                data.append(img)
                labels.append(category)
                
            except Exception as e:
                print(f"Erro ao carregar imagem {img_path}: {e}")

    # cria o dataframe e retorna
    df = pd.DataFrame({'Image': data, 'Label': labels})        
    return df
        