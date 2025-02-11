from flask import Flask, request, jsonify
import pickle
import pandas as pd
from model_loader import find_similar_players  # 함수 가져오기

app = Flask(__name__)

# 데이터 불러오기
df = pd.read_csv('../data/player_data.csv')

# 모델 불러오기
with open('../models/knn_model.pkl', 'rb') as f:
    knn_model = pickle.load(f)

with open('../models/label_encoder.pkl', 'rb') as f:
    le = pickle.load(f)

@app.route('/find_players', methods=['POST'])
def get_similar_players():
    """
    프론트엔드에서 전달한 포지션과 키(height)를 받아 유사한 선수 5명을 반환하는 API.
    """
    data = request.json
    position = data.get('position')
    height = data.get('height')

    if not position or not height:
        return jsonify({'error': 'position과 height 값을 입력하세요'}), 400

    try:
        # 유사한 선수 찾기
        similar_players = find_similar_players(position, float(height), knn_model, df, le)
        return jsonify({'similar_players': similar_players.tolist()})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
