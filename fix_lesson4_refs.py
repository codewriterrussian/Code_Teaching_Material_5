from pathlib import Path

path = Path("student_handouts_md/Lesson_04_Operators.md")
text = path.read_text(encoding="utf-8")
text = text.replace("images_Lesson_07/", "images_Lesson_04_Operators/")
path.write_text(text, encoding="utf-8")