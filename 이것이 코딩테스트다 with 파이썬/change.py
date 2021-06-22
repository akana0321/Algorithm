money = int(input())
count = 0
# 큰 화폐 단위부터 차례대로 확인
coin_type = [500, 100, 50, 10]

for coin in coin_type:
    count += money // coin # 해당 화폐로 거슬러 줄 수 있는 동전의 수 세기
    money %= coin

print(count)