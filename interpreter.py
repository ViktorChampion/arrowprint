import sys
import random

def run_arrowprint(code_str):
    # Создаем сетку
    lines = code_str.split('\n')
    grid = []
    for line in lines:
        line = line.rstrip()
        if line:
            grid.append(list(line))
    
    if not grid:
        return
    
    max_y = len(grid)
    max_x = max(len(row) for row in grid)
    for row in grid:
        while len(row) < max_x:
            row.append(' ')
    
    # Стеки
    stack = []
    string_stack = []
    list_stack = []
    
    # Находим старт
    x, y = 0, 0
    dx, dy = 1, 0
    found = False
    
    for y in range(max_y):
        for x in range(max_x):
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
    
    steps = 0
    
    while steps < 100000:
        steps += 1
        
        if y >= max_y or x >= max_x or y < 0 or x < 0:
            break
        
        char = grid[y][x]
        
        # === НАВИГАЦИЯ ===
        if char == '>':
            dx, dy = 1, 0
        elif char == '<':
            dx, dy = -1, 0
        elif char == '^':
            dx, dy = 0, -1
        elif char == 'v':
            dx, dy = 0, 1
        elif char == '/':
            dx, dy = -dy, -dx
        elif char == '\\':
            dx, dy = dy, dx
        elif char == '!':
            dx, dy = -dx, -dy
        elif char == '#':
            nx, ny = x + dx*2, y + dy*2
            if 0 <= ny < max_y and 0 <= nx < max_x:
                x, y = nx, ny
        elif char == '`':
            for ty in range(max_y):
                for tx in range(max_x):
                    if (tx != x or ty != y) and grid[ty][tx] == '`':
                        x, y = tx, ty
                        break
                else:
                    continue
                break
        
        # === СТРОКИ ===
        elif char in ['"', "'"]:
            quote = char
            string = ""
            cx, cy = x + dx, y + dy
            while 0 <= cy < max_y and 0 <= cx < max_x and grid[cy][cx] != quote:
                string += grid[cy][cx]
                cx += dx
                cy += dy
            string_stack.append(string)
            x, y = cx, cy
        
        # === ЧИСЛА ===
        elif char.isdigit() or char == '?':
            num_str = char if char.isdigit() else ''
            cx, cy = x + dx, y + dy
            
            if char == '?':
                num_str = '0.'
                while 0 <= cy < max_y and 0 <= cx < max_x and grid[cy][cx].isdigit():
                    num_str += grid[cy][cx]
                    cx += dx
                    cy += dy
                stack.append(float(num_str))
                x, y = cx - dx, cy - dy
            else:
                while 0 <= cy < max_y and 0 <= cx < max_x and (grid[cy][cx].isdigit() or grid[cy][cx] == '?'):
                    if grid[cy][cx] == '?':
                        num_str += '.'
                        cx += dx
                        cy += dy
                        while 0 <= cy < max_y and 0 <= cx < max_x and grid[cy][cx].isdigit():
                            num_str += grid[cy][cx]
                            cx += dx
                            cy += dy
                        break
                    else:
                        num_str += grid[cy][cx]
                        cx += dx
                        cy += dy
                
                if '.' in num_str:
                    stack.append(float(num_str))
                else:
                    stack.append(int(num_str))
                x, y = cx - dx, cy - dy
        
        # === МАТЕМАТИКА (инфиксная) ===
        elif char in '+-*;%&':
            expr = ""
            cx, cy = x - dx, y - dy
            while 0 <= cy < max_y and 0 <= cx < max_x:
                ch = grid[cy][cx]
                if ch.isdigit() or ch == '?' or (ch == '-' and (cx - dx < 0 or cy - dy < 0 or not grid[cy-dy][cx-dx].isdigit())):
                    expr = ch + expr
                    cx -= dx
                    cy -= dy
                else:
                    break
            
            expr += char
            
            cx, cy = x + dx, y + dy
            while 0 <= cy < max_y and 0 <= cx < max_x:
                ch = grid[cy][cx]
                if ch.isdigit() or ch == '?' or (ch == '-' and (cx + dx >= max_x or cy + dy >= max_y or not grid[cy+dy][cx+dx].isdigit())):
                    expr += ch
                    cx += dx
                    cy += dy
                else:
                    break
            
            try:
                expr_eval = expr.replace(';', '/')
                result = eval(expr_eval)
                stack.append(result)
                x, y = cx - dx, cy - dy
            except:
                pass
        
        # === ТРАНСМУТАЦИЯ ===
        elif char == '@':
            nx, ny = x + dx, y + dy
            if 0 <= ny < max_y and 0 <= nx < max_x:
                spec_char = grid[ny][nx]
                if spec_char in ['!', '$', '?']:
                    content = ""
                    cx, cy = nx + dx, ny + dy
                    while 0 <= cy < max_y and 0 <= cx < max_x:
                        if grid[cy][cx] == '@':
                            break
                        content += grid[cy][cx]
                        cx += dx
                        cy += dy
                    
                    if spec_char == '!':
                        digits = ''.join(c for c in str(content) if c.isdigit())
                        stack.append(int(digits) if digits else 0)
                    elif spec_char == '$':
                        string_stack.append(str(content))
                    elif spec_char == '?':
                        if content.isdigit():
                            list_stack.append([int(content)])
                        elif '.' in content:
                            list_stack.append([float(content)])
                        else:
                            list_stack.append([content])
                    
                    x, y = cx, cy
                else:
                    if string_stack:
                        s = string_stack.pop()
                        digits = ''.join(c for c in s if c.isdigit())
                        stack.append(int(digits) if digits else 0)
                    elif stack:
                        val = stack.pop()
                        string_stack.append(str(val))
                    elif list_stack:
                        val = list_stack.pop()
                        string_stack.append(str(val))
        
        # === ИНВЕРСИЯ ===
        elif char == '~':
            if stack:
                val = stack.pop()
                if isinstance(val, (int, float)):
                    stack.append(-val)
            elif string_stack:
                val = string_stack.pop()
                string_stack.append(val[::-1])
            elif list_stack:
                val = list_stack.pop()
                if isinstance(val, list):
                    list_stack.append(val[::-1])
        
        # === ДЛИНА ===
        elif char == '$':
            nx, ny = x + dx, y + dy
            if 0 <= ny < max_y and 0 <= nx < max_x:
                next_char = grid[ny][nx]
                if next_char.isdigit() or next_char == '?':
                    num_str = ""
                    cx, cy = nx, ny
                    while 0 <= cy < max_y and 0 <= cx < max_x:
                        ch = grid[cy][cx]
                        if ch.isdigit() or ch == '?':
                            num_str += ch
                            cx += dx
                            cy += dy
                        else:
                            break
                    
                    if '.' in num_str:
                        val = float(num_str)
                        str_val = str(val)
                        if '.' in str_val:
                            stack.append(len(str_val.split('.')[1]))
                        else:
                            stack.append(0)
                    else:
                        stack.append(len(num_str))
                    x, y = cx - dx, cy - dy
                elif next_char in ['"', "'"]:
                    quote = next_char
                    cx, cy = nx + dx, ny + dy
                    s = ""
                    while 0 <= cy < max_y and 0 <= cx < max_x and grid[cy][cx] != quote:
                        s += grid[cy][cx]
                        cx += dx
                        cy += dy
                    stack.append(len(s))
                    x, y = cx, cy
                elif next_char == '{':
                    cx, cy = nx, ny
                    balance = 1
                    content = ""
                    cx += dx
                    cy += dy
                    while 0 <= cy < max_y and 0 <= cx < max_x and balance > 0:
                        ch = grid[cy][cx]
                        if ch == '{':
                            balance += 1
                        elif ch == '}':
                            balance -= 1
                        if balance > 0:
                            content += ch
                        cx += dx
                        cy += dy
                    
                    elements = []
                    if content:
                        current = ""
                        depth = 0
                        for c in content:
                            if c == '{':
                                depth += 1
                            elif c == '}':
                                depth -= 1
                            elif c == ',' and depth == 0:
                                elements.append(current.strip())
                                current = ""
                                continue
                            current += c
                        if current:
                            elements.append(current.strip())
                    
                    stack.append(len(elements))
                    x, y = cx - dx, cy - dy
        
        # === ДУБЛИРОВАНИЕ ===
        elif char == ':':
            if stack:
                stack.append(stack[-1])
            elif string_stack:
                string_stack.append(string_stack[-1])
            elif list_stack:
                list_stack.append(list_stack[-1])
        
        # === СПИСКИ ===
        elif char == '{':
            brace_str = ""
            cx, cy = x + dx, y + dy
            balance = 1
            while 0 <= cy < max_y and 0 <= cx < max_x and balance > 0:
                ch = grid[cy][cx]
                if ch == '{':
                    balance += 1
                elif ch == '}':
                    balance -= 1
                if balance > 0:
                    brace_str += ch
                cx += dx
                cy += dy
            
            if '|' in brace_str and '{' not in brace_str:
                try:
                    p1, p2 = brace_str.split('|', 1)
                    v1 = float(p1.strip()) if p1.strip().replace('.', '').isdigit() else (stack.pop() if stack else 0)
                    v2 = float(p2.strip()) if p2.strip().replace('.', '').isdigit() else (stack.pop() if stack else 100)
                    low, high = min(v1, v2), max(v1, v2)
                    if low == int(low) and high == int(high):
                        stack.append(random.randint(int(low), int(high)))
                    else:
                        stack.append(random.uniform(low, high))
                except:
                    stack.append(0)
            else:
                elements = []
                if brace_str:
                    current = ""
                    depth = 0
                    for c in brace_str:
                        if c == '{':
                            depth += 1
                        elif c == '}':
                            depth -= 1
                        elif c == ',' and depth == 0:
                            elements.append(current.strip())
                            current = ""
                            continue
                        current += c
                    if current:
                        elements.append(current.strip())
                
                arr = []
                for elem in elements:
                    if elem.replace('.', '').isdigit():
                        if '.' in elem:
                            arr.append(float(elem))
                        else:
                            arr.append(int(elem))
                    elif (elem.startswith('"') and elem.endswith('"')) or (elem.startswith("'") and elem.endswith("'")):
                        arr.append(elem[1:-1])
                    else:
                        arr.append(elem)
                list_stack.append(arr)
            
            x, y = cx - dx, cy - dy
        
        # === ИНДЕКСАЦИЯ ===
        elif char == '[':
            if not list_stack:
                x, y = x + dx, y + dy
                continue
            
            current = list_stack[-1]
            cx, cy = x, y
            
            while True:
                cx += dx
                cy += dy
                
                coord_str = ""
                while 0 <= cy < max_y and 0 <= cx < max_x and grid[cy][cx] != ']':
                    coord_str += grid[cy][cx]
                    cx += dx
                    cy += dy
                
                if not coord_str:
                    break
                
                try:
                    idx = int(coord_str)
                    if isinstance(current, list) and 0 <= idx < len(current):
                        current = current[idx]
                    else:
                        break
                except:
                    break
                
                nx, ny = cx + dx, cy + dy
                if 0 <= ny < max_y and 0 <= nx < max_x and grid[ny][nx] == '[':
                    cx, cy = nx, ny
                    continue
                else:
                    x, y = cx, cy
                    break
            
            if isinstance(current, (int, float)):
                stack.append(current)
            else:
                string_stack.append(str(current))
        
        # === УСЛОВИЯ ===
        elif char == '(':
            cond_str = ""
            cx, cy = x + dx, y + dy
            while 0 <= cy < max_y and 0 <= cx < max_x and grid[cy][cx] != ')':
                cond_str += grid[cy][cx]
                cx += dx
                cy += dy
            
            result = False
            cond_str = cond_str.strip()
            
            negated = False
            if cond_str.startswith('№'):
                negated = True
                cond_str = cond_str[1:].strip()
            
            if cond_str.startswith('{') and cond_str.endswith('}') and '?' in cond_str:
                try:
                    inner = cond_str[1:-1].strip()
                    p1, p2 = inner.split('?', 1)
                    weight_true = float(p1.strip()) if p1.strip().replace('.', '').isdigit() else 1
                    weight_false = float(p2.strip()) if p2.strip().replace('.', '').isdigit() else 1
                    total = weight_true + weight_false
                    if total > 0:
                        result = random.random() < (weight_true / total)
                except:
                    result = False
            elif cond_str.startswith('/'):
                divisor = float(cond_str[1:]) if cond_str[1:].replace('.', '').isdigit() else 2
                if stack:
                    result = (stack[-1] % divisor == 0)
            elif '>' in cond_str:
                p1, p2 = cond_str.split('>', 1)
                v1 = float(p1.strip()) if p1.strip().replace('.', '').isdigit() else (stack[-1] if stack else 0)
                v2 = float(p2.strip()) if p2.strip().replace('.', '').isdigit() else 0
                result = v1 > v2
            elif '<' in cond_str:
                p1, p2 = cond_str.split('<', 1)
                v1 = float(p1.strip()) if p1.strip().replace('.', '').isdigit() else (stack[-1] if stack else 0)
                v2 = float(p2.strip()) if p2.strip().replace('.', '').isdigit() else 0
                result = v1 < v2
            elif '=' in cond_str:
                p1, p2 = cond_str.split('=', 1)
                v1 = float(p1.strip()) if p1.strip().replace('.', '').isdigit() else (stack[-1] if stack else 0)
                v2 = float(p2.strip()) if p2.strip().replace('.', '').isdigit() else 0
                result = v1 == v2
            
            if negated:
                result = not result
            
            if result:
                if 0 <= cy < max_y and 0 <= cx < max_x:
                    x, y = cx - dx, cy - dy
            else:
                dx, dy = -dy, dx
                if 0 <= cy < max_y and 0 <= cx < max_x:
                    x, y = cx - dx, cy - dy
        
        # === ВВОД/ВЫВОД ===
        elif char == '.':
            if string_stack:
                print(string_stack.pop(), end="", flush=True)
            elif stack:
                print(stack[-1], end="", flush=True)
            elif list_stack:
                print(list_stack[-1], end="", flush=True)
            else:
                print("", end="", flush=True)
        
        elif char == ',':
            try:
                user_input = input()
            except EOFError:
                user_input = ""
            
            if user_input.replace('.', '').replace('-', '').isdigit():
                if '.' in user_input:
                    stack.append(float(user_input))
                else:
                    stack.append(int(user_input))
            else:
                string_stack.append(user_input)
        
        # === UNICODE ===
        elif char == '∑':
            if list_stack:
                arr = list_stack.pop()
                if isinstance(arr, list):
                    stack.append(sum(arr))
                else:
                    stack.append(0)
        
        elif char == '∏':
            if list_stack:
                arr = list_stack.pop()
                if isinstance(arr, list):
                    result = 1
                    for item in arr:
                        result *= item
                    stack.append(result)
                else:
                    stack.append(0)
        
        elif char == '∞':
            stack.append(float('inf'))
        
        # === СПЕЦИАЛЬНЫЕ ===
        elif char == '_':
            nx, ny = x + dx*3, y + dy*3
            if 0 <= ny < max_y and 0 <= nx < max_x:
                x, y = nx, ny
        
        elif char == '|':
            while y < max_y:
                x += dx
                if x >= max_x or x < 0:
                    x = 0 if dx > 0 else max_x - 1
                    y += dy
                    if y >= max_y or y < 0:
                        break
                if grid[y][x] == '\n' or x == 0 or x == max_x - 1:
                    break
        
        elif char == ' ':
            pass
        
        # === ОСТАНОВКА ===
        if char == '@' and 0 <= y+dy < max_y and 0 <= x+dx < max_x and grid[y+dy][x+dx] == '@':
            break
        
        # === ДВИЖЕНИЕ ===
        new_x, new_y = x + dx, y + dy
        if 0 <= new_y < max_y and 0 <= new_x < max_x:
            x, y = new_x, new_y
        else:
            break

if __name__ == "__main__":
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r', encoding='utf-8') as f:
            code = f.read()
        run_arrowprint(code)
    else:
        print("Usage: python script.py <filename>")
