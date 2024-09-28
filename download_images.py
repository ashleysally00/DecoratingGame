import requests
import os

# List of image URLs
image_urls = [
    "https://static.wixstatic.com/media/28f7ce_bf9722a172e5411888572a81e594ea70~mv2.png",
    "https://static.wixstatic.com/media/28f7ce_a9becc9f0cb84a36af0188a6d017b1b2~mv2.png",
    "https://static.wixstatic.com/media/28f7ce_1c55289f4b9a4ee8990678be29b59b8f~mv2.png",
    "https://static.wixstatic.com/media/28f7ce_cf57f2e8a75e467492d66dd9d303ef76~mv2.png",
    "https://static.wixstatic.com/media/28f7ce_f6852b2f4da94d35bbf91fb221e4b9d7~mv2.png",
    "https://static.wixstatic.com/media/28f7ce_a3736ac4275949fe8282b9f0d5f89202~mv2.png",
    "https://static.wixstatic.com/media/28f7ce_ce6f2b0fc6fc474c8e2026901ea6e15a~mv2.png",
    "https://static.wixstatic.com/media/28f7ce_fd723c0dc2c14241a7c50927e9f7ac61~mv2.png",
    "https://static.wixstatic.com/media/28f7ce_4cacdecf85f84bfbae5417b5c0335434~mv2.png",
    "https://static.wixstatic.com/media/28f7ce_ccfed2607b814c1b9538fcad84639974~mv2.png",
    "https://static.wixstatic.com/media/28f7ce_fa6000500c734697adc2e728a9d870cb~mv2.png"
]

# Create 'images' directory if it doesn't exist
if not os.path.exists('images'):
    os.makedirs('images')

# Download each image
for i, url in enumerate(image_urls, 1):
    response = requests.get(url)
    if response.status_code == 200:
        filename = f"images/piece_{i}.png"
        with open(filename, 'wb') as file:
            file.write(response.content)
        print(f"Downloaded: {filename}")
    else:
        print(f"Failed to download: {url}")

print("Download complete!")