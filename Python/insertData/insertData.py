import os

script_dir = os.path.dirname(os.path.realpath(__file__))
input_path = os.path.join(script_dir, "input_data.txt")
output_path = os.path.join(script_dir, "output_data.txt")

def process_data(datafile, outputfile):
    with open(datafile, 'rt', encoding='utf-8') as file:
        lines = file.readlines()

        buffer = []
        for line in lines:
            buffer.extend(line.strip().split('\t'))

            # 17개의 컬럼을 찾았을 경우 출력
            while len(buffer) >= 13:
                with open(outputfile, 'a', encoding='utf-8') as f:
                    formatted_line = "', '".join(buffer[:13])
                    f.write(f"('{formatted_line}'),\n")
                buffer = buffer[17:]

if __name__ == '__main__':
    process_data(input_path, output_path)
