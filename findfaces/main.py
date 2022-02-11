from Analyzer import Analyzer
from unk_detect import Unknow_Detector
from face_encoder import FaceEncoder
from search_people import load_dbtemp
from api_interaction import API_Interaction as Api
import simplejson as json
from faces import Faces
from rtsp import Rtsp
import cv2

api = Api(active=False)
analyzer = Analyzer()
unk_detec = Unknow_Detector()
encod = FaceEncoder()
fc = Faces()
rt = Rtsp(url='rtsp://<<IP ADDRESS>>:9000/live')

def main():
    dbtemp = load_dbtemp()

    while True:
        detection = {}
        if rt.get_connect_status():
            frame = rt.get_last_frame()
            faces = fc.findfaces(image=frame, recize_factor=30)
            faces = fc.crop_faces(frame, faces)

            detection.update({"find_faces": len(faces['faces'])})

            if len(faces["faces"]) > 0:
                for face in faces['faces']:
                    face1_json = encod.encode_face(face['face'])
                    detection.update({"encoded": False})
                    #detection.update({"encode_face": face1_json})

                    if face1_json != None:
                        detection.update({"encoded": True})
                        face1 = encod.json_to_array(face1_json)
                        people = encod.search_people(face1, dbtemp)

                        print("==> people", people)

                        if people['status'] == 'unknow':
                            detection.update({"detection": False})
                            face_unknow = face1_json
                            unk_detec.set_count()

                        else:
                            infos = analyzer.analyze(face['face'])
                            people.update({"infos": infos})
                            # print("==>time:", dt.now()-hora)
                            # print(json.dumps(infos, indent=4, sort_keys=True))

                            api.send_know_founded(people)
                            unk_detec.resset()

                            face.update({"label": people['alias']})
                            detection.update({"detection": True})
                            detection.update({"alias": people['alias']})
                            detection.update({"distance": people['distance']})
                            detection.update({"infos": infos})
                    else:
                        unk_detec.resset()

            else:
                unk_detec.resset()

            if unk_detec.get_count() >= 10:
                #analisa a face
                # hora = dt.now()
                infos = analyzer.analyze(face['face'])
                # print("==>time:", dt.now()-hora)
                # print(json.dumps(infos, indent=4, sort_keys=True))

                unk_detec.resset()
                face_unknow = json.loads(face_unknow)
                api.send_unknow_founded(face_unknow['face'], json.dumps(infos))
                detection.update({"infos": json.dumps(infos)})

            print(detection)

            #present to check if all is ok
            frame = fc.draw_retangle_faces(frame, faces)
            cv2.imshow('Press "q" to exit', frame)
            if cv2.waitKey(20) & 0xFF == ord('q'):
                break

if __name__ == "__main__":
    main()