import os
from datetime import datetime

file_name = 'test.txt'
content = 'Привет, мир!'

# Создаёт или перезаписывает файл с содержимым
with open(file_name, 'w') as file:
    file.write(content)

# Коммит и пуш изменений в репозиторий
os.system('git add ' + file_name)
os.system(f'git commit -m "Добавлен файл test.txt на {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}"')
os.system('git push')
