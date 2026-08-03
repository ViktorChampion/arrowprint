import sys
import random

def run_arrowprint(code_str):
    lines = code_str.split('\n')
    grid = []
    for line in lines:
        if line.rstrip():
            grid.append(list(line.rstrip()))
    
    if not grid:
        return
    
    def ensure(y, x):
        if y < 0 or x < 0:
            return
        while y >= len(grid):
            grid.append([])
        while x >= len(grid[y]):
            grid[y].append(' ')
    
    stack = []
    
    # Находим старт
    x, y = 0, 0
    dx, dy = 1, 0
    found = False
    
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == '>':
                dx, dy = 1, 0
                found = True
                break
            elif grid[y][x] == '<':
                dx, dy = -1, 0
                found = True
                break
            elif grid[y][x] == '^':
                dx, dy = 0, -1
                found = True
                break
            elif grid[y][x] == 'v':
                dx, dy = 0, 1
                found = True
                break
        if found:
            break
    
    if not found:
        return
    
    def parse_string(text):
        result = ""
        i = 0
        while i < len(text):
            if text[i] == '\\' and i + 1 < len(text):
                esc = text[i + 1]
                if esc == 'n':
                    result += '\n'
                elif esc == 't':
                    result += '\t'
                elif esc == '\\':
                    result += '\\'
                elif esc == '"':
                    result += '"'
                i += 2
            else:
                result += text[i]
                i += 1
        return result
    
    try:
        while True:
            ensure(y, x)
            c = grid[y][x]
            
            # === НАВИГАЦИЯ (7 символов) ===
            if c == '>':
                dx, dy = 1, 0
            elif c == '<':
                dx, dy = -1, 0
            elif c == '^':
                dx, dy = 0, -1
            elif c == 'v':
                dx, dy = 0, 1
            elif c == '/':
                dx, dy = -dy, -dx
            elif c == '\\':
                dx, dy = dy, dx
            
            # === ТЕЛЕПОРТАЦИЯ, РАНДОМ, ИНДЕКСАЦИЯ И СРЕЗЫ ( ) ===
            elif c == '(':
                cx, cy = x + dx, y + dy
                content = ""
                
                # Читаем содержимое скобок
                while True:
                    ensure(cy, cx)
                    if grid[cy][cx] == ')':
                        break
                    content += grid[cy][cx]
                    cx += dx
                    cy += dy
                
                content = content.strip()
                
                # 1. РАНДОМ (число|число)
                if '|' in content:
                    parts = content.split('|')
                    if len(parts) == 2:
                        try:
                            a = int(parts[0].strip()) if parts[0].strip() else 0
                            b = int(parts[1].strip()) if parts[1].strip() else 9
                            if a <= b:
                                stack.append(random.randint(a, b))
                            else:
                                stack.append(random.randint(b, a))
                        except:
                            stack.append(0)
                        x, y = cx, cy
                        continue
                
                # 2. ТЕЛЕПОРТАЦИЯ (число,число)
                elif ',' in content:
                    parts = content.split(',')
                    if len(parts) == 2:
                        xp = parts[0].strip()
                        yp = parts[1].strip()
                        
                        if xp.startswith('+') or xp.startswith('-'):
                            x += int(xp)
                        else:
                            x = int(xp)
                        
                        if yp.startswith('+') or yp.startswith('-'):
                            y += int(yp)
                        else:
                            y = int(yp)
                        
                        if y >= 0 and x >= 0:
                            ensure(y, x)
                        x, y = cx, cy
                        continue
                
                # 3. ИНДЕКСАЦИЯ И СРЕЗЫ
                else:
                    # СРЕЗ (начало:конец:шаг)
                    if ':' in content:
                        parts = content.split(':')
                        
                        # Парсим значения
                        start = int(parts[0].strip()) if parts[0].strip() else 0
                        end = int(parts[1].strip()) if len(parts) > 1 and parts[1].strip() else len(stack)
                        step = int(parts[2].strip()) if len(parts) > 2 and parts[2].strip() else 1
                        
                        # Отрицательные индексы
                        if start < 0:
                            start = len(stack) + start
                        if end < 0:
                            end = len(stack) + end
                        
                        # Берем срез и перемещаем в конец
                        if 0 <= start < len(stack) and 0 <= end <= len(stack):
                            sliced = stack[start:end:step]
                            del stack[start:end:step]
                            stack.extend(sliced)
                    
                    # ОДИНОЧНЫЙ ИНДЕКС
                    else:
                        try:
                            idx = int(content)
                            if idx < 0:
                                idx = len(stack) + idx
                            if 0 <= idx < len(stack):
                                val = stack.pop(idx)
                                stack.append(val)
                            else:
                                stack.append(0)
                        except:
                            stack.append(0)
                    
                    x, y = cx, cy
                    continue
            
            # === ИНДЕКСАЦИЯ [ ] ===
            elif c == '[':
                cx, cy = x + dx, y + dy
                idx = ""
                while True:
                    ensure(cy, cx)
                    if grid[cy][cx] == ']':
                        break
                    idx += grid[cy][cx]
                    cx += dx
                    cy += dy
                
                idx = idx.strip()
                
                has_arrow = False
                px, py = x - dx, y - dy
                if py >= 0 and px >= 0:
                    ensure(py, px)
                    if grid[py][px] in '><^v':
                        has_arrow = True
                
                if has_arrow:
                    if ':' in idx:
                        parts = idx.split(':')
                        s = int(parts[0]) if parts[0].strip() else 0
                        e = int(parts[1]) if len(parts) > 1 and parts[1].strip() else len(stack)
                        st = int(parts[2]) if len(parts) > 2 and parts[2].strip() else 1
                        if s < 0:
                            s = len(stack) + s
                        if e < 0:
                            e = len(stack) + e
                        sliced = stack[s:e:st]
                        del stack[s:e:st]
                        for item in sliced:
                            stack.append(item)
                    else:
                        try:
                            i = int(idx)
                            if i < 0:
                                i = len(stack) + i
                            if 0 <= i < len(stack):
                                val = stack.pop(i)
                                stack.append(val)
                        except:
                            pass
                else:
                    if stack:
                        last = stack.pop()
                        if isinstance(last, str):
                            if ':' in idx:
                                parts = idx.split(':')
                                s = int(parts[0]) if parts[0].strip() else 0
                                e = int(parts[1]) if len(parts) > 1 and parts[1].strip() else len(last)
                                st = int(parts[2]) if len(parts) > 2 and parts[2].strip() else 1
                                stack.append(last[s:e:st])
                            else:
                                try:
                                    i = int(idx)
                                    if 0 <= i < len(last):
                                        stack.append(last[i])
                                    else:
                                        stack.append("")
                                except:
                                    stack.append("")
                        else:
                            sv = str(last)
                            if ':' in idx:
                                parts = idx.split(':')
                                s = int(parts[0]) if parts[0].strip() else 0
                                e = int(parts[1]) if len(parts) > 1 and parts[1].strip() else len(sv)
                                st = int(parts[2]) if len(parts) > 2 and parts[2].strip() else 1
                                r = sv[s:e:st]
                                try:
                                    stack.append(int(r) if r.isdigit() else r)
                                except:
                                    stack.append(r)
                            else:
                                try:
                                    i = int(idx)
                                    if 0 <= i < len(sv):
                                        stack.append(sv[i])
                                    else:
                                        stack.append("")
                                except:
                                    stack.append("")
                    else:
                        stack.append("")
                
                x, y = cx, cy
                continue
            
            # === ВЫВОД (1 символ) ===
            elif c == '?':
                if stack:
                    print(stack.pop(), end="", flush=True)
            
            # === УДАЛЕНИЕ БЕЗ ВЫВОДА (1 символ) ===
            elif c == '\'':
                if stack:
                    stack.pop()
            
            # === ДУБЛИРОВАНИЕ (1 символ) ===
            elif c == ':':
                if stack:
                    stack.append(stack[-1])
            
            # === ИНВЕРТ (1 символ) ===
            elif c == '~':
                if stack:
                    v = stack.pop()
                    if isinstance(v, (int, float)):
                        stack.append(-v)
                    else:
                        stack.append(str(v)[::-1])
            
            # === ДЛИНА (1 символ) ===
            elif c == '$':
                if stack:
                    v = stack.pop()
                    stack.append(len(str(v)))
            
            # === ВЗРЫВ (1 символ) ===
            elif c == '!':
                if stack:
                    v = stack.pop()
                    for ch in str(v):
                        if ch.isdigit():
                            stack.append(int(ch))
                        else:
                            stack.append(ch)
            
            # === СБОРКА (1 символ) ===
            elif c == '_':
                if stack:
                    tmp = []
                    while stack:
                        tmp.append(stack.pop())
                    tmp.reverse()
                    result = ""
                    for v in tmp:
                        result += str(v)
                    stack.append(result)
            
            # === СТЕПЕНЬ (**) ===
            elif c == '*' and x + 1 < len(grid[y]) and grid[y][x + 1] == '*':
                if len(stack) >= 2:
                    a = stack.pop()
                    b = stack.pop()
                    try:
                        an = float(a) if not isinstance(a, (int, float)) else a
                        bn = float(b) if not isinstance(b, (int, float)) else b
                        stack.append(bn ** an)
                    except:
                        stack.append(b)
                        stack.append(a)
                    x, y = x + 1, y
                    continue
            
            # === КОРЕНЬ (√) ===
            elif c == '√':
                if len(stack) >= 2:
                    a = stack.pop()
                    b = stack.pop()
                    try:
                        an = float(a) if not isinstance(a, (int, float)) else a
                        bn = float(b) if not isinstance(b, (int, float)) else b
                        if an != 0:
                            result = bn ** (1.0 / an)
                            stack.append(result)
                        else:
                            stack.append(0)
                    except:
                        stack.append(b)
                        stack.append(a)
                elif stack:
                    v = stack.pop()
                    try:
                        vn = float(v) if not isinstance(v, (int, float)) else v
                        stack.append(vn ** 0.5)
                    except:
                        stack.append(v)
            
            # === МАТЕМАТИКА (7 символов) ===
            elif c in '+-*;%&|':
                if len(stack) >= 2:
                    a = stack.pop()
                    b = stack.pop()
                    
                    try:
                        an = float(a) if not isinstance(a, (int, float)) else a
                        bn = float(b) if not isinstance(b, (int, float)) else b
                    except:
                        stack.append(b)
                        stack.append(a)
                        continue
                    
                    if c == '+':
                        stack.append(bn + an)
                    elif c == '-':
                        stack.append(bn - an)
                    elif c == '*':
                        stack.append(bn * an)
                    elif c == ';':
                        if an != 0:
                            stack.append(bn / an)
                        else:
                            stack.append(0)
                    elif c == '%':
                        if an != 0:
                            stack.append(bn % an)
                        else:
                            stack.append(0)
                    elif c == '&':
                        stack.append(int(bn) & int(an))
                    elif c == '|':
                        stack.append(int(bn) | int(an))
            
            # === СТРОКИ (1 символ - только ") ===
            elif c == '"':
                q = c
                s = ""
                cx, cy = x + dx, y + dy
                while True:
                    ensure(cy, cx)
                    if grid[cy][cx] == q:
                        break
                    s += grid[cy][cx]
                    cx += dx
                    cy += dy
                
                s = parse_string(s)
                stack.append(s)
                x, y = cx, cy
            
            # === ЧИСЛА ===
            elif c.isdigit():
                num_str = c
                cx, cy = x + dx, y + dy
                
                while True:
                    if cy < 0 or cx < 0 or cy >= len(grid) or cx >= len(grid[cy]):
                        break
                    ch = grid[cy][cx]
                    if ch.isdigit():
                        num_str += ch
                        cx += dx
                        cy += dy
                    elif ch == '.':
                        num_str += '.'
                        cx += dx
                        cy += dy
                        while True:
                            if cy < 0 or cx < 0 or cy >= len(grid) or cx >= len(grid[cy]):
                                break
                            ch2 = grid[cy][cx]
                            if ch2.isdigit():
                                num_str += ch2
                                cx += dx
                                cy += dy
                            else:
                                break
                        break
                    else:
                        break
                
                try:
                    stack.append(float(num_str) if '.' in num_str else int(num_str))
                except:
                    stack.append(0)
                
                x, y = cx - dx, cy - dy
            
            # === УСЛОВИЯ { } ===
            elif c == '{':
                start_x, start_y = x, y
                cx, cy = x + dx, y + dy
                cond = ""
                while True:
                    ensure(cy, cx)
                    if grid[cy][cx] == '}':
                        break
                    cond += grid[cy][cx]
                    cx += dx
                    cy += dy
                
                cond = cond.strip()
                result = False
                
                # === № (вхождение) ===
                if cond.startswith('№'):
                    rest = cond[1:].strip()
                    
                    if rest and stack:
                        last = str(stack[-1])
                        
                        if rest.startswith('"') and rest.endswith('"'):
                            rest = rest[1:-1]
                        
                        if cond.startswith('№№'):
                            result = rest in last
                        else:
                            result = rest.lower() in last.lower()
                    elif len(stack) >= 2:
                        a = str(stack[-2])
                        b = str(stack[-1])
                        if cond.startswith('№№'):
                            result = b in a
                        else:
                            result = b.lower() in a.lower()
                
                # === == (строгое сравнение) ===
                elif cond.startswith('=='):
                    rest = cond[2:].strip()
                    if rest and stack:
                        last = stack[-1]
                        if rest.startswith('"') and rest.endswith('"'):
                            rest = rest[1:-1]
                            rest = parse_string(rest)
                            result = str(last) == rest
                        else:
                            try:
                                result = float(last) == float(rest)
                            except:
                                result = False
                    elif len(stack) >= 2:
                        result = str(stack[-2]) == str(stack[-1])
                
                # === = (нестрогое сравнение) ===
                elif cond.startswith('='):
                    rest = cond[1:].strip()
                    if rest and stack:
                        last = stack[-1]
                        if rest.startswith('"') and rest.endswith('"'):
                            rest = rest[1:-1]
                            rest = parse_string(rest)
                            result = str(last).lower() == rest.lower()
                        else:
                            try:
                                val = float(rest)
                                last_num = float(last) if not isinstance(last, (int, float)) else last
                                result = float(last_num) == float(val)
                            except:
                                result = False
                    elif len(stack) >= 2:
                        a = stack[-2]
                        b = stack[-1]
                        try:
                            result = float(a) == float(b)
                        except:
                            result = str(a).lower() == str(b).lower()
                
                # === < (меньше) ===
                elif cond.startswith('<'):
                    rest = cond[1:].strip()
                    if rest and stack:
                        try:
                            val = float(rest)
                            last = stack[-1]
                            result = float(last) < val
                        except:
                            result = False
                    elif len(stack) >= 2:
                        try:
                            result = float(stack[-2]) < float(stack[-1])
                        except:
                            result = False
                
                # === > (больше) ===
                elif cond.startswith('>'):
                    rest = cond[1:].strip()
                    if rest and stack:
                        try:
                            val = float(rest)
                            last = stack[-1]
                            result = float(last) > val
                        except:
                            result = False
                    elif len(stack) >= 2:
                        try:
                            result = float(stack[-2]) > float(stack[-1])
                        except:
                            result = False
                
                # === ; (делимость) ===
                elif cond.startswith(';'):
                    rest = cond[1:].strip()
                    if rest and stack:
                        try:
                            val = float(rest)
                            last = stack[-1]
                            if val != 0:
                                result = (float(last) / val) % 1 == 0
                        except:
                            result = False
                    elif len(stack) >= 2:
                        try:
                            a = float(stack[-2])
                            b = float(stack[-1])
                            if b != 0:
                                result = (a / b) % 1 == 0
                        except:
                            result = False
                
                # === {} (проверка на != 0) ===
                else:
                    if stack:
                        last = stack[-1]
                        try:
                            result = float(last) != 0
                        except:
                            result = str(last) != ""
                
                if result:
                    x, y = cx, cy
                else:
                    dx, dy = 0, 1
                    x, y = start_x, start_y + 1
                    if y >= 0 and x >= 0:
                        ensure(y, x)

            # === СУММА (1 символ) ===
            elif c == '∑':
                if stack:
                    nums = []
                    tmp = []
                    while stack:
                        v = stack.pop()
                        tmp.append(v)
                        if isinstance(v, (int, float)):
                            nums.append(v)
                    tmp.reverse()
                    stack.extend(tmp)
                    stack.append(sum(nums) if nums else 0)
            
            # === ПРОИЗВЕДЕНИЕ (1 символ) ===
            elif c == '∏':
                if stack:
                    nums = []
                    tmp = []
                    while stack:
                        v = stack.pop()
                        tmp.append(v)
                        if isinstance(v, (int, float)):
                            nums.append(v)
                    tmp.reverse()
                    stack.extend(tmp)
                    r = 1
                    for n in nums:
                        r *= n
                    stack.append(r if nums else 0)
            
            # === БЕСКОНЕЧНОСТЬ (1 символ) ===
            elif c == '∞':
                stack.append(float('inf'))
            
            # === ВВОД (1 символ) ===
            elif c == ',':
                try:
                    inp = input()
                except EOFError:
                    inp = ""
                if inp.replace('.', '').replace('-', '').isdigit():
                    stack.append(float(inp) if '.' in inp else int(inp))
                else:
                    stack.append(inp)
            
            # === ВЫВОД КАК ASCII (символ) ===
            elif c == '₽':
                if stack:
                    v = stack.pop()
                    try:
                        code = int(float(v)) if not isinstance(v, (int, float)) else int(v)
                        if 0 <= code <= 127:
                            print(chr(code), end="", flush=True)
                        else:
                            print("?", end="", flush=True)
                    except:
                        print("?", end="", flush=True)
            
            # === РАНДОМ (минимум максимум `) ===
            elif c == '`':
                if len(stack) >= 2:
                    b = stack.pop()
                    a = stack.pop()
                    
                    try:
                        a = int(float(a)) if not isinstance(a, (int, float)) else int(a)
                        b = int(float(b)) if not isinstance(b, (int, float)) else int(b)
                        
                        if a <= b:
                            low, high = a, b
                        else:
                            low, high = b, a
                        
                        stack.append(random.randint(low, high))
                    except:
                        stack.append(0)
            
            # === КОММЕНТАРИЙ (1 символ) ===
            elif c == '#':
                while y < len(grid) and x < len(grid[y]):
                    x += dx
                    if x < 0 or x >= len(grid[y]):
                        break
                continue
            
            # === ПРОБЕЛ ===
            elif c == ' ':
                pass
            
            # === @ - ПРЕОБРАЗОВАНИЕ И ОСТАНОВКА ===
            elif c == '@':
                # Сначала проверяем, не остановка ли это @@
                nx, ny = x + dx, y + dy
                if ny >= 0 and nx >= 0:
                    ensure(ny, nx)
                    if grid[ny][nx] == '@':
                        break
                
                # Если не остановка - проверяем модификаторы
                if stack:
                    v = stack.pop()
                    nx, ny = x + dx, y + dy
                    if ny >= 0 and nx >= 0:
                        ensure(ny, nx)
                        mod = grid[ny][nx]
                        
                        # @! - преобразование в целое число
                        if mod == '!':
                            try:
                                if isinstance(v, str):
                                    if v.isdigit():
                                        stack.append(int(v))
                                    else:
                                        stack.append(0)
                                elif isinstance(v, float):
                                    stack.append(int(v))
                                else:
                                    stack.append(int(v))
                            except:
                                stack.append(0)
                            x, y = nx, ny
                            continue
                        
                        # @$ - преобразование в строку
                        elif mod == '$':
                            stack.append(str(v))
                            x, y = nx, ny
                            continue
                        
                        # @? - преобразование в число с плавающей точкой
                        elif mod == '?':
                            try:
                                if isinstance(v, str):
                                    digits = ''.join(ch for ch in v if ch.isdigit())
                                    if '.' in v:
                                        parts = v.split('.')
                                        left_digits = ''.join(ch for ch in parts[0] if ch.isdigit())
                                        right_digits = ''.join(ch for ch in parts[1] if ch.isdigit()) if len(parts) > 1 else ''
                                        
                                        if left_digits or right_digits:
                                            num_str = (left_digits if left_digits else '0') + '.' + (right_digits if right_digits else '0')
                                            stack.append(float(num_str))
                                        else:
                                            stack.append(0.0)
                                    elif digits:
                                        stack.append(float(digits + '.0'))
                                    else:
                                        stack.append(0.0)
                                elif isinstance(v, int):
                                    stack.append(float(v))
                                else:
                                    stack.append(float(v))
                            except:
                                stack.append(0.0)
                            x, y = nx, ny
                            continue
                        # @~ - старое поведение (авто-преобразование)
                        elif mod == '~':
                            if isinstance(v, (int, float)):
                                stack.append(str(v))
                            else:
                                try:
                                    stack.append(float(str(v)) if '.' in str(v) else int(str(v)))
                                except:
                                    stack.append(v)
                            x, y = nx, ny
                            continue
                        
                        # Если модификатор не распознан - пропускаем
                        else:
                            stack.append(v)
                            x, y = nx, ny
                            continue
                    else:
                        stack.append(v)
            
            # === ДВИЖЕНИЕ ===
            nx, ny = x + dx, y + dy
            if ny >= 0 and nx >= 0:
                ensure(ny, nx)
                x, y = nx, ny
            else:
                break
    except KeyboardInterrupt:
        sys.exit(0)
