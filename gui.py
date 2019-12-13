import time
import tkinter as tk


def draw_grid(path):
    root = tk.Tk()

    c = tk.Canvas(root, height=1000, width=1000, bg='white')
    c.pack(fill=tk.BOTH, expand=True)

    di = 15
    stx = 55
    sty = 45

    def draw(board):
        for i in range(0, 8):
            for j in range(0, 8):
                if board[i][j]:
                    x = (j * 125) + stx
                    y = (i * 105) + sty
                    c.create_oval(x, y, x + di, y + di, fill='red')

    def create_grid(event):
        w = c.winfo_width()
        h = c.winfo_height()
        c.delete('grid_line')

        # Creates all vertical lines at intevals of 100
        for i in range(0, w, 125):
            c.create_line([(i, 0), (i, h)], tag='grid_line')

        # Creates all horizontal lines at intevals of 100
        for i in range(0, h, 105):
            c.create_line([(0, i), (w, i)], tag='grid_line')

    c.bind('<Configure>', create_grid)
    for board in path:
        c.delete('all')
        create_grid(None)
        draw(board)
        root.update()
        time.sleep(1)

    time.sleep(5)
    root.quit()

