# ArrowPrint

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Python](https://img.shields.io/badge/python-3.6+-green)
![License](https://img.shields.io/badge/license-MIT-green)
![Platform](https://img.shields.io/badge/platform-Windows-lightgrey)

**ArrowPrint** is an esoteric programming language inspired by 2D languages such as Befunge. The program is a two-dimensional grid of characters, and execution is performed by moving through this grid in a specific direction. The language is based on a stack architecture and includes many operators for navigation, stack operations, arithmetic, conditionals, and type conversions.

---

## Language Guide

### Navigation
| Symbol | Description |
|--------|-------------|
| `>` | Move right |
| `<` | Move left |
| `^` | Move up |
| `v` | Move down |
| `/` | Mirror (reflect direction) |
| `\` | Mirror (reflect direction) |
| `(x,y)` | Teleport to specified coordinates. Relative coordinates are supported, e.g., `(+2,-3)` |

### Stack Operations
| Symbol | Description |
|--------|-------------|
| `?` | Print the top element (without newline) |
| `'` | Remove the top element |
| `:` | Duplicate the top element |
| `~` | Invert: number becomes negative, string is reversed |
| `$` | Length of string or number of digits in a number |
| `!` | Explode: split value into individual characters/digits |
| `_` | Assemble: concatenate all stack elements into a single string |
| `∑` | Sum of all numbers in the stack |
| `∏` | Product of all numbers in the stack |
| `∞` | Push infinity (`inf`) onto the stack |

### Arithmetic Operations
| Symbol | Description |
|--------|-------------|
| `+` | Addition |
| `-` | Subtraction |
| `*` | Multiplication |
| `**` | Exponentiation |
| `;` | Division |
| `%` | Modulo (remainder) |
| `&` | Bitwise AND |
| `\|` | Bitwise OR |
| `√` | Root. If there are two numbers on the stack — root `a` of `b` (`a b √`). If one — square root |

### Conditionals
| Symbol | Description |
|--------|-------------|
| `{` `}` | Conditional block. The condition is written inside. If true — executes the code inside, otherwise — moves to the next line |

#### Conditions:
| Syntax | Description |
|--------|-------------|
| `{=10}` | Equal to 10 |
| `{==}` | Compare the top two stack elements |
| `{=}` | Loose equality (type coercion) |
| `{<5}` | Less than 5 |
| `{>3}` | Greater than 3 |
| `{<}` | Less than (compare top two elements) |
| `{>}` | Greater than (compare top two elements) |
| `{;2}` | Divisible by 2 (remainder 0) |
| `{№"abc"}` | Check if a substring exists in a string |
| `{}` | Not equal to 0 or non-empty string |

### Indexing and Slices
| Syntax | Description |
|--------|-------------|
| `(n)` | Get element at index `n` and push to the top |
| `(-1)` | Last element |
| `(start:end)` | Get a slice and push to the top |
| `(start:end:step)` | Get a slice with step |
| `[n]` | Indexing while preserving order (the taken element is pushed to the top) |

### Input and Output
| Symbol | Description |
|--------|-------------|
| `,` | Read a string from the keyboard |
| `?` | Print the top element |
| `₽` | Print the top element as an ASCII character |

### Type Conversions (with modifiers)
| Command | Description |
|---------|-------------|
| `@!` | Convert to integer |
| `@$` | Convert to string |
| `@?` | Convert to float |
| `@~` | Auto-conversion (legacy behavior) |

### Other Commands
| Symbol | Description |
|--------|-------------|
| `#` | Comment (ignored until end of line) |
| `@@` | Stop program execution |
| `` ` `` | Generate a random number. Usage: `min max \`` |
| `(a\|b)` | Generate a random number from `a` to `b` |

---

### Examples Programs

#### Hello, World

> "Hello, World!"?@@

#### Calculator

> "First number: "?,"Second number: "?,+?@@

#### Random Number

> (1|100)?@@

---

## Installation

### Requirements
- Python 3.6 or higher

### Windows Installation
1. Download the installer
2. Run `install_arrowprint.bat` as administrator
3. Restart your command prompt

---

## License

MIT

---

## Links

- GitHub: [your-repo-link]
- Documentation: [your-docs-link]
- Community: [your-discord/telegram]

---

**Happy programming with ArrowPrint!** 🚀

---

---

# ArrowPrint (Русская версия)

**ArrowPrint** — это эзотерический язык программирования, вдохновлённый двумерными языками, такими как Befunge. Программа представляет собой двумерную сетку символов, а выполнение происходит путём перемещения по этой сетке в определённом направлении. Язык основан на стековой архитектуре и включает множество операторов для навигации, работы со стеком, математических вычислений, условных переходов и преобразования типов.

---

## Руководство по языку

### Навигация
| Символ | Описание |
|--------|----------|
| `>` | Движение вправо |
| `<` | Движение влево |
| `^` | Движение вверх |
| `v` | Движение вниз |
| `/` | Зеркало (отражение направления) |
| `\` | Зеркало (отражение направления) |
| `(x,y)` | Телепорт на указанные координаты. Поддерживаются относительные координаты, например `(+2,-3)` |

### Работа со стеком
| Символ | Описание |
|--------|----------|
| `?` | Вывод верхнего элемента стека (без перевода строки) |
| `'` | Удаление верхнего элемента стека |
| `:` | Дублирование верхнего элемента стека |
| `~` | Инверсия: число меняет знак, строка разворачивается |
| `$` | Длина строки или количества цифр числа |
| `!` | Взрыв: разбивает значение на отдельные символы/цифры |
| `_` | Сборка: объединяет все элементы стека в одну строку |
| `∑` | Сумма всех чисел в стеке |
| `∏` | Произведение всех чисел в стеке |
| `∞` | Положить бесконечность (`inf`) в стек |

### Математические операции
| Символ | Описание |
|--------|----------|
| `+` | Сложение |
| `-` | Вычитание |
| `*` | Умножение |
| `**` | Возведение в степень |
| `;` | Деление |
| `%` | Остаток от деления |
| `&` | Побитовое И |
| `\|` | Побитовое ИЛИ |
| `√` | Корень. Если в стеке два числа — корень степени a из b (`a b √`). Если одно — квадратный корень |

### Условные операторы
| Символ | Описание |
|--------|----------|
| `{` `}` | Условный блок. Внутри указывается условие. Если условие истинно — выполняется код внутри, иначе — переход на следующую строку |

#### Условия:
| Синтаксис | Описание |
|-----------|----------|
| `{=10}` | Равно 10 |
| `{==}` | Сравнение двух верхних элементов стека |
| `{=}` | Нестрогое сравнение (приводит типы) |
| `{<5}` | Меньше 5 |
| `{>3}` | Больше 3 |
| `{<}` | Меньше (сравнение двух верхних элементов) |
| `{>}` | Больше (сравнение двух верхних элементов) |
| `{;2}` | Делится на 2 (остаток 0) |
| `{№"abc"}` | Проверка вхождения подстроки в строку |
| `{}` | Не равно 0 или не пустая строка |

### Индексация и срезы
| Синтаксис | Описание |
|-----------|----------|
| `(n)` | Взять элемент по индексу `n` и положить наверх стека |
| `(-1)` | Последний элемент |
| `(start:end)` | Взять срез и положить наверх |
| `(start:end:step)` | Взять срез с шагом |
| `[n]` | Индексация с сохранением порядка (взятый элемент кладётся наверх) |

### Ввод и вывод
| Символ | Описание |
|--------|----------|
| `,` | Ввод строки с клавиатуры |
| `?` | Вывод верхнего элемента стека |
| `₽` | Вывод верхнего элемента как ASCII-символ |

### Преобразование типов (с модификаторами)
| Команда | Описание |
|---------|----------|
| `@!` | Преобразовать в целое число |
| `@$` | Преобразовать в строку |
| `@?` | Преобразовать в число с плавающей точкой |
| `@~` | Авто-преобразование (старое поведение) |

### Прочие команды

| Символ | Описание |
|--------|----------|

| `#` | Комментарий (игнорируется до конца строки) |
| `@@` | Остановка выполнения программы |
| `` ` `` | Генерация случайного числа. Использование: `минимум максимум \`` |
| `(a\|b)` | Генерация случайного числа от a до b |

---

### Примеры программ

#### Привет, мир

> "Hello, World!"?@@

#### Калькулятор

> "First number: "?,"Second number: "?,+?@@

#### Случайное число

> (1|100)?@@

---

## Установка

### Требования

- Python 3.6 или выше

### Установка на Windows

1. Скачайте установщик
2. Запустите `install_arrowprint.bat` от имени администратора
3. Перезапустите командную строку

---

## Лицензия

MIT

---

## Ссылки

- GitHub: [ссылка на репозиторий]
- Документация: [ссылка на документацию]
- Сообщество: [ссылка на Discord/Telegram]

---

**Удачи в программировании на ArrowPrint!** 🚀
