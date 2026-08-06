# ArrowPrint

**ArrowPrint** is an esoteric programming language created in 2026. It is inspired by two-dimensional languages such as [[Befunge]], combining stack-based logic, non-linear execution, and minimalist syntax. The language is often described as "Befunge for those who want to write code with style and soul."

According to the author, every ArrowPrint program is not just an algorithm — it's a **journey**. Literally: the code is a two-dimensional grid through which an instruction pointer moves, executing commands along the way. This creates a "quest-like" feel, where the programmer both designs the map and navigates through it.

## Philosophy

ArrowPrint was not built for practical tasks. It was built for **the joy of coding**. It doesn't try to replace Python, C++, or any mainstream language. Its goal is to give the programmer a sense of exploration — where every new program is a maze, and every mistake is not a bug, but an "unexpected route."

*"In ArrowPrint, code is not read top-to-bottom. It is read in whatever direction you choose to go."* — ViktorChampion

## History

The language was originally written with a hard limit of 100,000 commands per program. This limitation was a deliberate design choice to encourage concise and creative coding, forcing programmers to think in terms of efficiency and elegance rather than brute force. While this limit has since been removed in later versions, the philosophy behind it remains: ArrowPrint is about expression, not endless loops.

## Syntax and structure

An ArrowPrint program is a rectangular grid of symbols. Execution begins at the first arrow (`>`, `<`, `^`, or `v`) found in the grid. The instruction pointer moves cell by cell, and each cell contains either a command, data, or a comment.

A key feature of the language is the **absence of explicit blocks**. Branching and loops are implemented through direction changes and conditional jumps (`{ }`).

## Commands

### Navigation
| Symbol | Description |
|--------|-------------|
| `>` | Move right |
| `<` | Move left |
| `^` | Move up |
| `v` | Move down |
| `/` | Mirror (reflect direction) |
| `\` | Mirror (reflect direction) |
| `(x,y)` | Teleport to absolute or relative coordinates (e.g., `(+2,-3)`) |

### Stack Operations
| Symbol | Description |
|--------|-------------|
| `?` | Print top of stack (no newline) |
| `'` | Pop and discard top |
| `:` | Duplicate top |
| `~` | Invert: negate number or reverse string |
| `$` | Length of string or number of digits |
| `!` | Explode: split value into characters/digits |
| `_` | Assemble: concatenate all stack items into one string |
| `∑` | Sum of all numbers on the stack |
| `∏` | Product of all numbers on the stack |
| `∞` | Push infinity (`inf`) |

### Arithmetic
| Symbol | Description |
|--------|-------------|
| `+` | Addition |
| `-` | Subtraction |
| `*` | Multiplication |
| `**` | Exponentiation |
| `;` | Division |
| `%` | Modulo |
| `&` | Concatenation (smart join). If both are floats — join as decimals (e.g., 3.5 & 6.7 → 3.567). If numbers — concatenate as strings then convert to number. If strings — concatenate. If string + number — concatenate to string. |
| `|` | Maximum: finds the maximum number in the entire stack, clears the stack, and pushes the result. If no numbers are found, pushes 0. |
| `√` | Root: `a b √` = a-th root of b; with one value = square root |

### Conditionals
| Symbol | Description |
|--------|-------------|
| `{` `}` | Conditional block. If condition is true, execute block; else skip to next line. |

#### Supported conditions
| Syntax | Meaning |
|--------|---------|
| `{=10}` | Equal to 10 |
| `{==}` | Compare top two stack values |
| `{=}` | Loose equality |
| `{<5}` | Less than 5 |
| `{>3}` | Greater than 3 |
| `{<}` | Less than (top two values) |
| `{>}` | Greater than (top two values) |
| `{;2}` | Divisible by 2 |
| `{№"abc"}` | Substring check |
| `{}` | Not zero / non-empty |

