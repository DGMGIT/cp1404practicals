"""
CP1404/CP5632 Practical
Programming Language
Daniel Mackenzie
"""

from prac_06.programming_language import ProgrammingLanguage


ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

types = [ruby, python, visual_basic]

print(ruby)
print(python)
print(visual_basic)

print("The dynamically typed languages are:")
for type in types:
    if type.is_dynamic():
        print(type.field)
