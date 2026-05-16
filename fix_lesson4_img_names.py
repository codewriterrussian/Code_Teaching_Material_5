from pathlib import Path

path = Path("student_handouts_md/Lesson_04_Operators.md")
text = path.read_text(encoding="utf-8")

for i in range(1, 6):
    text = text.replace(f"lesson7_img{i}.png", f"lesson4_img{i}.png")

path.write_text(text, encoding="utf-8")