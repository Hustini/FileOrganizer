import tkinter as tk
from PIL import Image, ImageTk
import os

path_origin_folder = 'C:/Users/ejder/OneDrive - Bildungszentrum Zürichsee/Desktop/FileOrganizer'

def images():
    """
    # Load the image using Pillow
    # Resize the image (width, height)
    # Convert the resized image to PhotoImage to use with Tkinter
    :return: file_img, folder_img
    """
    image = Image.open('img/file.png')
    resized_image = image.resize((100, 100))
    file_img = ImageTk.PhotoImage(resized_image)

    image2 = Image.open('img/folder.png')
    resized_image2 = image2.resize((100, 100))
    folder_img = ImageTk.PhotoImage(resized_image2)
    return file_img, folder_img


def button_clicked():
    pass


def main():
    root = tk.Tk()
    root.title('FileOrganizer')
    root.resizable(False, False)

    items = os.listdir(path_origin_folder)

    file_img, folder_img = images()

    row = 0
    col = 0
    for i in range(len(items)):
        item_path = os.path.join(path_origin_folder, items[i])
        if os.path.isdir(item_path):
            image_to_show = folder_img
        elif os.path.isfile(item_path):
            image_to_show = file_img

        button = tk.Button(root, image=image_to_show, bd=0)
        button.grid(row=row, column=col)

        if col < 4:
            col += 1
        else:
            col = 0
            row += 1

    root.mainloop()


if __name__ == '__main__':
    main()
