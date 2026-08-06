# ArrowPrint

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Python](https://img.shields.io/badge/python-3.6+-green)
![License](https://img.shields.io/badge/license-MIT-green)
![Platform](https://img.shields.io/badge/platform-Windows-lightgrey)

**ArrowPrint** is an esoteric programming language created in 2026. It is inspired by two-dimensional languages such as [[Befunge]], combining stack-based logic, non-linear execution, and minimalist syntax. The language is often described as "Befunge for those who want to write code with style and soul."

According to the author, every ArrowPrint program is not just an algorithm — it's a **journey**. Literally: the code is a two-dimensional grid through which an instruction pointer moves, executing commands along the way. This creates a "quest-like" feel, where the programmer both designs the map and navigates through it.

== Philosophy ==

ArrowPrint was not built for practical tasks. It was built for **the joy of coding**. It doesn't try to replace Python, C++, or any mainstream language. Its goal is to give the programmer a sense of exploration — where every new program is a maze, and every mistake is not a bug, but an "unexpected route."

''"In ArrowPrint, code is not read top-to-bottom. It is read in whatever direction you choose to go."'' — ViktorChampion

== History ==

The language was originally written with a hard limit of 100,000 commands per program. This limitation was a deliberate design choice to encourage concise and creative coding, forcing programmers to think in terms of efficiency and elegance rather than brute force. While this limit has since been removed in later versions, the philosophy behind it remains: ArrowPrint is about expression, not endless loops.

== Syntax and structure ==

An ArrowPrint program is a rectangular grid of symbols. Execution begins at the first arrow (<code>></code>, <code><</code>, <code>^</code>, or <code>v</code>) found in the grid. The instruction pointer moves cell by cell, and each cell contains either a command, data, or a comment.

A key feature of the language is the **absence of explicit blocks**. Branching and loops are implemented through direction changes and conditional jumps (<code>{ }</code>).

== Commands ==

=== Navigation ===
{| class="wikitable"
|-
! Symbol !! Description
|-
| <code>></code> || Move right
|-
| <code><</code> || Move left
|-
| <code>^</code> || Move up
|-
| <code>v</code> || Move down
|-
| <code>/</code> || Mirror (reflect direction)
|-
| <code>\</code> || Mirror (reflect direction)
|-
| <code>(x,y)</code> || Teleport to absolute or relative coordinates (e.g., <code>(+2,-3)</code>)
|}

=== Stack Operations ===
{| class="wikitable"
|-
! Symbol !! Description
|-
| <code>?</code> || Print top of stack (no newline)
|-
| <code>'</code> || Pop and discard top
|-
| <code>:</code> || Duplicate top
|-
| <code>~</code> || Invert: negate number or reverse string
|-
| <code>$</code> || Length of string or number of digits
|-
| <code>!</code> || Explode: split value into characters/digits
|-
| <code>_</code> || Assemble: concatenate all stack items into one string
|-
| <code>∑</code> || Sum of all numbers on the stack
|-
| <code>∏</code> || Product of all numbers on the stack
|-
| <code>∞</code> || Push infinity (<code>inf</code>)
|}

=== Arithmetic ===
{| class="wikitable"
|-
! Symbol !! Description
|-
| <code>+</code> || Addition
|-
| <code>-</code> || Subtraction
|-
| <code>*</code> || Multiplication
|-
| <code>**</code> || Exponentiation
|-
| <code>;</code> || Division
|-
| <code>%</code> || Modulo
|-
| <code>&</code> || Concatenation (smart join). If both are floats — join as decimals (e.g., 3.5 & 6.7 → 3.567). If numbers — concatenate as strings then convert to number. If strings — concatenate. If string + number — concatenate to string.
|-
| <code>&#124;</code> || Maximum: finds the maximum number in the entire stack, clears the stack, and pushes the result. If no numbers are found, pushes 0.
|-
| <code>√</code> || Root: <code>a b √</code> = a-th root of b; with one value = square root
|}

=== Conditionals ===
{| class="wikitable"
|-
! Symbol !! Description
|-
| <code>{</code> <code>}</code> || Conditional block. If condition is true, execute block; else skip to next line.
|}

==== Supported conditions ====
{| class="wikitable"
|-
! Syntax !! Meaning
|-
| <code>{=10}</code> || Equal to 10
|-
| <code>{==}</code> || Compare top two stack values
|-
| <code>{=}</code> || Loose equality
|-
| <code>{<5}</code> || Less than 5
|-
| <code>{>3}</code> || Greater than 3
|-
| <code>{<}</code> || Less than (top two values)
|-
| <code>{>}</code> || Greater than (top two values)
|-
| <code>{;2}</code> || Divisible by 2
|-
| <code>{№"abc"}</code> || Substring check
|-
| <code>{}</code> || Not zero / non-empty
|}

=== Indexing and slices ===
{| class="wikitable"
|-
! Syntax !! Description
|-
| <code>(n)</code> || Push element at index <code>n</code> to top
|-
| <code>(-1)</code> || Last element
|-
| <code>(start:end)</code> || Slice
|-
| <code>(start:end:step)</code> || Slice with step
|-
| <code>[n]</code> || Index with order preservation
|}

=== I/O ===
{| class="wikitable"
|-
! Symbol !! Description
|-
| <code>,</code> || Read string from stdin
|-
| <code>?</code> || Print top of stack
|-
| <code>₽</code> || Convert and push: number ↔ character ↔ string
|}

=== Type conversion ===
{| class="wikitable"
|-
! Command !! Description
|-
| <code>@!</code> || Convert to integer
|-
| <code>@$</code> || Convert to string
|-
| <code>@?</code> || Convert to float
|-
| <code>@~</code> || Auto-convert (legacy)
|-
| <code>@^</code> || Convert top of stack to UPPERCASE (string)
|-
| <code>@v</code> || Convert top of stack to lowercase (string)
|}

=== Miscellaneous ===
{| class="wikitable"
|-
! Symbol !! Description
|-
| <code>#</code> || Comment (to end of line)
|-
| <code>@@</code> || Halt execution
|-
| <code>`</code> || Random: <code>min max `</code>
|-
| <code>(a&#124;b)</code> || Random in range <code>[a..b]</code>
|}

== Example programs ==

=== [[Hello, World!]] ===
<pre>>"Hello, World!"?@@</pre>

=== [[Factorial]] ===
<pre>
v v        <
>6>{>1}>:1-^
   v
   >∏?@@
</pre>

=== [[FizzBuzz]] ===
<pre>
>0>{<100}>1+{;3}>  v
   v        v
   >@@      >{;5}> >{;3}>"Fizz"?v
             v      v
             >:?  v >           >{;5}>"Buzz"?v
                                 v
                                 >           v
                  >                          >"\n"?v
  ^                                                <
</pre>

=== [[A+B problem]] ===
<pre>
>,,+?@@
</pre>

=== [[Calculator (program form)|Calculator]] ===
<pre>
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
</pre>

== Computational class ==

ArrowPrint is believed to be [[Turing complete]], as it supports conditional loops, arbitrary stack manipulation, and dynamic control flow.

== Implementation ==

The reference implementation is written in Python 3 and is available on GitHub.

=== Requirements ===
- Python 3.6 or higher

=== Windows Installation ===
1. Download the installer and interpreter files from the GitHub repository:
   <pre>https://github.com/ViktorChampion/arrowprint</pre>
   or download the ZIP archive using the '''Code''' → '''Download ZIP''' button.

2. Run <code>install_arrowprint.bat</code> as administrator:
   - Right-click the file
   - Select '''"Run as administrator"'''

3. After installation, the interpreter is placed in <code>C:\ArrowPrint</code> and added to your system PATH.

4. '''Restart your terminal''' (command prompt or PowerShell).

5. Now you can run any ArrowPrint program:
   <pre>arrowprint program.arp</pre>

=== Linux / macOS ===
Not yet officially supported, but can be run manually via Python:
<pre>python3 interpreter.py program.arp</pre>

== Trivia ==

* The name "ArrowPrint" comes from the arrow-based navigation and the <code>?</code> print command.
* The language contains a hidden tribute to Befunge's <code>#</code> and <code>_</code> commands.
* There is no <code>print()</code> function — only <code>?</code> and <code>₽</code>.
* The random generator (<code>`</code> and <code>(a|b)</code>) was originally a joke, but became a core feature.
* Early versions of the language had a hard limit of 100,000 commands per program, encouraging concise and creative coding.

== External links ==

* [https://github.com/ViktorChampion/arrowprint GitHub Repository]
* [https://github.com/ViktorChampion/ArrowPrintInterpreter/ GitHub repository for online interpreter]
* [https://viktorchampion.github.io/ArrowPrintInterpreter/ online interpreter]
* [https://github.com/ViktorChampion/arrowprint/blob/master/README.md Language Documentation]

== See also ==

* [[Befunge]]
* [[Brainfuck]]
* [[Esolang]]
* [[List of esoteric programming languages]]

----

'''ArrowPrint''' — where every arrow leads somewhere. 🚀

[[Category:Languages]][[Category:2026]][[Category:Generated by AI]][[Category:Two-dimensional]]

