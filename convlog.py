import re

# Путь к вашему лог-файлу
input_file = 'export_log.txt'
# Путь к файлу, куда будут сохранены результаты
output_file = 'tfc.tsv'

# Регулярное выражение для поиска строк, начинающихся с "TFC"
pattern = re.compile(r'^TFC\s+([^\s]+)\s+([^\s]+)\s+(\d+)\s+\[(\d+)x(\d+)\]\s+(PF_[^\s]+)$')

# Открываем файлы для чтения и записи
with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
    # Записываем заголовок для TSV файла
    outfile.write('Name\tGuid\tIndex\tWidth\tHeight\tFormat\n')
    
    for line in infile:
        match = pattern.match(line.strip())
        if match:
            # Извлекаем части строки, соответствующие шаблону
            name, uuid, index, width, height, format = match.groups()
            # Записываем в TSV формат
            outfile.write(f'{name}\t{uuid}\t{index}\t{width}\t{height}\t{format}\n')

print(f"Данные успешно извлечены и сохранены в {output_file}")