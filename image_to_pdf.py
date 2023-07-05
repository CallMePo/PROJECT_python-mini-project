from PIL import Image
def Images_Pdf(filename, output):
    images=[]

    for file in filename:
        im = Image.open(file)
        im = im.convert('RGB')
        images.append(im)

        images[0].save(output, save_all=True, append_image=images[1:1])
Images_Pdf(["assets\img\shafaadimitri~3014050740008989089_3553619532.jpg"],"output.pdf")