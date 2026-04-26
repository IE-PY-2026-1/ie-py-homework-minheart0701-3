# 파일이름 :[1차과제 Code 입력]
# 작 성 자 :유민형

1차과제 코드 제출
# [4단계] 함수 정의: 데이터 분석 및 계산 로직 분리
def analyze_health(walk, food, goal):
    """오늘의 활동량과 사료량을 분석하는 함수 (2단계 조건문 활용)"""
    status = ""
    if walk >= goal:
        status += "✅ 활동량 충분! "
    else:
        status += "⚠️ 산책 부족! "
        
    if food > 200:
        status += "🍖 과식 주의"
    else:
        status += "🥗 적정 섭취"
    return status

def show_statistics(logs):
    """배열 내 데이터를 계산하는 함수 (4단계 배열 활용)"""
    if not logs:
        print("\n데이터가 없습니다. 먼저 기록을 입력해주세요.")
        return
    
    total_walk = 0
    for log in logs:
        total_walk += log[1] # 각 리스트의 1번 인덱스(산책시간) 합산
    
    avg_walk = total_walk / len(logs)
    print(f"\n📊 [통계] 현재까지 평균 산책 시간: {avg_walk:.1f}분")

# --- 메인 프로그램 시작 ---

# [1단계] 변수 및 입출력
print("🐾 우리 집 막내 건강 지킴이 V1.0 🐾")
pet_name = input("반려동물 이름을 입력하세요: ")
goal_walk = int(input(f"{pet_name}의 하루 권장 산책 시간(분): "))
health_logs = []  # [4단계] 데이터를 담을 배열(리스트)

# [3단계] 반복문 및 메뉴
while True:
    print(f"\n--- {pet_name} 헬스케어 메뉴 ---")
    print("1. 기록 입력 (입력/배열)")
    print("2. 당일 진단 (조건문)")
    print("3. 전체 통계 (함수 계산)")
    print("4. 기록 검색 (배열 탐색)")
    print("5. 프로그램 종료")
    
    choice = input("원하는 메뉴 번호를 입력하세요: ")

    if choice == '1':
        # 데이터 입력 및 배열 저장
        day = len(health_logs) + 1
        walk = int(input(f"[{day}일차] 산책 시간(분): "))
        food = int(input(f"[{day}일차] 사료 섭취량(g): "))
        mood = int(input(f"[{day}일차] 컨디션 점수(1-10): "))
        
        # 2차원 배열 구조로 저장
        health_logs.append([day, walk, food, mood])
        print(f"✨ {day}일차 기록이 완료되었습니다!")

    elif choice == '2':
        if not health_logs:
            print("❗ 먼저 기록을 입력해야 진단이 가능합니다.")
        else:
            # 가장 최근 데이터 가져오기
            recent = health_logs[-1]
            result = analyze_health(recent[1], recent[2], goal_walk)
            print(f"\n🩺 오늘의 진단: {result}")

    elif choice == '3':
        show_statistics(health_logs)

    elif choice == '4':
        if not health_logs:
            print("❗ 저장된 기록이 없습니다.")
        else:
            search_day = int(input("조회하고 싶은 일차(숫자)를 입력하세요: "))
            if 0 < search_day <= len(health_logs):
                log = health_logs[search_day - 1]
                print(f"\n📅 {search_day}일차 상세 기록")
                print(f"- 산책: {log[1]}분 / 사료: {log[2]}g / 기분: {log[3]}점")
            else:
                print("❌ 해당 일차의 기록이 없습니다.")

    elif choice == '5':
        print(f"사랑스러운 {pet_name}(와)과 함께 건강한 하루 보내세요! 종료합니다.")
        break # 반복문 탈출

    else:
        print("⚠️ 잘못된 입력입니다. 1~5 사이의 숫자를 입력해주세요.")




＃ ２차 과제 제출
#[1] 변수 선언 (5개 이상:이름, 나이, 체중, 지수, 칭호 등)
pet_age = 0       #int
pet_weight = 0,0  #float
health_index = 0,0 #float
special_title = "" #str

