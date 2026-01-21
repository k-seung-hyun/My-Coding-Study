# 팀 리스트 생성
teams = ["LG 트윈스", "두산 베어스", "키움 히어로즈", "SSG 랜더스", "KT 위즈", "한화 이글스", "삼성 라이온즈", "NC 다이노스", "롯데 자이언츠", "기아 타이거즈"]

# 승수를 받을 빈 리스트 생성
wins_list = []

# 승수 입력 받기
for team in teams:
    win = int(input(f"{team}의 승수를 입력해주세요: "))
    wins_list.append(win)

#[팀, 승수]를 묶어서 새로운 리스트 생성
rank_data = []

for i in range(len(teams)):
    rank_data.append([teams[i], wins_list[i]])

# 정렬
rank_data.sort(key=lambda x: x[1], reverse=True)

print("\n--- 2025 KBO 최종 순위표 ---")

# 최종 결과 출력
for i in range(len(rank_data)):
    team_name = rank_data[i][0]
    win_count = rank_data[i][1]
    print(f"{i+1}위: {team_name} ({win_count}승)")