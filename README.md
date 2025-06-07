# LOLPython - Інтерпретатор LOLCODE на Python

LOLPython — це простий інтерпретатор для підмножини мови програмування [LOLCODE 1.2](https://github.com/justinmeza/lolcode-spec/blob/master/v1.2/lolcode-spec-v1.2.md), написаний на Python.

Проєкт включає лексер, парсер (що будує AST) та інтерпретатор, який виконує код.

**[Посилання на дизайн-документ](DESIGN.md)**

## Підтримувані можливості

*   Структура програми: `HAI 1.2` / `KTHXBYE`
*   Коментарі: `BTW ...`
*   Змінні: `I HAS A`, `ITZ`, `R`
*   Типи: `NUMBR`, `YARN`, `TROOF`, `NOOB`
*   Виведення: `VISIBLE`
*   Арифметика: `SUM OF`, `DIFF_OF`, `PRODUKT OF`, `QUOSHUNT OF`
*   Порівняння: `BOTH SAEM`, `DIFFRINT`

## Встановлення

1.  Клонуйте репозиторій:
    ```bash
    git clone https://your-repo-url/lolpython.git
    cd lolpython
    ```

2.  (Рекомендовано) Створіть та активуйте віртуальне середовище:
    ```bash
    python -m venv venv
    source venv/bin/activate  # для Linux/macOS
    # venv\Scripts\activate    # для Windows
    ```

3.  Встановіть залежності для розробки (pytest):
    ```bash
    pip install pytest
    ```

## Використання

Щоб запустити LOLCODE файл, використовуйте головний модуль `lolpython.main`:

```bash
python -m lolpython.main examples/hello.lol