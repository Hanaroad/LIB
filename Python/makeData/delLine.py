import re

# 입력 파일명과 출력 파일명을 지정해주세요.
input_file = './74410m.txt'
output_file = './data.txt'


# 정규표현식 패턴을 정의합니다.
pattern = r"\b[1-9]$"

# 입력 파일을 읽기 모드로 엽니다.
with open(input_file, 'r') as f:
    lines = f.readlines()

# 패턴과 일치하지 않는 행을 저장할 리스트를 생성합니다.
filtered_lines = []

for line in lines:
    # 탭을 기준으로 문자열을 분리합니다.
    elements = line.strip().split('\t')
    if len(elements) >= 2:
        # 두 번째 열의 날짜에서 마지막 숫자를 가져옵니다.
        last_digit = int(elements[1][-1]) if elements[1] else None
        # 마지막 숫자가 1부터 9 사이인 행은 건너뜁니다.
        if last_digit is not None and last_digit >= 1 and last_digit <= 9:
            continue
    filtered_lines.append(line)

# 출력 파일에 필터링된 행을 씁니다.
with open(output_file, 'w') as f:
    for line in filtered_lines:
        f.write(line)

print("작업이 완료되었습니다.")
