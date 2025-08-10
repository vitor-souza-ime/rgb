import requests
from PIL import Image
from io import BytesIO
import matplotlib.pyplot as plt
import numpy as np

def baixar_imagem(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/114.0.0.0 Safari/537.36"
    }
    resp = requests.get(url, headers=headers)
    resp.raise_for_status()
    return Image.open(BytesIO(resp.content)).convert("RGB")

urls = [
    "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c4/Escola_de_Atenas_-_Vaticano_2.jpg/500px-Escola_de_Atenas_-_Vaticano_2.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/1665_Girl_with_a_Pearl_Earring.jpg/800px-1665_Girl_with_a_Pearl_Earring.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/d/df/Fran%C3%A7ois_Boucher_-_Jeanne-Antoinette_Poisson%2C_Marquise_de_Pompadour_-_1966.47_-_Fogg_Museum.jpg/960px-Fran%C3%A7ois_Boucher_-_Jeanne-Antoinette_Poisson%2C_Marquise_de_Pompadour_-_1966.47_-_Fogg_Museum.jpg"
]

nomes = ["A Escola de Atenas — Rafael (1509–1511) - Renascimento", 
         "A Moça com o Brinco de Pérola — Johannes Vermeer (1665) - Barroco Holandês", 
         "Retrato de Madame de Pompadour — François Boucher (c. 1756) - Rococó"]

fig, axs = plt.subplots(len(urls), 1, figsize=(12, 4 * len(urls)))

if not isinstance(axs, (list, np.ndarray)):
    axs = [axs]

for i, url in enumerate(urls):
    img = baixar_imagem(url)
    hist = img.histogram()

    hist_r = hist[0:256]
    hist_g = hist[256:512]
    hist_b = hist[512:768]

    axs[i].plot(hist_r, color='red', label='Vermelho')
    axs[i].plot(hist_g, color='green', label='Verde')
    axs[i].plot(hist_b, color='blue', label='Azul')
    axs[i].set_title(f"Histograma RGB - {nomes[i]}")
    axs[i].set_xlabel("Intensidade de cor")
    axs[i].set_ylabel("Número de pixels")
    axs[i].legend()

plt.tight_layout()
plt.show()
