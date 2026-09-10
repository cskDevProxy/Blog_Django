import os
import uuid

# Переименовывание photo
def rename_photo(instance, filename):
    ext = os.path.splitext(filename)[1]
    new_name = f'{uuid.uuid4().hex}{ext}'
    return f'posts/images/{new_name}'

# Переименовывание file
def rename_file(instance, filename):
    ext = os.path.splitext(filename)[1]
    new_name = f'{uuid.uuid4().hex}{ext}'
    return f'posts/files/{new_name}'