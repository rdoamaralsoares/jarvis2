import face_recognition
import cv2
from datetime import datetime as dt

class Faces:
    def __init__(self):
        pass

    def findfaces(self, image, recize_factor=100):

        response = {}
        # Find all the faces in the image using the default HOG-based model.
        # This method is fairly accurate, but not as accurate as the CNN model and not GPU accelerated.
        # See also: find_faces_in_picture_cnn.py

        image = self.recize_image(image, recize_factor)

        start = dt.now()
        face_locations = face_recognition.face_locations(image)
        elapsed = str(dt.now()-start)
        response.update({"time_elapsed": elapsed})
        myfaces = []

        for face in face_locations:
            x0 = int(face[1]*(100/recize_factor))
            y0 = int(face[0]*(100/recize_factor))
            x1 = int(face[3]*(100/recize_factor))
            y1 = int(face[2]*(100/recize_factor))

            midle = (int((x0+x1)/2), int((y0+y1)/2))
            coord = (x1, y0, x0, y1)
            person = {"coordinates": coord, "midle_point": midle, "label":"unknow"}
            myfaces.append(person)
        response.update({"faces": myfaces})

        return response

    def recize_image(self, image, scale_percent=100):
        width = int(image.shape[1] * scale_percent / 100)
        height = int(image.shape[0] * scale_percent / 100)
        dim = (width, height)
        # resize image
        resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)

        return resized

    def crop_faces(self, image, list_of_faces):
        faceslist = []
        for face in list_of_faces['faces']:
            (x, y, w, h) = face['coordinates']
            img = image[y:h, x:w]
            faceslist.append(img)
            face.update({"face": img})
        #return list_of_faces, faceslist
        return list_of_faces

    def draw_retangle_faces(self, image, faces):
        for face in faces['faces']:
            (x, y, w, h) = face['coordinates']
            cv2.rectangle(image, (x, y), (w, h), (0, 0, 255), 2)
            cv2.circle(image, face['midle_point'], 5, (0, 0, 255), 5)
            cv2.putText(image, face['label'], (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
        return image

    def encode_face(self, faces):
        pass