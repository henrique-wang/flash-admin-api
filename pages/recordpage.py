import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image
from PIL import ImageTk
import imutils
from imutils.video import VideoStream
import threading
import cv2
import os

LARGEFONT = ("Verdana", 35)
MEDIUMFONT = ("Verdana", 20)

class RecordPage(tk.Frame):

    def __init__(self, parent, controller):
        PICAMERA = False
        self.controller = controller
        self.videox = 0.25
        self.videoy = 0.25
        self.vs = VideoStream(usePiCamera=PICAMERA).start()
        self.outputPath = r'pages\photos'
        self.frame = None
        self.thread = None
        self.stopEvent = None
        self.record = False
        # initialize the root window and image panel
        self.root = parent
        self.panel = None
        self.panelCalibrate = None
        self.button_record = None
        self.button_stop = None
        self.button_send = None
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Após posicionar a bandeja na região delimitada, selecione 'Calibrate' para iniciar a calibração",
                          font=MEDIUMFONT)
        label.place(relx=0.5, rely=0.1, anchor='center')

        self.labelAction = tk.Label(self, text="",
                          font=MEDIUMFONT, fg = 'red')
        self.labelAction.place(relx=0.75, rely=0.3, anchor='center')

        self.labelAction = tk.Label(self, text=controller.product.__str__(),
                                    font=MEDIUMFONT, fg='black')
        self.labelAction.place(relx=0.75, rely=0.5, anchor='center')

        # button to start calibrating
        # layout2
        self.button_calibrate = tk.Button(self, text="Calibrate", bg='blue', fg='white',
                                  command=lambda: self.calibrate(controller))
        self.button_calibrate.place(relx=0.89, rely=0.8, anchor='se')

        # button to cancel
        # layout2
        button_cancel = tk.Button(self, text="Cancel",
                                  command=lambda: self.cancel_shop(controller), bg='red', fg='white')
        button_cancel.place(relx=0.9, rely=0.85, anchor='se')

        self.stopEvent = threading.Event()
        self.thread = threading.Thread(target=self.videoLoop, args=())
        self.thread.start()

    def cancel_shop(self, controller):
        cancel = messagebox.askokcancel(title=None, message="Você realmente deseja cancelar o envio do vídeo?")
        if cancel == True:
            if self.panelCalibrate != None:
                self.panelCalibrate.destroy()
            self.onClose(controller)
            controller.show_frame("HomePage")

    def videoLoop(self):
        try:
            count = 0
            # keep looping over frames until we are instructed to stop
            while not self.stopEvent.is_set():
                # grab the frame from the video stream and resize it to
                # have a maximum width of 300 pixels
                self.frame = self.vs.read()
                self.frame = imutils.resize(self.frame, width=500)

                # OpenCV represents images in BGR order; however PIL
                # represents images in RGB order, so we need to swap
                # the channels, then convert to PIL and ImageTk format
                image = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
                image = Image.fromarray(image)
                image = ImageTk.PhotoImage(image)

                # Capture Frame if record = true
                if self.record == True:
                    if count%10 == 0:
                        cv2.imwrite(r"pages\record\frame{}.jpg".format(count), self.frame.copy())
                    count += 1
                # if the panel is not None, we need to initialize it
                if self.panel is None:
                    self.panel = tk.Label(image=image)
                    self.panel.image = image
                    self.panel.place(relx=self.videox, rely=0.25, anchor='n')

                # otherwise, simply update the panel
                else:
                    self.panel.configure(image=image)
                    self.panel.image = image
        except RuntimeError as e:
            print("[INFO] caught a RuntimeError")

    def onClose(self, controller):
        self.record = False
        print("[INFO] closing...")
        self.stopEvent.set()
        self.vs.stop()
        self.panel.destroy()
        if self.button_stop != None:
            self.button_stop.destroy()

        self.labelAction.destroy()
        self.labelAction = tk.Label(self, text="Video has been recorded",
                                    font=MEDIUMFONT, bg='red')
        self.labelAction.place(relx=0.75, rely=0.3, anchor='center')

        self.button_send = tk.Button(self, text="Send Video", bg='blue', fg='white',
                                     command=lambda: self.send_video(controller))
        self.button_send.place(relx=0.89, rely=0.8, anchor='se')

    def record_video(self, controller):
        # AQUI VAI FUNCAO DE GRAVAR E ENVIAR VIDEO
        print("recording")
        self.record = True
        self.labelAction.destroy()
        self.labelAction = tk.Label(self, text="Recording",
                                     font=MEDIUMFONT, bg='red')
        self.labelAction.place(relx=0.75, rely=0.2, anchor='center')

        self.button_record.destroy()

        self.button_stop = tk.Button(self, text="Stop", bg='blue', fg='white',
                                  command=lambda: self.onClose(controller))
        self.button_stop.place(relx=0.89, rely=0.8, anchor='se')


        # when its over:
        #self.labelAction.destroy()
        #self.labelAction = ttk.Label(self, text="Video sent",
        #                             font=MEDIUMFONT, bg='red')
        #self.labelAction.place(relx=0.75, rely=0.3, anchor='center')

    def calibrate(self, controller):
        # AQUI VAI FUNCAO DE CALIBRACAO
        self.videox = 0.6
        print("calibrating")
        self.labelAction.destroy()
        self.labelAction = tk.Label(self, text="Calibrating",
                                     font=MEDIUMFONT, bg='red')
        self.labelAction.place(relx=0.75, rely=0.3, anchor='center')
        self.videox = 0.75
        self.panel.place(relx=self.videox, rely=0.25, anchor='n')
        filename = "{}.jpg".format("Calibrate")
        p = os.path.sep.join((self.outputPath, filename))
        # save the file
        cv2.imwrite(p, self.frame.copy())
        # read photo
        image = cv2.imread(r"pages\photos\Calibrate.jpg")
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(image)
        [imageSizeWidth, imageSizeHeight] = image.size
        image = image.resize((imageSizeWidth, imageSizeHeight))
        image = ImageTk.PhotoImage(image)
        # put on view
        self.panelCalibrate = tk.Label(image=image)
        self.panelCalibrate.image = image
        self.panelCalibrate.place(relx=0.1, rely=0.25)


        # when its over:
        # self.labelAction.destroy()
        # self.labelAction = ttk.Label(self, text="Calibration has ended. Please start to record,",
        #                             font=MEDIUMFONT, bg='red')
        # self.labelAction.place(relx=0.75, rely=0.3, anchor='center')
        # button to record
        # layout2
        self.button_calibrate.destroy()
        # Enable record button
        self.button_record = tk.Button(self, text="Record", bg='blue', fg='white',
                                  command=lambda: self.record_video(controller))
        self.button_record.place(relx=0.89, rely=0.8, anchor='se')

    # third window frame page2

    def send_video(self, controller):
        ok = messagebox.showinfo("Message", "Video sent!")
        self.panelCalibrate.destroy()
        controller.show_frame("HomePage")