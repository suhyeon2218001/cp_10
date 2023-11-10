import random

def generate_lotto_numbers():
    # 빈 리스트 생성
    lotto_numbers = []

    # 로또 번호가 6개가 될 때까지 반복
    while len(lotto_numbers) < 6:
        # 1부터 45까지의 랜덤한 숫자 생성
        number = random.randint(1, 45)

        # 생성된 숫자가 이미 리스트에 없으면 추가
        if number not in lotto_numbers:
            lotto_numbers.append(number)

    # 리스트를 오름차순으로 정렬
    lotto_numbers.sort()

    # 생성된 로또 번호 출력
    print("생성된 로또 번호는 {} 입니다.".format(lotto_numbers))

    # 생성된 로또 번호 반환
    return lotto_numbers

# 함수 실행
generate_lotto_numbers()
