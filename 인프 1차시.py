# 생선 분류 문제
bream_length = [25.4, 26.3, 26.5, 29.0, 29.0, 29.7, 29.7, 30.0, 30.0, 30.7, 31.0, 31.0,
                31.5, 32.0, 32.0, 32.0, 33.0, 33.0, 33.5, 33.5, 34.0, 34.0, 34.5, 35.0,
                35.0, 35.0, 35.0, 36.0, 36.0, 37.0, 38.5, 38.5, 39.5, 41.0, 41.0]
bream_weight = [242.0, 290.0, 340.0, 363.0, 430.0, 450.0, 500.0, 390.0, 450.0, 500.0, 475.0, 500.0,
                500.0, 340.0, 600.0, 600.0, 700.0, 700.0, 610.0, 650.0, 575.0, 685.0, 620.0, 680.0,
                700.0, 725.0, 720.0, 714.0, 850.0, 1000.0, 920.0, 955.0, 925.0, 975.0, 950.0]

import matplotlib.pyplot as plt

plt.scatter(bream_length, bream_weight)
plt.xlabel('length')
plt.ylabel('weight')
plt.show()

smelt_length = [9.8, 10.5, 10.6, 11.0, 11.2, 11.3, 11.8, 11.8, 12.0, 12.2, 12.4, 13.0, 14.3, 15.0]
smelt_weight = [6.7, 7.5, 7.0, 9.7, 9.8, 8.7, 10.0, 9.9, 9.8, 12.2, 13.4, 12.2, 19.7, 19.9]

plt.scatter(bream_length, bream_weight)
plt.scatter(smelt_length, smelt_weight)
plt.xlabel('length')
plt.ylabel('weight')
plt.show()

# Feature
length = bream_length + smelt_length
weight = bream_weight + smelt_weight
print(length)
print(weight)

# 사이킷런을 위해서는 2차원 리스트로 제작해야 함
fish_data = [[l, w] for l, w in zip(length, weight)]
print(fish_data)

# Taget
fish_target =[1] * 35 + [0] * 14
print(fish_target)

from sklearn.neighbors import KNeighborsClassifier
kn = KNeighborsClassifier()

# 학습
kn.fit(fish_data, fish_target) # Feature(2D), Target

# 평가
kn.score(fish_data, fish_target)

kn.predict([[30, 600]])
print(kn._fit_X)
print(kn._y)


kn49 = KNeighborsClassifier(n_neighbors=49)
kn49.fit(fish_data, fish_target)
print(kn49.score(fish_data, fish_target))




# 훈련 셋, 테스트 셋
fish_length = [25.4, 26.3, 26.5, 29.0, 29.0, 29.7, 29.7, 30.0, 30.0, 30.7, 31.0, 31.0,
                31.5, 32.0, 32.0, 32.0, 33.0, 33.0, 33.5, 33.5, 34.0, 34.0, 34.5, 35.0,
                35.0, 35.0, 35.0, 36.0, 36.0, 37.0, 38.5, 38.5, 39.5, 41.0, 41.0, 9.8,
                10.5, 10.6, 11.0, 11.2, 11.3, 11.8, 11.8, 12.0, 12.2, 12.4, 13.0, 14.3, 15.0]
fish_weight = [242.0, 290.0, 340.0, 363.0, 430.0, 450.0, 500.0, 390.0, 450.0, 500.0, 475.0, 500.0,
                500.0, 340.0, 600.0, 600.0, 700.0, 700.0, 610.0, 650.0, 575.0, 685.0, 620.0, 680.0,
                700.0, 725.0, 720.0, 714.0, 850.0, 1000.0, 920.0, 955.0, 925.0, 975.0, 950.0, 6.7,
                7.5, 7.0, 9.7, 9.8, 8.7, 10.0, 9.9, 9.8, 12.2, 13.4, 12.2, 19.7, 19.9]

fish_data = [[l, w] for l, w in zip(fish_length, fish_weight)]
fish_target = [1] * 35 + [0] * 14

print(fish_data)
print(fish_target)

train_input = fish_data[:35]
train_target = fish_target[:35] # bream

test_input = fish_data[35:]
test_target = fish_target[35:] # smelt

kn.fit(train_input, train_target)
kn.score(test_input, test_target)

# 샘플링 편향
# 훈련 데이터 셋은 모두 bream, 테스트 데이터 셋은 모두 smelt

import numpy as np
input_arr = np.array(fish_data)
target_arr = np.array(fish_target)

print(input_arr)
print(target_arr)
print(input_arr.shape)

np.random.seed(42)
index = np.arange(49)
np.random.shuffle(index)
print(index)
print(input_arr[[1, 3]])
print(input_arr[2:5, 1])

train_input = input_arr[index[:35]]
train_target = target_arr[index[:35]]
test_input = input_arr[index[35:]]
test_target = target_arr[index[35:]]
print(train_input)
print(test_input)

plt.scatter(train_input[:, 0], train_input[:, 1])
plt.scatter(test_input[:, 0], test_input[:, 1])
plt.xlabel('length')
plt.ylabel('weight')
plt.show()

kn.fit(train_input, train_target)
kn.score(test_input, test_target)
print(kn.predict(test_input))
print(test_target)