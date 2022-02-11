import cv2
from threading import Thread
class Rtsp:
    def __init__(self, url):
        self.url = url
        self.last_image = None
        self.thread = Thread(target=self.capture, args=())
        self.thread.daemon = True
        self.thread.start()
        self.connected = False
        pass

    def capture(self):
        print(f'==> Try Connect to: {self.url}')
        try:
            cap = cv2.VideoCapture(self.url)
        except:
            self.connected = False
            print('==> Error to Connect')
            exit(0)
        print(f'==> Connected')

        print('==> Capture Started')
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                while not ret:
                    ret, frame = cap.read()
            #if not ret:
            #     continue
            self.last_image = frame
            self.connected = True
        self.connected = False
        print('==> Capture Stoped')

    def get_last_frame(self):
        return self.last_image

    def get_connect_status(self):
        return self.connected

    def save_capture(self):
        pass
