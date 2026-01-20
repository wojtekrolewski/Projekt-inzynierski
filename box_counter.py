import cv2
from tkinter import Tk, filedialog, Scale, IntVar, Button, Label, Entry
from math import log
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from sklearn.linear_model import LinearRegression

image_properties = []

def choose_image():
    root = Tk()
    root.withdraw()  # Ukrywa główne okno

    file_path = filedialog.askopenfilename(title="Choose an image file", filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp")])

    if file_path:
        read_image(file_path)
        create_interface()

def read_image(file_path):
    global image
    image = cv2.imread(file_path)

    image_height, image_width, _ = image.shape

    image_properties.append(image)
    image_properties.append(image_height)
    image_properties.append(image_width)

def preprocess_image(box_size, threshold, reverse):
    global image

    enclose_count = 0
    temp_image = image.copy()

    for h in range(int(image_height + 1 / box_size)):
        for w in range(int(image_width / box_size + 1)):
            cv2.rectangle(temp_image, (box_size * w, box_size * h), (box_size + box_size * w, 1 + box_size + box_size * h),
                          color=(0, 0, 255), thickness=1)

            selection = temp_image[box_size * h:1 + box_size + box_size * h, box_size * w:box_size + box_size * w, 1]
            try:
                blue_mean = selection.mean()
            except RuntimeWarning:
                blue_mean = 0

            # Zmiana znaku w warunku w zależności od wartości reverse
            if (blue_mean >= threshold) if reverse else (blue_mean <= threshold):
                cv2.rectangle(temp_image, (box_size * w, box_size * h), (box_size + box_size * w, 1 + box_size + box_size * h),
                              color=(0, 0, 125), thickness=-1)
                enclose_count += 1

    return temp_image, enclose_count

def update_image(box_size, threshold, reverse):
    global pudelek_label, minkowski_label, plot_frame
    temp_image, enclose_count = preprocess_image(box_size, threshold, reverse)

    # Aktualizacja etykiet w interfejsie
    pudelek_label.config(text=f"Liczba pudełek: {enclose_count}")

    # Unikaj logarytmowania wartości mniejszych lub równych zeru
    if box_size > 0 and enclose_count > 0:
        plot_frame.add_point(log(1/box_size), log(enclose_count))

    cv2.imshow("Gridded Image", temp_image)

def switch_sign():
    global reverse_sign, plot_frame
    reverse_sign = not reverse_sign
    plot_frame.clear_plot()
    update_image(int(box_size_label.get()), int(threshold_var.get()), reverse_sign)

def draw_regression_line():
    global plot_frame, slope_entry
    plot_frame.clear_regression_line()
    plot_frame.draw_regression_line()

    # Obliczanie i wyświetlanie wymiaru pudełkowego
    if len(plot_frame.points_x) >= 2:
        X, Y = zip(*zip(plot_frame.points_x, plot_frame.points_y))
        X = np.array(X).reshape(-1, 1)
        Y = np.array(Y)

        model = LinearRegression()
        model.fit(X, Y)

        slope = model.coef_[0]
        slope_entry.delete(0, 'end')
        slope_entry.insert(0, f"{slope:.5f}")

class PlotFrame:
    def __init__(self, root):
        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.figure, master=root)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.pack()
        self.points_x = []
        self.points_y = []
        self.regression_line = None

    def add_point(self, x, y):
        self.points_x.append(x)
        self.points_y.append(y)
        self.update_plot()

    def clear_plot(self):
        self.points_x = []
        self.points_y = []
        self.clear_regression_line()
        self.update_plot()

    def clear_regression_line(self):
        if self.regression_line:
            self.regression_line.remove()
            self.regression_line = None

    def draw_regression_line(self):
        if len(self.points_x) >= 2:
            X, Y = zip(*zip(self.points_x, self.points_y))
            X = np.array(X).reshape(-1, 1)
            Y = np.array(Y)

            model = LinearRegression()
            model.fit(X, Y)

            X_fit = np.linspace(min(X), max(X), 100).reshape(-1, 1)
            Y_fit = model.predict(X_fit)

            self.regression_line, = self.ax.plot(X_fit, Y_fit, color='red', label='Regression Line')
            self.ax.legend()
            self.canvas.draw()

    def update_plot(self):
        self.ax.clear()
        self.ax.plot(self.points_x, self.points_y, marker='o', linestyle='None', color='b')
        self.ax.set(xlabel='log(1/δ)', ylabel='log(N_δ(F))',
                    title='Fractal Dimension Estimation')
        self.ax.grid()
        self.canvas.draw()

def clear_plot():
    global plot_frame
    plot_frame.clear_plot()

def create_interface():
    global image_height, image_width, image, reverse_sign, pudelek_label, box_size_label, threshold_var, slope_entry, plot_frame

    image_height = image_properties[1]
    image_width = image_properties[2]
    reverse_sign = False  # Flaga do zmiany znaku w warunku

    root = Tk()
    root.title("Parameter Adjustment")

    box_size_label = Scale(root, label="Box Size", from_=3, to=50, orient="horizontal", length=200, command=lambda x: update_image(int(x), int(threshold_var.get()), reverse_sign))
    box_size_label.set(7)
    box_size_label.pack()

    threshold_var = IntVar()
    threshold_label = Scale(root, label="Threshold", from_=0, to=255, orient="horizontal", length=200, variable=threshold_var, command=lambda x: update_image(int(box_size_label.get()), int(x), reverse_sign))
    threshold_label.set(100)
    threshold_label.pack()

    switch_button = Button(root, text="Switch Sign", command=switch_sign)
    switch_button.pack()

    pudelek_label = Label(root, text="Liczba pudełek: ")
    pudelek_label.pack()

    plot_frame = PlotFrame(root)

    slope_label = Label(root, text="Wymiar pudełkowy:")
    slope_label.pack()

    slope_entry = Entry(root)
    slope_entry.pack()

    draw_regression_button = Button(root, text="Draw Regression Line", command=draw_regression_line)
    draw_regression_button.pack()

    clear_plot_button = Button(root, text="Clear Plot", command=clear_plot)
    clear_plot_button.pack()

    update_image(int(box_size_label.get()), int(threshold_var.get()), reverse_sign)

    root.mainloop()

if __name__ == "__main__":
    choose_image()
