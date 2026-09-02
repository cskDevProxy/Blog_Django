import os
import uuid


def rename_photo(instance, filename):
    ext = os.path.splitext(filename)[1]

    new_name = f'{uuid.uuid4().hex}{ext}'

    return f'posts/images/{new_name}'

