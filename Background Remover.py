from rembg import remove
from PIL import Image

input_path='assets\img\Desain tanpa judul.jpg'
output_path='a.png'
inp= Image.open(input_path)
output=remove(inp)
output.save(output_path)