#[2] 입출력 포매팅 ＆ 형변환
ｐｅｔ—ｎａｍｅ ＝ ｉｎｐｕｔ（“반려동물 이름 입력： ”）
ｐｅｔ—ａｇｅ ＝ ｉｎｔ（ｉｎｐｕｔ（“나이 입력（정수）： ”））
ｐｅｔ—ｗｅｉｇｈｔ ＝ ｆｌｏａｔ（ｉｎｐｕｔ（“현재 몸무게（ｋｇ）： ”））ｐｒｉｎｔ（“－－－ｑ반려동물 정밀 건강 진단 시스템－－－”）
ｐｅｔ—ｎａｍｅ  ＝ 

＃｢３｣ 리스트 입력 및 ｆｏｒ문 활용 （활동 수치 ３개 입력）
＃활동 데이터：｢산책 시간、 식사량、 수면 시간｣
ａｃｔｉｖｉｔｙ—ｄａｔａ ＝ ［］
ａｃｔｉｖｉｔｙ—ｎａｍｅｓ ＝［“산책 시간９분）”、 “식사량（ｇ）”、“수면 시간（시간）” ｣

ｉ ｉｎ ｒａｎｇｅ（３） ：
      ｖａｌｕｅ ＝ ｆｌｏａｔ９ｉｎｐｕｔ（ｆ“오늘의｛ａｃｔｉｖｉｔｙ—ｎａｍｅｓ［ｉ］｝을 입력하세요： ”）
      ａｃｔｉｖｉｔｙ—ｄａｔａ。ａｐｐｅｎｄ（ｖａｌｕｅ） ＃［４］ 리스트 조작１ （ａｐｐｅｎｄ）

＃［４］리스트 조작 （메소드／내장함수 ４종； ａｐｐｅｎｄ、 ｓｕｍ、 ｌｅｎ、 ｍａｘ）
ｔｏｔａｌ—ａｃｔｉｖｉｔｙ ＝ ｓｕｍ（ａｃｔｉｖｉｔｙ—ｄａｔａ）
ａｖｇ—ａｃｔｉｖｉｔｙ ＝ ｔｏｔａｌ—ａｃｔｉｖｉｔｙ／ ｌｅｎ（ａｃｔｉｖｉｔｙ—ｄａｔａ）＃３。 ｌｅｎ 활용
ｍａｘ—ｖａｌ＝ｍａｘ（ａｃｔｉｖｉｔｙ—ｄａｔａ）   ＃４。 ｍａｘ 활용

＃｢５、６｣ 가중치 연산 및 복합 대입 연산자 활용
＃종합 건강 지수 공식：（산책＊１。５）＋ （식사＊０。８）＋ （수면＊１。２）
ｈｅａｌｔｈ—ｉｎｄｅｘ ＋＝ （ａｃｔｉｖｉｔｙ－ｄａｔａ［０］＊１。５）
ｈｅａｌｔｈ—ｉｎｄｅｘ ＋＝ （ａｃｔｉｖｉｔｙ—ｄａｔａ［１］ ＊ ０。８）
ｈｅａｌｔｈ—ｉｎｄｅｘ ＋＝ （ａｃｔｉｖｉｔｙ—ｄａｔａ［２］＊１。２）

＃［７］ 제어구조 （ｉｆ－ｅｌｉｆ－ｅｌｓｅ ５단계 등급 판정）
ｇｒａｄｅ ＝ “”
ｉｆ ｈｅａｌｔｈ—ｉｎｄｅｘ ＞＝ ２００：
      ｇｒａｄｅ ＝ “Ｓ（최상의 컨디션）”
ｅｌｉｆ ｈｅａｌｔｈ—ｉｎｄｅｘ ＞＝ １５０：
      ｇｒａｄｅ ＝ “Ａ （건강함）“
ｅｌｉｆ ｈｅａｌｔｈ—ｉｎｄｅｘ ＞＝ １００：
      ｇｒａｄｅ ＝ ”Ｂ （보통）“
ｅｌｉｆ ｈｅａｌｔｈ—ｉｎｄｅｘ ＞＝ ５０：
      ｇｒａｄｅ ＝ ”Ｃ （주의） “
ｅｌｓｅ：
      ｇｒａｄｅ ＝ ”Ｆ （관리 시급）“

＃｢５、７｣ 논리 연산자（ａｎｄ／ｏｒ）를 활용한 특별 칭호 부여 （중첩／독립 ｉｆ）
ｉｆ ａｃｔｉｖｉｔｙ—ｄａｔａ［０］ ＞＝ ６０ ａｎｄ ｈｅａｌｔｈ—ｉｎｄｅｘ ＞＝ １８０：
       ｓｐｅｃｉａｌ—ｔｉｔｌｅ ＝ ”전설의 산책왕“
