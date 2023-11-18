def clean_title(self):
    title = self.cleaned_data['title']
    ALLOWED_CHARS = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯабвгдеёжзийклмнопрстуфхцчшщбыъэюя0123456789- "
    if not (set(title) <= set(ALLOWED_CHARS)):
        raise ValidationError("Должны быть только русские символы, дефис и пробел.")

    return title

print(set('dadadas'))