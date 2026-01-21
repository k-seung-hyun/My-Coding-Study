# 팀 리스트 생성
teams = ["LG 트윈스", "두산 베어스", "키움 히어로즈", "SSG 랜더스", "KT 위즈", "한화 이글스", "삼성 라이온즈", "NC 다이노스", "롯데 자이언츠", "기아 타이거즈"]
rank_data = []

print("--- 2025 KBO 상세 경기 결과 입력 ---")

for team in teams:
    print(f"\n[{team}]의 기록 입력하기")
    win = int(input("승: "))
    draw = int(input("무: "))
    lose = int(input("패: "))

    # 1단계: 승률 계산
    if (win + lose) > 0:
        win_rate = win / (win + lose)
    else:
        win_rate = 0.0

    # 2단계: 데이터 추가
    rank_data.append([team, win, draw, lose, win_rate])

# 3단계: 모든 팀 입력이 끝난 후 정렬
rank_data.sort(key=lambda x: x[4], reverse=True)

print("\n" + "="*50)
print("🏆 2025 KBO 최종 순위표 (승률 기준)")
print("="*50)

for i in range(len(rank_data)):
    # 언패킹 순서 주의: 위에서 [team, win, draw, lose, rate]로 담았으니 맞춰서 꺼내기
    t, w, d, l, rate = rank_data[i]
    print(f"{i+1}위: {t} | {w}승 {l}패 {d}무 | 승률: {rate:.3f}")