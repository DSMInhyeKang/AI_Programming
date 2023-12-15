from sklearn.datasets import load_iris

# #1 train_test_split을 import 하시오.
from sklearn.model_selection import train_test_split

# #2 load_irist()함수를 사용하여 data 변수에 데이터셋을 저장하시오.
data = load_iris()

# #3 data를 출력하여 확인해보시오.
print(data)

# #4 data에서 key값이 "feature_names"인 데이터를 출력하여 확인해보시오.
print(data['feature_names'])

# #5 data에서 key값이 "data"인 데이터를 출력하여 확인해보시오.
print(data['data'])

# #6 data에서 key값이 "target_names"인 데이터를 출력하여 확인해보시오.
print(data['target_names'])

# #7 data에서 key값이 "target"인 데이터를 출력하여 확인해보시오.
print(data['target'])

# #8 data에서 key값이 "data"인 데이터를 feuature 변수에 저장하시오.
feature = data['data']

# #9 feature를 출력하여 확인하시오.
print(feature)

# #10 data에서 key값이 "target"인 데이터를 target 변수에 저장하시오.
target = data['target']

# #11 target을 출력하여 확인하시오.
print(target)


# #12 train_test_split을 사용하여 훈련 데이터셋과 테스트 데이터셋으로 분류하시오
# # (단, 훈련 데이터셋과 테스트 데이터셋의 비율은 7:3, random_state는 42, stratify를 사용하시오.)
train_input, test_input, train_target, test_target = train_test_split(feature, target, test_size=45, stratify=target, random_state=42)

# #13~15 KNeighborsClassifier를 import하고 사용하여 모델을 학습시키시오.
from sklearn.neighbors import KNeighborsClassifier

kn = KNeighborsClassifier()
kn.fit(train_input, train_target)


# #16 테스트 데이터셋에 대해 모델을 평가하시오.(평가 결과도 출력하시오.)
print(kn.score(test_input, test_target))


# #17 훈련 데이터셋에 대해 모델을 평가하시오.(평가 결과도 출력하시오.)
print(kn.score(train_input, train_target))


# #18 샘플([[6, 3, 5, 2]])에 대한 모델의 예측값을 출력하시오.
print(kn.predict([[6, 3, 5, 2]]))

# #19 예측값을 구하는 코드(바로 위의 코드)를 사용하여 해당 샘플이 어떤 꽃인지 출력하시오.
print(data.target_names[kn.predict([[6, 3, 5, 2]])])


# #20 과대적합, 과소적합 중 어느 것에 해당하는지 이유와 함께 설명하시오.
# 과소적합: 훈련 셋의 평가 결과보다 테스트 셋의 평가 결과가 더 높기 때문이다.