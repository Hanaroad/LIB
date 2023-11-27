import re


def dataRead(datafile):
    with open(datafile, 'rt', encoding='utf-8') as file:
        lines = file.readlines()

    with open('./data.txt', 'w', encoding='utf-8') as f:
        for line in lines:
            line = re.sub(r"[^0-9:. -]", " ", line)  # 정규표현식
            line = list(line.strip().split())
            if len(line) >= 3:
                id_value = line[0]
                datetime_value = line[1]
                date_value = datetime_value[:8]
                time_value = datetime_value[8:]
                temperature = float(line[2])
                values = [float(val) for val in line[3:]]
                result = f"('{id_value}', '{datetime_value}', '{date_value}', '{time_value}', {temperature}, {', '.join(map(str, values))}, '2023-06-12 12:29:00'),"
                f.write(result + "\n")

                
# ('2022-01-01 0:00', -2.6, 4, 1, 0, 75.3, 'AWS744'),


if __name__ == '__main__':
    dataRead('./74410m.txt')
