'''
    1. 경사하강법 (gradient descent)
        1) 역전파 알고리즘은 신경망 학습 문제를 최적화 문제(optimization)를 접근함.
           손실함수 값을 최소로 하는 가중치를 찾으면 됨.
            - 가장 낮은 값을 찾으면 됨.
        2) 그래디언트(기울기)는 접선의 기울기로 이해해도 됨.
           접선의 기울기가 양수이면 반대로 가중치를 감소시킴
            - 손실함수를 가중치로 미분한 값이 양수이면 => 가중치를 감소시킴
            - 손실함수를 가중치로 미분한 값이 음수이면 => 가중치를 증가시킴
        3) 손실함수 (loss, cost function)을 최소화 하기 위해
           함수(f)의 계수(coefficient) 값을 찾기 위해 사용되는 최적화 알고리즘.
            - 계수의 초기 추정값을 시작으로 계속해서 계수를 업데이트하며,
              손실(cost)을 줄이는 일련의 작업을 수행하는 알고리즘.
            - 경사 하강법의 목표는 코스트 함수를 최소화하기 위해 계수 값을 찾는 것임.
            - 계수의 경사도(gradient)를 계산한 후, 경사도가 가리키는 방향으로 계수를
              업데이트하는 것으로 작동함.
            - 업데이트의 크기는 학습률(learning rate)에 의해 제어되며,
              학습률은 각 반복의 단계 크기를 결정함.
'''

x = 10
learning_rate = 0.2
max_iterations = 100

#손실함수 정의
loss_func = lambda x: (x - 3) **2 + 10

#그래디언트(기울기) 정의 (손실함수의 1차 미분값)
gradient = lambda x: 2 * x - 6

# 경사하강법
for i in range(max_iterations):
    x = x - learning_rate * gradient(x)
    print("손실함수값(", x, ") = ", loss_func(x))

print("최솟값 = ", x)












