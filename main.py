import tkinter as tk
from PIL import Image, ImageTk
import os

path_origin_folder = 'C:/Users/ejder/OneDrive - Bildungszentrum Zürichsee/Desktop/FileOrganizer'

def main():
    root = tk.Tk()
    root.title('FileOrganizer')
    root.resizable(False, False)

    items = os.listdir(path_origin_folder)
    print(items)

    # Load the image using Pillow
    image = Image.open('img/file.png')

    # Resize the image (width, height)
    resized_image = image.resize((100, 100))

    # Convert the resized image to PhotoImage to use with Tkinter
    tk_image = ImageTk.PhotoImage(resized_image)

    # Load the image using Pillow
    image2 = Image.open('img/folder.png')

    # Resize the image (width, height)
    resized_image2 = image2.resize((100, 100))

    # Convert the resized image to PhotoImage to use with Tkinter
    tk_image2 = ImageTk.PhotoImage(resized_image2)

    row = 0
    col = 0
    for i in range(len(items)):
        if os.path.isdir(os.path.join(path_origin_folder, items[i])):
            tk.Label(root, image=tk_image2).grid(row=row, column=col)
        elif os.path.isfile(os.path.join(path_origin_folder, items[i])):
            tk.Label(root, image=tk_image).grid(row=row, column=col)
        if col < 4:
            col += 1
        else:
            col = 0
            row += 1

    root.mainloop()


if __name__ == '__main__':
    main()
