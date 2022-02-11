#Encode and Decode Faces to Json
import face_recognition, json, os
import numpy as np
from datetime import datetime as dt

class FaceEncoder:
    def __init__(self):
        pass

    def encode_face(self, face):
        know = face_recognition.face_encodings(face)
        if len(know) > 0:
            know = know[0]
            facelist = know.tolist()
            face = {"face": facelist}
            return json.dumps(face)
        return None


    def face_to_json(self, face_image_path, index=0):
        start = dt.now()
        #load image
        image = face_recognition.load_image_file(face_image_path)

        # Get 128-dimension face encoding
        # Always returns a list of found faces, for this purpose we take first face only (assuming one face per image as you can't be twice on one image)
        know = face_recognition.face_encodings(image)[0]

        #transform the array image to a list
        facelist = know.tolist()

        #tranform to a json to be saved
        json_face = json.dumps(facelist)

        spent = dt.now()- start

        #creates the json
        my_json = {
            "index": index,
            "face": json_face,
            "time_spent": str(spent)
        }
        #print(json.dumps(my_json, indent=4, sort_keys=True))
        return my_json


    def encode_faces_directory(self, directory_path, version = 1.0):
        start = dt.now()
        index = 0
        faces ={
            "Version":version,
            "Creation_Date": str(dt.now().isoformat()),
            "Num_of_Faces": 0,
            "File_Erros":[],
            "List_of_Faces":[],
            "Time_Elapsed": ""
        }
        file_errors = []
        list_of_faces = []
        for face in os.listdir(directory_path):
            if face[0] != '.':
                try:
                    jsonface = self.face_to_json(f'{directory_path}/{face}', index=index)
                    jsonface.update({"filename": face})
                    list_of_faces.append(jsonface)
                    index += 1
                except:
                    file_errors.append(face)
                    print(f'Error in face:{face}')
        faces["File_Erros"] = file_errors
        faces["List_of_Faces"] = list_of_faces
        faces["Time_Elapsed"] = str(dt.now()-start)
        faces["Num_of_Faces"] = len(list_of_faces)

        try:
            with open('faces.json', 'w') as outfile:
                json.dump(faces, outfile, ensure_ascii=False, indent=4)
        except:
            print('Error to save file .json')

        print(f'file errors: {file_errors}')
        print(f'total time elapsed: {dt.now()-start}')
        return True

    #face_json should be a Json with a key "face" to be read
    def json_to_array(self, face_json):
        face_json = json.loads(face_json)
        face_j = face_json["face"]
        myarray = np.array(face_j)
        return myarray

    #face_json should be a Json with a key "face" to be read
    def json_to_list(self, face_json):
        list = []
        #face_json = json.loads(face_json)
        #mylist = face_json["face"]
        #list.append(np.array(mylist))
        list.append(np.array(face_json))
        return list

    def search_people(self, face1, dbtemp):
        pessoa = {}
        distances = []

        for people in dbtemp['people']:
            face2 = self.json_to_list(people["face"])
            distance = face_recognition.face_distance(face1, face2)
            distance_float = distance.tolist()[0]

            distances.append(distance_float)
            if pessoa != {}:
                if pessoa["distance"] > distance_float:
                    pessoa = people
                    pessoa.update({"distance": distance_float})
            else:
                pessoa = people
                pessoa.update({"distance": distance_float})

        if pessoa['distance'] < 0.5:
            pessoa.update({"status": "know"})
            return pessoa
        else:
            return {"status": "unknow"}