teams = ["LG 트윈스", "두산 베어스", "키움 히어로즈", "SSG 랜더스", "KT 위즈", "한화 이글스", "삼성 라이온즈", "NC 다이노스", "롯데 자이언츠", "기아 타이거즈"]
rank_data = []

print("--- 2025 KBO 경기 결과 입력 및 파일 저장 ---")

for team in teams:
    print(f"{team}의 기록 입력")
    win = int(input("승: "))
    draw = int(input("무: "))
    lose = int(input("패: "))

    if (win + lose) > 0:
        win_rate = win / (win + lose)
    else:
        win_rate = 0.0
    
    rank_data.append([team, win, draw, lose, win_rate])

# 승률 기준 정렬
rank_data.sort(key=lambda x: x[4], reverse=True)

# --- 💾 파일 저장 로직 추가 ---
# 'w'는 Write(쓰기) 모드이다. 파일이 없으면 새로 만들고, 있으면 덮어씀.
with open("kbo_rank.txt", "w", encoding="utf-8") as f:
    f.write("--- 2025 KBO 최종 순위표 ---\n")
    for i in range(len(rank_data)):
        t, w, d, l, rate = rank_data[i]
        # 파일에 써넣을 문자열 만들기
        line = f"{i+1}위: {t} | {w}승 {d}무 {l}패 | 승률: {rate:.3f}\n"
        f.write(line)

print("\n✅ kbo_rank.txt 파일에 저장이 완료되었습니다!")