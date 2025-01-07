import cv2
import numpy as np
from skimage.feature import hog
import tarfile
import os
from sklearn.metrics.pairwise import cosine_similarity
import sys

# HOG 특징점 추출 함수
def extract_hog_features(image):
    """HOG 특징점 추출"""
    feature = hog(image, orientations=9, pixels_per_cell=(8, 8),
                  cells_per_block=(2, 2), block_norm='L2-Hys', visualize=False)
    return feature

# label.tar.gz 파일에서 라벨 이미지 불러오기 및 HOG 특징 벡터 추출
def load_label_features_from_tar(tar_gz_file):
    print(f"Loading label images and extracting HOG features from '{tar_gz_file}'...")
    label_features = []

    with tarfile.open(tar_gz_file, "r:gz") as tar:
        for member in tar.getmembers():
            if member.isfile() and member.name.endswith(('.png', '.jpg', '.jpeg')):
                extracted_file = tar.extractfile(member)
                file_bytes = np.asarray(bytearray(extracted_file.read()), dtype=np.uint8)
                image = cv2.imdecode(file_bytes, cv2.IMREAD_GRAYSCALE)

                if image is not None:
                    image_resized = cv2.resize(image, (128, 128))
                    feature = extract_hog_features(image_resized)
                    label_features.append(feature)

    print(f"Extracted HOG features from {len(label_features)} label images.")
    return np.array(label_features)

# 입력 이미지와 라벨 특징 벡터 비교
def detect_empire_state(input_image_path, tar_gz_file, threshold=0.6):
    print(f"Detecting Empire State Building in '{input_image_path}'...")

    # 라벨 이미지의 HOG 특징 벡터 불러오기
    label_features = load_label_features_from_tar(tar_gz_file)

    # 입력 이미지 로드 및 HOG 특징점 추출
    input_image = cv2.imread(input_image_path, cv2.IMREAD_GRAYSCALE)
    if input_image is None:
        print(f"Error: Input image '{input_image_path}' not found.")
        sys.exit(1)

    input_image_resized = cv2.resize(input_image, (128, 128))
    input_feature = extract_hog_features(input_image_resized)

    # 유사도 계산 (Cosine Similarity)
    similarities = cosine_similarity([input_feature], label_features)[0]
    max_similarity = max(similarities)

    # 결과 판단
    if max_similarity >= threshold:
        print("True: Empire State Building detected in the image.")
    else:
        print("False: Empire State Building not detected in the image.")


# 메인 실행 코드
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python hw2_2.py <input_image>")
        sys.exit(1)

    # 명령행 인자로 입력 이미지 경로 받기
    input_image_path = sys.argv[1]
    tar_gz_file = "label.tar.gz"  # 라벨 이미지가 포함된 tar.gz 파일

    # 검출 실행
    detect_empire_state(input_image_path, tar_gz_file, threshold=0.7)