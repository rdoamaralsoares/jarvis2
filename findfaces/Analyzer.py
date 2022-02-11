from deepface import DeepFace

class Analyzer:
    def __init__(self):
        pass

    def analyze(self, img):
        analysis = DeepFace.analyze(img, actions=["age", "gender", "emotion"], enforce_detection=False)
        analysis.pop("region", None)
        return analysis

    def analyze_all(self, img):
        analysis = DeepFace.analyze(img, actions=["age", "gender", "emotion", "race"], enforce_detection=False)
        return analysis

    def analyze_age(self, img):
        analysis = DeepFace.analyze(img, actions=["age"], enforce_detection=False)
        return analysis

    def analyze_gender(self, img):
        analysis = DeepFace.analyze(img, actions=["gender"], enforce_detection=False)
        return analysis

    def analyze_emotion(self, img):
        analysis = DeepFace.analyze(img, actions=["emotion"], enforce_detection=False)
        return analysis

    def analyze_race(self, img):
        analysis = DeepFace.analyze(img, actions=["race"], enforce_detection=False)
        return analysis
