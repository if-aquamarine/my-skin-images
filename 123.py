import os

folder = "skins"

if not os.path.exists(folder):
    print(f"Папка '{folder}' не найдена!")
    exit()

for filename in os.listdir(folder):
    old_path = os.path.join(folder, filename)

    if not os.path.isfile(old_path):
        continue

    # Разделяем имя и расширение
    name, ext = os.path.splitext(filename)

    # Приводим расширение к нижнему регистру и убираем лишние точки
    ext = ext.lower()

    # Если расширение уже .png — ничего не делаем (но проверим дубли)
    if ext == ".png":
        # Защита от случая "file.png.png"
        while name.lower().endswith(".png"):
            name = name[:-4]  # убираем последнее ".png" из имени
        new_filename = name + ".png"
    else:
        # Любой другой случай: просто даём .png
        new_filename = filename.rstrip(".")  # на случай file. → file
        if new_filename == "":
            new_filename = "unknown"
        # Убираем все старые расширения и ставим .png
        new_filename = os.path.splitext(new_filename)[0] + ".png"

    # Убедимся, что имя не пустое
    if new_filename == ".png":
        new_filename = "unknown.png"

    # Если имя изменилось — переименовываем
    if new_filename != filename:
        new_path = os.path.join(folder, new_filename)
        # На случай, если файл с таким именем уже есть — не перезаписывать
        if os.path.exists(new_path):
            print(f"⚠️  Пропущено (файл уже существует): {new_filename}")
        else:
            os.rename(old_path, new_path)
            print(f"Исправлено расширение: {filename} → {new_filename}")