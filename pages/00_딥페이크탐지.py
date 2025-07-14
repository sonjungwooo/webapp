# ---------------------------
# 1. 모델 정의 (model.py) - 라이브러리 없이 대체 버전
# ---------------------------
def load_dummy_model():
    # 실제 모델 대신 간이 점수 계산을 위한 더미 함수 반환
    return lambda face: 0.5  # 모든 얼굴에 대해 50% 딥페이크 확률 반환


# ---------------------------
# 2. 얼굴 추출 함수 (preprocessing.py) - 라이브러리 없이 대체 버전
# ---------------------------
def extract_dummy_faces(video_path, max_frames=5):
    # 외부 라이브러리 없이 동작하는 더미 얼굴 추출 함수
    return [f"face_{i}" for i in range(max_frames)]


# ---------------------------
# 3. 딥페이크 탐지 함수 (detector.py) - 라이브러리 없이 대체 버전
# ---------------------------
from model import load_dummy_model
from preprocessing import extract_dummy_faces
import random

def deepfake_detection(video_path, model_weights=None):
    print("[INFO] 간이 얼굴 추출 중...")
    faces = extract_dummy_faces(video_path)
    if not faces:
        print("[ERROR] 얼굴 없음")
        return None

    model = load_dummy_model()
    predictions = []
    for face in faces:
        # 간단한 의사 예측 점수 생성
        probability = 0.4 + random.uniform(-0.2, 0.2)
        predictions.append(probability)
        print(f"[INFO] {face} → 딥페이크 확률: {probability:.2f}")

    avg_prob = sum(predictions) / len(predictions)
    print(f"[RESULT] 평균 딥페이크 확률: {avg_prob:.2f}")
    return avg_prob


# ---------------------------
# 4. 메인 실행 함수 (main.py) - 라이브러리 없이 대체 버전
# ---------------------------
import os
import argparse
from detector import deepfake_detection

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--video', type=str, required=True, help='비디오 파일 경로')
    args = parser.parse_args()

    if not os.path.exists(args.video):
        print(f"[ERROR] 비디오 파일이 존재하지 않습니다: {args.video}")
        return

    probability = deepfake_detection(args.video)
    if probability is not None:
        print(f"[FINAL RESULT] 예측된 딥페이크 확률: {probability:.2f} (0: 진짜, 1: 딥페이크)")

if __name__ == '__main__':
    main()

import streamlit as st
import tempfile
import os
from detector import deepfake_detection

st.set_page_config(page_title="딥페이크 탐지기", layout="centered")
st.title("🎭 딥페이크 탐지기 (FaceForensics++)")

st.write("업로드한 비디오 파일에서 얼굴을 추출하고, 사전 학습된 Xception 모델을 이용해 딥페이크 확률을 계산합니다.")

MODEL_PATH = "xception_ffpp.h5"

uploaded_file = st.file_uploader("비디오 파일 업로드 (.mp4)", type=["mp4"])

if uploaded_file is not None:
    st.video(uploaded_file)

    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as tmp_file:
        tmp_file.write(uploaded_file.read())
        tmp_video_path = tmp_file.name

    if not os.path.exists(MODEL_PATH):
        st.error(f"모델 가중치 파일이 없습니다: {MODEL_PATH}")
    else:
        st.info("얼굴을 추출하고 분석 중입니다. 잠시만 기다려주세요...")
        probability = deepfake_detection(tmp_video_path, MODEL_PATH)

        if probability is not None:
            st.success(f"🎯 딥페이크 확률: {probability:.2f} (0: 진짜, 1: 딥페이크)")
            if probability >= 0.5:
                st.markdown("### ⚠️ 이 영상은 **딥페이크일 가능성**이 높습니다.")
            else:
                st.markdown("### ✅ 이 영상은 **진짜일 가능성**이 높습니다.")
        else:
            st.error("분석 중 오류가 발생했습니다. 다른 파일로 다시 시도해주세요.")

    os.remove(tmp_video_path)
else:
    st.info("좌측 상단에서 .mp4 파일을 업로드해 주세요.")
