import face_recognition
from face_encoder import FaceEncoder
import json

encod = FaceEncoder()

def load_dbtemp():
    #carregando o arquivo DB Temp e criando o Dicionario
    file = open("faces/database_temp.json")
    data_json = json.load(file)
    return data_json

# def search_people(face1, dbtemp):
#     pessoa = {}
#     distances = []
#
#     for people in dbtemp['people']:
#         face2 = encod.json_to_list(people["face"])
#         results = face_recognition.compare_faces(face1, face2, 0.2)[0]
#         distance = face_recognition.face_distance(face1, face2)
#         distance_float = distance.tolist()[0]
#
#         distances.append(distance_float)
#         if pessoa != {}:
#             if pessoa["distance"] > distance_float:
#                 pessoa = people
#                 pessoa.update({"distance": distance_float})
#                 pessoa.update({"result": results})
#         else:
#             pessoa = people
#             pessoa.update({"distance": distance_float})
#             pessoa.update({"result": results})
#
#     if pessoa['distance'] < 0.5:
#         pessoa.update({"status": "know"})
#         return pessoa
#     else:
#         return {"status": "unknow"}