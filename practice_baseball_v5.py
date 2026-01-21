print("--- 📂 저장된 야구 순위 데이터 불러오기 ---")

# 'r'은 Read(읽기) 모드.
try:
    with open("kbo_rank.txt", "r", encoding="utf-8") as f:
        # 파일의 모든 내용을 읽어서 리스트로 가져옴.
        lines = f.readlines()
        
        for line in lines:
            # strip()은 문장 끝의 줄바꿈(\n) 문자를 제거해줌.
            print(line.strip())

except FileNotFoundError:
    print("❌ 저장된 파일(kbo_rank.txt)을 찾을 수 없습니다. 먼저 v4를 실행해 주세요.")

print("\n✅ 데이터를 모두 불러왔습니다!")

# f.readlines(): 파일에 적힌 문장들을 한 줄씩 쪼개서 리스트로 만들어 줌. (예: ["1위: LG...", "2위: 삼성..."])
# line.strip(): 파일을 읽어오면 문장 끝에 보이지 않는 \n(엔터)이 붙어 있는데 이걸 제거해줘야 출력했을 때 줄 간격이 너무 벌어지지 않고 깔끔함.
# try-except: 만약 파일이 없을 때 프로그램이 에러를 내며 꺼지는 것을 방지하는 '예외 처리' 문법.