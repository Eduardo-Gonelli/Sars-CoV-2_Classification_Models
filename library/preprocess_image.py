try:
    # Tentar importar a biblioteca
    import cv2
except ImportError:
    # Caso não esteja instalada, instalar a biblioteca
    import pip
    pip.main(['install', 'opencv-python'])
    # Importar após a instalação
    import cv2
import numpy as np

try:
    import numpy as np
except ImportError:
    import pip
    pip.main(['install', 'numpy'])
    import numpy as np

# Função para redimensionar e converter imagem para escala de cinza
def preprocess_image(img, t_size=64):
    t_size = int(t_size) # precisa ser inteiro    
    target_size = (t_size, t_size)  # novo tamanho que a imagem terá
    # Converte para escala de cinza se a imagem for colorida
    if len(img.shape) == 3:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Redimensiona a imagem
    img = cv2.resize(img, target_size)
    return img

# Função que redimensiona a imagem e exclui o canal alpha se tiver
def preprocess_image_tf(img, target_size=(128, 128)):
    # Converte imagem PIL para array numpy
    img = np.array(img)
    # Redimensiona a imagem
    img = cv2.resize(img, target_size)
    # Garantir que a imagem tenha 3 canais
    if img.shape[2] == 4:
        img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
    return img

def random_rotation(image):
    # Gira a imagem em um ângulo aleatório
    angle = np.random.uniform(-10, 10)
    h, w = image.shape[:2]
    M = cv2.getRotationMatrix2D((int(w/2), int(h/2)), angle, 1)
    return cv2.warpAffine(image, M, (w, h))

def random_zoom(image):
    # Aplica um zoom aleatório na imagem
    scale = np.random.uniform(1.2, 1.5)
    h, w = image.shape[:2]
    M = cv2.getRotationMatrix2D((int(w/2), int(h/2)), 0, scale)
    return cv2.warpAffine(image, M, (w, h))

# Função para realizar a inversão horizontal da imagem
def horizontal_flip(image):
    return cv2.flip(image, 1)

# Função para realizar a inversão vertical da imagem
def vertical_flip(image):
    return cv2.flip(image, 0)

# Função para ajustar o brilho e contraste da imagem
def adjust_brightness_contrast(image, alpha=1.0, beta=0.0):
    """
    alpha: Contraste da imagem. Valores > 1 aumentam o contraste, valores entre 0 e 1 diminuem o contraste.
    beta: Brilho da imagem. Valores positivos aumentam o brilho, valores negativos diminuem o brilho.
    """
    return cv2.convertScaleAbs(image, alpha=alpha, beta=beta)