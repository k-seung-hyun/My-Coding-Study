# KBO Team 리스트 생성
teams = ["LG 트윈스", "두산 베어스", "키움 히어로즈", "SSG 랜더스", "KT 위즈", "한화 이글스", "삼성 라이온즈", "NC 다이노스", "롯데 자이언츠", "기아 타이거즈"]

# 각 팀의 승리 수를 담을 빈 리스트 생성
wins_list = []

print("--- 2025 KBO 팀 별 승리 수 작성 ---")

# 반복문을 이용해서 모든 팀의 승리 숫자 받기
for team in teams:
    win = int(input(f"{team}의 승수를 입력해주세요."))
    wins_list.append(win)

print("\n--- 실시간 야구 순위표 (입력순) ---")

# 리스트 두 개를 합쳐서 출력
for i in range(len(teams)):
    print(f"{i+1}번째 팀: {teams[i]} ({wins_list[i]}승)")