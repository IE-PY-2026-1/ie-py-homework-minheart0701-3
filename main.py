# 파일이름 :[1차과제 Code 입력]
# 작 성 자 :유민형
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