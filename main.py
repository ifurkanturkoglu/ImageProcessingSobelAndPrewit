from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog as fd, ttk
from Edge_detection import *  # ????

master = Tk()
canvas = Canvas(master, height=600, width=750)
canvas.pack()

frame_image = Frame(master, bg="wheat")
frame_image.place(relx=0.05, rely=0.05, relwidth=0.75, relheight=0.75)



def alg_parametres(img, threshold, algorihtm):

    if threshold=="\n":
        threshold=30
    else:
        threshold=int(threshold)
    global Edge
    Edge = edge_detection(img, threshold, algorihtm)

    if (algorihtm == "sobel"):
        Edge.sobel()

        Gx_view()
        Gy_view()
        Gsiddets_view()

    if (algorihtm == "prewitt"):
        Edge.prewitt()

        Gx_view()
        Gy_view()
        Gsiddets_view()

def select_file():
    global img
    global Copy_image
    filetypes = (
        ('image files', '.jpg'),
        ('All files', '.*')
    )

    Selected_image = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)

    img = ImageTk.PhotoImage(Image.open(Selected_image).resize((170, 170)))
    Copy_image=Image.open(Selected_image).resize((170, 170))
    org_img = Label(frame_image, image=img)
    org_img.place(relx=0.07, rely=0.07)


def Gx_view():
    global img2
    img2 = ImageTk.PhotoImage(Edge.gx_image)

    Gx = Label(frame_image, text="2", image=img2)
    Gx.place(relx=0.93, rely=0.07, anchor='ne')

def Gy_view():
    global img3
    img3 = ImageTk.PhotoImage(Edge.gy_image)

    Gy = Label(frame_image, image=img3)
    Gy.place(relx=0.07, rely=0.93, anchor='sw')

def Gsiddets_view():
    global img4
    img4 = ImageTk.PhotoImage(Edge.gsiddet_image)

    Gsiddet = Label(frame_image, image=img4)
    Gsiddet.place(relx=0.93, rely=0.93, anchor='se')


# Load button
Load_button = ttk.Button(master, text='Load File', command=select_file)
Load_button.pack(expand=True)
Load_button.place(relx=0.07, rely=0.93, anchor='sw')

# Treshold
Trs = Text(master, bg="antiquewhite2", height=1, width="6")
Trs.pack()
Trs.place(relx=0.35, rely=0.91, anchor='e')

# algorihtm
menu_opsion = StringVar(master)
menu_opsion.set("\t")
menu = OptionMenu(master, menu_opsion, "sobel", "prewitt")
menu.pack()
menu.place(relx=0.93, rely=0.07, anchor="e")



aply_button = ttk.Button(master, text='aply',command=lambda: alg_parametres(Copy_image, Trs.get("1.0",END), menu_opsion.get()))
aply_button.pack()
aply_button.place(relx=0.83, rely=0.93, anchor='sw')

master.mainloop()
