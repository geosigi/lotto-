# 난수 생성을 통한 로또 번호 생성
import random

lotto_num = list(range(5))

for i in range(1,5):
    lotto_num[i] = random.randint(1,45)
    
lotto_num.sort()   
print("로또번호 {}".format(lotto_num))
result= []
import random

lotto_num = list(range(5))

for i in range(1,5):
    lotto_num[i] = random.randint(1,45)
    
lotto_num.sort()   
print("로또번호 {}".format(lotto_num))

# 중복된 번호 제거
result= []

for value in lotto_num:
    if value not in result:
        result.append(value)

print("로또번호 {}".format(result))

