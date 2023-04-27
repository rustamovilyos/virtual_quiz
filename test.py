# # import pickle
# #
# #
# # with open('working/ref_name.pkl', 'rb') as f:
# #     data = pickle.load(f)
# #     print(data)
# #
# # with open('working/ref_embed.pkl', 'rb') as f:
# #     data = pickle.load(f)
# #     print(data)
#
# from tkinter import *
# import cv2
#
# # Define a video capture object
# vid = cv2.VideoCapture(0)
#
# # Declare the width and height in variables
# width, height = 800, 600
#
# # Set the width and height
# vid.set(cv2.CAP_PROP_FRAME_WIDTH, width)
# vid.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
#
# # Create a GUI app
# app = Tk()
#
# # Bind the app with Escape keyboard to
# # quit app whenever pressed
# app.bind('<Escape>', lambda e: app.quit())
#
# # Create a label and display it on app
# label_widget = Label(app)
# label_widget.pack()
#
#
# # Create a function to open camera and
# # display it in the label_widget on app
#
#
# def open_camera():
#     from working.auth import recognition
#     recognition
#     # # Capture the video frame by frame
#     # _, frame = vid.read()
#     #
#     # # Convert image from one color space to other
#     # opencv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
#     #
#     # # Capture the latest frame and transform to image
#     # captured_image = Image.fromarray(opencv_image)
#     #
#     # # Convert captured image to photoimage
#     # photo_image = ImageTk.PhotoImage(image=captured_image)
#     #
#     # # Displaying photoimage in the label
#     # label_widget.photo_image = photo_image
#     #
#     # # Configure image in the label
#     # label_widget.configure(image=photo_image)
#     #
#     # # Repeat the same process after every 10 seconds
#     # label_widget.after(10, open_camera)
#
#
# # Create a button to open the camera in GUI app
# button1 = Button(app, text="Open Camera", command=open_camera)
# button1.pack()
#
# # Create an infinite loop for displaying app on screen
# app.mainloop()

# def seidel(A, b, x0, tol=1e-8, max_iter=100):
#     """
#     Решает систему линейных уравнений Ax = b методом Зейделя.
#
#     :param A: матрица системы уравнений
#     :param b: вектор свободных членов
#     :param x0: начальное приближение
#     :param tol: допустимая погрешность
#     :param max_iter: максимальное число итераций
#     :return: решение системы уравнений x
#     """
#
#     n = len(A)
#     x = x0.copy()
#
#     for k in range(max_iter):
#         x_old = x.copy()
#
#         for i in range(n):
#             s = sum(A[i][j] * x[j] for j in range(i))
#             s += sum(A[i][j] * x_old[j] for j in range(i + 1, n))
#             x[i] = (b[i] - s) / A[i][i]
#
#         if all(abs(x[i] - x_old[i]) < tol for i in range(n)):
#             return x
#
#     raise ValueError("Решение не сошлось за заданное число итераций.")
#
#
# A = [[4, 1, 1], [2, 7, 1], [1, 2, 6]]
# b = [4, 9, 9]
# x0 = [0, 0, 0]
#
# x = seidel(A, b, x0)
#
# print(x)  # Выводит решение системы уравнений


