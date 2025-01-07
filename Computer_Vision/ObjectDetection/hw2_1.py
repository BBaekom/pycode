import cv2
import numpy as np
import time
from skimage.feature import hog
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# MNIST 바이너리 파일 읽기 함수
def load_mnist_images(filename, num_images):
    with open(filename, "rb") as f:
        f.read(16)  # 헤더 스킵
        buffer = f.read(num_images * 28 * 28)
        data = np.frombuffer(buffer, dtype=np.uint8).reshape(num_images, 28, 28)
        return data

def load_mnist_labels(filename, num_labels):
    with open(filename, "rb") as f:
        f.read(8)  # 헤더 스킵
        buffer = f.read(num_labels)
        labels = np.frombuffer(buffer, dtype=np.uint8)
        return labels

# 전처리 함수: Gaussian Blur + 이미지 반전
def preprocess_images(images):
    processed = []
    for img in images:
        img = cv2.GaussianBlur(img, (3, 3), 0)  # Gaussian Blur (노이즈 제거)
        img = cv2.bitwise_not(img)  # 이미지 반전 (숫자를 흰색, 배경을 검은색으로)
        processed.append(img)
    return np.array(processed)

# HOG 특징 벡터 추출 함수
def extract_hog_features(images):
    hog_features = []
    for img in images:
        feature = hog(
            img, 
            orientations=9, pixels_per_cell=(8, 8), cells_per_block=(2, 2),
            block_norm='L2-Hys', transform_sqrt=True, visualize=False
        )
        hog_features.append(feature)
    return np.array(hog_features)

# SIFT 특징 벡터 추출 함수
def extract_sift_features(images):
    sift = cv2.SIFT_create()
    descriptors_list = []
    for img in images:
        img = cv2.resize(img, (28, 28))
        _, descriptors = sift.detectAndCompute(img, None)
        if descriptors is not None:
            descriptors_list.append(descriptors.mean(axis=0))  # 평균 특징 벡터
        else:
            descriptors_list.append(np.zeros(128))  # 특징점이 없으면 128차원 0벡터
    return np.array(descriptors_list)

# 모델 학습 및 평가 함수
def train_and_evaluate(model_name, model, x_train, x_test, y_train, y_test):
    start_train = time.time()
    model.fit(x_train, y_train)
    end_train = time.time()

    start_predict = time.time()
    y_pred = model.predict(x_test)
    end_predict = time.time()

    accuracy = accuracy_score(y_test, y_pred)
    print(f"{model_name} Accuracy: {accuracy:.4f}")
    print(f"{model_name} Training Time: {end_train - start_train:.2f} seconds")
    print(f"{model_name} Inference Time: {end_predict - start_predict:.2f} seconds\n")
    return accuracy

# 파일 경로 설정
train_images_path = "train-images.idx3-ubyte"
train_labels_path = "train-labels.idx1-ubyte"
test_images_path = "t10k-images.idx3-ubyte"
test_labels_path = "t10k-labels.idx1-ubyte"

# 데이터 로드 및 전처리
print("Loading MNIST dataset and preprocessing...")
x_train = load_mnist_images(train_images_path, 60000)
y_train = load_mnist_labels(train_labels_path, 60000)
x_test = load_mnist_images(test_images_path, 10000)
y_test = load_mnist_labels(test_labels_path, 10000)
x_train_preprocessed = preprocess_images(x_train)
x_test_preprocessed = preprocess_images(x_test)

# HOG 특징 벡터 추출
print("Extracting HOG features...")
x_train_hog = extract_hog_features(x_train_preprocessed)
x_test_hog = extract_hog_features(x_test_preprocessed)

# SIFT 특징 벡터 추출
print("Extracting SIFT features...")
x_train_sift = extract_sift_features(x_train_preprocessed)
x_test_sift = extract_sift_features(x_test_preprocessed)

# 모델 설정 및 학습
print("\n=== Training and Evaluating Models ===")
# kNN + HOG
knn_hog_acc = train_and_evaluate("kNN-HOG", KNeighborsClassifier(n_neighbors=5), x_train_hog, x_test_hog, y_train, y_test)
# Random Forest + HOG
rf_hog_acc = train_and_evaluate("Random Forest-HOG", RandomForestClassifier(n_estimators=200, max_depth=50, random_state=42), x_train_hog, x_test_hog, y_train, y_test)
# kNN + SIFT
knn_sift_acc = train_and_evaluate("kNN-SIFT", KNeighborsClassifier(n_neighbors=5), x_train_sift, x_test_sift, y_train, y_test)
# Random Forest + SIFT
rf_sift_acc = train_and_evaluate("Random Forest-SIFT", RandomForestClassifier(n_estimators=200, max_depth=50, random_state=42), x_train_sift, x_test_sift, y_train, y_test)

# 최종 결과 비교
print("\n=== Final Model Comparison ===")
print(f"kNN-HOG Accuracy: {knn_hog_acc:.4f}")
print(f"Random Forest-HOG Accuracy: {rf_hog_acc:.4f}")
print(f"kNN-SIFT Accuracy: {knn_sift_acc:.4f}")
print(f"Random Forest-SIFT Accuracy: {rf_sift_acc:.4f}")