def main():
    try:
        if len(sys.argv) > 1:
            # Режим 1: Запуск файла
            with open(sys.argv[1], 'r', encoding='utf-8') as f:
                code = f.read()
            run_arrowprint(code)
        else:
            # Режим 2: Интерактивный режим (REPL)
            print("ArrowPrint Interactive Mode (v1.0)")
            print("Type 'exit' to quit. Use '\\' at end of line for multi-line.")
            print("-" * 40)
            
            while True:
                lines = []
                try:
                    line = input(">>> ")
                    
                    # Проверка на выход
                    if line.strip().lower() in ['exit', 'quit']:
                        print("Goodbye!")
                        break
                    
                    lines.append(line)
                    
                    # Если строка заканчивается на \, продолжаем ввод
                    while line.endswith('\\'):
                        line = input("... ")
                        if line.strip().lower() in ['exit', 'quit']:
                            break
                        lines.append(line)
                    
                    if lines:
                        code = '\n'.join(lines)
                        # Убираем символы \ в конце строк
                        code = code.replace('\\\n', '\n')
                        run_arrowprint(code)
                        print()
                    
                except KeyboardInterrupt:
                    print("\nGoodbye!")
                    break
                except EOFError:
                    print("\nGoodbye!")
                    break
                except Exception as e:
                    print(f"Error: {e}")
                    
    except KeyboardInterrupt:
        sys.exit(0)
    except FileNotFoundError:
        print(f"File not found: {sys.argv[1]}")
        sys.exit(1)
if __name__ == "__main__":
    main()