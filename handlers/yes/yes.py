# CatOS-type package
author = "Anton2319"
mode = "="
deps = 'None'
description = 'Пизда'

yestrue = True if len(re.findall(r"[дДdD][AАаа]*[^\wБ-Яб-яёЁ]{0,1}$", text.split("\n")[-1])) == 1 else False
if yestrue:
    print("yestruecorrect")
    message("Пизда")