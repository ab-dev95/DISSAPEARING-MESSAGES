from tkinter import *


font = ('Ariel', 12, 'normal')
timer = None

def my_time():
    global counter, timer
    counter -= 1
    canvas.itemconfig(c_txt, text=f'Time Before Text Deletes: {counter}s')
    if counter == 0:
        txt.delete('1.0', 'end')
        return
    
    timer = canvas.after(1000, my_time)

def restart(_):
    global counter, timer
    counter = 6
    if timer is None:
        my_time()
    else:
        canvas.after_cancel(timer)
        my_time()

def save():
    my_text = txt.get('1.0', 'end')
    print(my_text)

root = Tk()
root.title('Disappearing Text Writing App')
root.geometry('500x600')
root.config(pady=10, padx=10)


top_frame = Frame(root, width=500)
middle_frame = Frame(root, width=500)
bottom_frame = Frame(root, width=500)
top_frame.grid()
middle_frame.grid(pady=5)
bottom_frame.grid()


lb = Label(top_frame, font=font, text='This app deletes what you have written\nif you do not type anything after 5 seconds')
lb.grid(row=0, column=0)

canvas = Canvas(top_frame, width=480, height=30)
c_txt = canvas.create_text(240,15, text='Time Before Text Deletes: 5s', font=font, fill='red')
canvas.grid(row=1, column=0, pady=2)

txt = Text(middle_frame, font=font, width=53)
txt.grid()

btn = Button(bottom_frame, text='Save Text', bg='blue', fg='white', font=font, command=save)
btn.grid(pady=5)


txt.bind('<Any-KeyPress>', restart)
root.mainloop()
