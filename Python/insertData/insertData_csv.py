import os
import csv

script_dir = os.path.dirname(os.path.realpath(__file__))
input_path = os.path.join(script_dir, "input_data.txt")
output_path = os.path.join(script_dir, "output_data.txt")


def dataRead(datafile, outputfile):
    with open(datafile, 'rt', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter='\t')  # 탭을 구분자로 사용

        with open(outputfile, 'w', encoding='utf-8') as f:
            # for fileLine in file:
            for line in reader:
            #     line = fileLine.strip().split('\t')  # 탭으로 구분하여 데이터를 분리합니다.
                
                # 예외 처리: 각 줄의 데이터가 기대한대로 항목이 아니면 스킵합니다 => (줄수+1)
                if len(line) != 17:
                    continue
                
                # 빈칸 처리: 각 항목을 검사하여 빈칸이면 ''로 바꾸기
                line = ['' if item == '' else item for item in line]  # <-- 이 부분을 추가했습니다
                

                # 여기서 데이터의 형식과 순서에 따라 처리합니다.
                # 예를 들면, line[0]은 'CA_act_1' 같은 값을, line[1]은 '천안시' 같은 값을 가지므로
                # 이를 적절히 처리해야 합니다. 
                # 아래는 단순한 예제로, 실제 요구 사항에 따라 수정해야 할 수 있습니다.
                formatted_line = f"('{line[0]}', '{line[1]}', '{line[2]}', '{line[3]}', '{line[4]}', '{line[5]}', '{line[6]}', '{line[7]}', '{line[8]}', '{line[9]}', '{line[10]}', '{line[11]}', '{line[12]}', '{line[13]}', '{line[14]}', '{line[15]}', '{line[16]}'),"
                f.write(formatted_line + "\n")

if __name__ == '__main__':
    dataRead(input_path, output_path)


