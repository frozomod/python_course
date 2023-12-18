import cv2 as cv


class FaceDetector:
    def __init__(self, path):
        self.faces = None
        self.image = None
        self.video = None
        self.path = path

    def load_image_or_video(self):
        if self.path.endswith(('.jpg', '.jpeg', '.png')):
            self.image = cv.imread(self.path)
        elif self.path.endswith(('.mp4', '.avi', '.mkv')):
            if self.video is None:
                self.video = cv.VideoCapture(self.path)
            read, self.image = self.video.read()
        else:
            raise ValueError("Unsupported file format. Supported formats: jpg, jpeg, png, mp4, avi, mkv")

    def detect(self):
        face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')
        eyes_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_eye.xml')

        frame_gray = cv.cvtColor(self.image, cv.COLOR_BGR2GRAY)
        frame_gray = cv.equalizeHist(frame_gray)

        self.faces = face_cascade.detectMultiScale(frame_gray)
        for (x, y, w, h) in self.faces:
            center = (x + w // 2, y + h // 2)
            self.image = cv.ellipse(self.image, center, (w // 2, h // 2), 0, 0, 360, (255, 0, 255), 4)
            face_ROI = frame_gray[y:y + h, x:x + w]

            eyes = eyes_cascade.detectMultiScale(face_ROI)
            for (x2, y2, w2, h2) in eyes:
                eye_center = (x + x2 + w2 // 2, y + y2 + h2 // 2)
                radius = int(round((w2 + h2) * 0.25))

                self.image = cv.circle(self.image, eye_center, radius, (255, 0, 0), 4)
                # frame = resizing(frame, 600)

    def infer(self):
        # Ваши операции инференса
        for (x, y, w, h) in self.faces:
            print(f"Face detected at coordinates: x={x}, y={y}, w={w}, h={h}")

    def display(self):
        cv.imshow('Capture - Face detection', self.image)

    def resize_image(self, new_width=None, new_height=None):
        h, w = self.image.shape[:2]

        if new_width is None and new_height is None:
            return self.image

        if new_width is None:
            ratio = new_height / h
            dimension = (int(w * ratio), new_height)

        else:
            ratio = new_width / w
            dimension = (new_width, int(h * ratio))
        self.image = cv.resize(self.image, dimension)
        # return cv.resize(self.image, dimension)


face = FaceDetector('video_1.mp4')
while True:
    face.load_image_or_video()
    face.resize_image(600)
    face.detect()
    face.display()
    face.infer()
    if cv.waitKey(10) == ord('q'):
        break
