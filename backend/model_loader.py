import pickle

def save_model(knn_model, le):
    """ 모델과 라벨 인코더를 파일로 저장하는 함수 """
    with open("../models/knn_model.pkl", "wb") as f:
        pickle.dump(knn_model, f)

    with open("../models/label_encoder.pkl", "wb") as f:
        pickle.dump(le, f)

def load_model():
    """ 저장된 모델과 라벨 인코더를 로드하는 함수 """
    with open("../models/knn_model.pkl", "rb") as f:
        knn_model = pickle.load(f)

    with open("../models/label_encoder.pkl", "rb") as f:
        le = pickle.load(f)

    return knn_model, le
