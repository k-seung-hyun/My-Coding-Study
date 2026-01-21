# 빈 리스트 생성
my_skills = []

# append 사용
my_skills.append("Python")
my_skills.append("Git")
my_skills.append("Java")

print(f"나의 스킬 목록: {my_skills}")



# 2개의 리스트 생성
todo_morning = ["운동", "독서"]
todo_afternoon = ["식사", "코딩"]

# 리스트 더하기
all_today = todo_morning + todo_afternoon

print(all_today)

# 전체 갯수 확인하기
total_count = len(all_today)

print(f"오늘 할 일: {all_today}")
print(f"할 일의 갯수: {total_count}개")


# 데이터 수정, f -string 활용
users = ["승현", "지원", "하영"]

# 1번째의 내용 변경
users[0] = "채영"

# f -string을 사용하여 출력
for user in users:
    print(f"안녕하세요! {user}님! 환영합니다!")