### Indexing and slices
| Syntax | Description |
|--------|-------------|
| `(n)` | Push element at index `n` to top |
| `(-1)` | Last element |
| `(start:end)` | Slice |
| `(start:end:step)` | Slice with step |
| `[n]` | Index with order preservation |

### I/O
| Symbol | Description |
|--------|-------------|
| `,` | Read string from stdin |
| `?` | Print top of stack |
| `₽` | Convert and push: number ↔ character ↔ string |

### Type conversion
| Command | Description |
|---------|-------------|
| `@!` | Convert to integer |
| `@$` | Convert to string |
| `@?` | Convert to float |
| `@~` | Auto-convert (legacy) |
| `@^` | Convert top of stack to UPPERCASE (string) |
| `@v` | Convert top of stack to lowercase (string) |

### Miscellaneous
| Symbol | Description |
|--------|-------------|
| `#` | Comment (to end of line) |
| `@@` | Halt execution |
| `` ` `` | Random: `min max `` |
| `(a|b)` | Random in range `[a..b]` |

## Example programs

### Hello, World!
```
>"Hello, World!"?@@
```

### Factorial
```
v v        <
>6>{>1}>:1-^
   v
   >∏?@@
```

### FizzBuzz
```
>0>{<100}>1+{;3}>  v
   v        v
   >@@      >{;5}> >{;3}>"Fizz"?v
             v      v
             >:?  v >           >{;5}>"Buzz"?v
                                 v
                                 >           v
                  >                          >"\n"?v
  ^                                                <
```

### A+B problem
```
>,,+?@@
```

### Calculator
```
>"1st num: "?,"2nd num: "?,"Operation: "?,{="+"}>'+?@@
                                          v
                                          >{="-"}>'-?@@
                                           v
                                           >{="*"}>'*?@@
                                            v
                                            >{="/"}>';?@@
                                             v
                                             >{="^"}>'**?@@
                                              v
                                              >"Idk"?@@
```

## Computational class

ArrowPrint is believed to be [[Turing complete]], as it supports conditional loops, arbitrary stack manipulation, and dynamic control flow.

## Implementation

The reference implementation is written in Python 3 and is available on GitHub.

### Requirements
- Python 3.6 or higher

### Windows Installation
1. Download the installer and interpreter files from the GitHub repository:
   ```
   https://github.com/ViktorChampion/arrowprint
   ```
   or download the ZIP archive using the **Code** → **Download ZIP** button.

2. Run `install_arrowprint.bat` as administrator:
   - Right-click the file
   - Select **"Run as administrator"**

3. After installation, the interpreter is placed in `C:\ArrowPrint` and added to your system PATH.

4. **Restart your terminal** (command prompt or PowerShell).

5. Now you can run any ArrowPrint program:
   ```
   arrowprint program.arp
   ```

### Linux / macOS
Not yet officially supported, but can be run manually via Python:
```
python3 interpreter.py program.arp
```

## Trivia

- The name "ArrowPrint" comes from the arrow-based navigation and the `?` print command.
- The language contains a hidden tribute to Befunge's `#` and `_` commands.
- There is no `print()` function — only `?` and `₽`.
- The random generator (`` ` `` and `(a|b)`) was originally a joke, but became a core feature.
- Early versions of the language had a hard limit of 100,000 commands per program, encouraging concise and creative coding.

## External links

- [GitHub Repository](https://github.com/ViktorChampion/arrowprint)
- [GitHub repository for online interpreter](https://github.com/ViktorChampion/ArrowPrintInterpreter/)
- [Online interpreter](https://viktorchampion.github.io/ArrowPrintInterpreter/)
- [Language Documentation](https://github.com/ViktorChampion/arrowprint/blob/master/README.md)

## See also

- [[Befunge]]
- [[Brainfuck]]
- [[Esolang]]
- [[List of esoteric programming languages]]

---

**ArrowPrint** — where every arrow leads somewhere. 🚀