ｅｌｉｆ ａｃｔｉｖｉｔｙ—ｄａｔａ［１］ ＞＝ ５００ ｏｒ ａｃｔｉｖｉｔｙ—ｄａｔａ［２］ ＞＝ １５：
         ｓｐｅｃｉａｌ－ｔｉｔｔｌｅ ＝ ”잠꾸러기”
ｅｌｓｅ：
         ｓｐｅｃｉａｌ—ｔｉｔｔｌｅ＝ “평범함”

＃최종 결과 출력 （ｆ－ｓｔｒｉｎｇ 포매팅）
ｐｒｉｎｔ（“—” ＊３０）
ｐｒｉｎｔ（ｆ“［｛ｐｅｔ—ｎａｍｅ｝］의 진단 결과”）
ｐｒｉｎｔ（ｆ“ 종합 건강 지수：｛ｈｅａｌｔｈ—ｉｎｄｅｘ：。２ｆ｝점 ”）
ｐｒｉｎｔ（ｆ“ 최종등급：｛ｇｒａｄｅ｝”）
ｐｒｉｎｔ（ｆ“ 특별 칭호：＜｛ｓｐｅｃｉａｌ—ｔｉｔｔｌｅ｝＞”）
ｐｒｉｎｔ（ｆ“ 최고 기록 수치：｛ｍａｘ—ｖａｌ｝”） 
ｐｒｉｎｔ（“—”＊３０）



# [1] 변수 선언 (5개 이상: 이름, 나이, 체중, 지수, 칭호 등)
pet_name = ""        # str
pet_age = 0          # int
pet_weight = 0.0     # float
health_index = 0.0   # float
special_title = ""   # str

# [2] 입출력 포매팅 & 형변환
print("--- 🐾 반려동물 정밀 건강 진단 시스템 ---")
pet_name = input("반려동물 이름 입력: ")
pet_age = int(input("나이 입력(정수): "))
pet_weight = float(input("현재 몸무게(kg): "))

# [3] 리스트 입력 및 for문 활용 (활동 수치 3개 입력)
# 활동 데이터: [산책 시간, 식사량, 수면 시간]
activity_data = []
activity_names = ["산책 시간(분)", "식사량(g)", "수면 시간(시간)"]

for i in range(3):
    value = float(input(f"오늘의 {activity_names[i]}을 입력하세요: "))
    activity_data.append(value) # [4] 리스트 조작 1 (append)

# [4] 리스트 조작 (메소드/내장함수 4종: append, sum, len, max)
total_activity = sum(activity_data)    # 2. sum 활용
avg_activity = total_activity / len(activity_data) # 3. len 활용
max_val = max(activity_data)           # 4. max 활용

# [5, 6] 가중치 연산 및 복합 대입 연산자 활용
# 종합 건강 지수 공식: (산책 * 1.5) + (식사 * 0.8) + (수면 * 1.2)
health_index += (activity_data[0] * 1.5) 
health_index += (activity_data[1] * 0.8)
health_index += (activity_data[2] * 1.2)

# [7] 제어구조 (if-elif-else 5단계 등급 판정)
grade = ""
if health_index >= 200:
    grade = "S (최상의 컨디션)"
elif health_index >= 150:
    grade = "A (건강함)"
elif health_index >= 100:
    grade = "B (보통)"
elif health_index >= 50:
    grade = "C (주의)"
else:
    grade = "F (관리 시급)"

# [5, 7] 논리 연산자(and/or)를 활용한 특별 칭호 부여 (중첩/독립 if)
if activity_data[0] >= 60 and health_index >= 180:
    special_title = "전설의 산책왕"
elif activity_data[1] >= 500 or activity_data[2] >= 15:
    special_title = "잠만자는 먹보 대장"
else:
    special_title = "평범한 귀요미"

# 최종 결과 출력 (f-string 포매팅)
print("-" * 30)
print(f"▶ [{pet_name}]의 진단 결과")
print(f"▶ 종합 건강 지수: {health_index:.2f}점")
print(f"▶ 최종 등급: {grade}")
print(f"▶ 특별 칭호: < {special_title} >")
print(f"▶ 최고 기록 수치: {max_val}")
print("-" * 30)