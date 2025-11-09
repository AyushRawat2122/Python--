# 🐍 Python Execution Flow

---

## 🔹 Step 1: The Source Code (`.py` file)

You write human-readable code, e.g.:

```python
print("Hello, world!")
```

This is **plain text**, not something the computer directly understands.

---

## 🔹 Step 2: Python Interpreter Reads It

Python has an **interpreter**, not a compiler (like C++).
But interestingly… it **does compile internally** before execution.

---

## 🔹 Step 3: Compilation → Bytecode

Before running, Python **compiles** your `.py` file into **bytecode** — a lower-level representation (not machine code yet).
This is a `.pyc` file (you’ll find them inside a `__pycache__` folder).

**Example:**

```
myfile.py  ──>  myfile.cpython-311.pyc
```

This bytecode is **platform-independent** — it can run anywhere Python runs.

---

## 🔹 Step 4: Execution by Python Virtual Machine (PVM)

The **Python Virtual Machine (PVM)** takes that bytecode and executes it **line by line**.

Think of it like:

```
Code → Bytecode → PVM → Actual Execution
```

So, the pipeline looks like:

```
Source Code (.py)
   ↓
Compiler → Bytecode (.pyc)
   ↓
PVM (Interpreter)
   ↓
Machine executes
```

This is why Python is slower than compiled languages like C++ —
each line is interpreted on the fly by the **PVM**.

---

## 🔹 Step 5: Memory Management

Python automatically handles:

* **Memory allocation**
* **Garbage collection** (unused objects cleared automatically)

So you don’t have to `free()` or `delete` anything manually like in C++.
