# Bootcamp
#Day 0 

# 🎉 Shravya Hello

PyPI version | Python Versions | License: MIT**

Say hello with style – A simple yet elegant greeting package for your Python projects.


## ✨ Features

* 🖨️ Beautiful, colorful terminal output using **Rich**
* 🎯 Simple command-line interface with **Typer**
* 🔧 Customizable greetings with name options
* 🚀 Easy to use both as a **library** and **command-line tool**

---

## 🚀 Installation

### From PyPI (Stable Release):

```bash
pip install shravya-hello
```

### From Test PyPI (Pre-Release):

```bash
pip install -i https://test.pypi.org/simple/ shravya-hello
```

---

## 🧩 Usage

### As a Command Line Tool

```bash
# Default greeting
shravya-hello greet

# Greeting with a name
shravya-hello greet --name "Shravya"
```

### As a Python Library

```python
from shravya_hello.hello import say_hello

# Default greeting
say_hello()

# Greeting with a name
say_hello("Shravya")
```

---

## 🎬 Demo

Watch the package in action:

`asciicast` *(add your cast URL or GIF here if available)*

---

## 📘 API Reference

```python
say_hello(name: Optional[str] = None) -> None
```

**Displays a stylized greeting message.**

**Parameters:**

* `name` *(optional)*: The name to greet. Defaults to `"World"` if not provided.

**Example:**

```python
from shravya_hello.hello import say_hello

# Will print: Hello, World!
say_hello()

# Will print: Hello, Shravya!
say_hello("Shravya")
```

---

## 🔧 Development

### To set up the development environment:

**Clone the repository:**

```bash
git clone https://github.com/shravya123/shravya-hello.git
cd shravya-hello
```

**Create and activate a virtual environment:**

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows, use: .venv\Scripts\activate
```

**Install dependencies:**

```bash
pip install -e ".[dev]"
```

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create a feature branch

   ```bash
   git checkout -b feature/amazing-feature
   ```
3. Commit your changes

   ```bash
   git commit -m 'Add some amazing feature'
   ```
4. Push to the branch

   ```bash
   git push origin feature/amazing-feature
   ```
5. Open a Pull Request

---

## 📝 License

This project is licensed under the **MIT License** – see the `LICENSE` file for details.

