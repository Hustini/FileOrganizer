import tkinter as tk
from PIL import Image, ImageTk
import shutil
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


def selected(path, selected_items, select_btn):
    selected_items.append(path)
    select_btn.config(bg='light blue')


def move_files(goal_path, selected_items):
    print(goal_path)
    print(selected_items)
    for item in selected_items:
        shutil.move(item, goal_path)


def main():
    root = tk.Tk()
    root.title('FileOrganizer')
    root.resizable(False, False)

    items = os.listdir(path_origin_folder)

    file_img, folder_img = images()

    selected_items = []
    row = 0
    col = 0
    for i in range(len(items)):
        item_path = os.path.join(path_origin_folder, items[i])
        if os.path.isdir(item_path):
            image_to_show = folder_img
        elif os.path.isfile(item_path):
            image_to_show = file_img

        button = tk.Button(root, image=image_to_show, bd=0)
        button.config(command=lambda path=item_path, btn=button: selected(path, selected_items, btn))
        button.grid(row=row, column=col, padx=5, pady=5)

        if col < 4:
            col += 1
        else:
            col = 0
            row += 1

    entry = tk.Entry(root, width=100)
    entry.grid(row=row + 1, column=0, columnspan=5, padx=5, pady=5)

    submit_btn = tk.Button(root, text='Submit', command=lambda: move_files(entry.get(), selected_items))
    submit_btn.grid(row=row + 2, column=0, columnspan=5, padx=5, pady=5)

    root.mainloop()


if __name__ == '__main__':
    main()
