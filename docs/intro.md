# Introduction

[![PythonCodeAudit Badge](https://img.shields.io/badge/Python%20Code%20Audit-Security%20Verified-FF0000?style=flat-square)](https://github.com/nocomplexity/codeaudit)
[![PyPI version](https://img.shields.io/pypi/v/linkaudit.svg)](https://pypi.org/project/linkaudit/)
[![Python Versions](https://img.shields.io/pypi/pyversions/linkaudit.svg)](https://pypi.org/project/linkaudit/)

**Linkaudit** is a fast, simple CLI tool that checks for broken links in `markdown`, `MyST`, and `rst` documentation. Built specifically for [JupyterBook](https://jupyterbook.org/) and Sphinx projects.

```bash
pip install linkaudit
linkaudit check docs/
```

---

## ✨ Why Linkaudit?

Maintaining documentation with hundreds of links is tedious. Dead links frustrate readers and damage credibility. While Sphinx includes a `linkcheck` builder, it can be slow, hard to customize, and its output is noisy.

Linkaudit solves these problems by being:

- **Fast** — Uses Python `asyncio` for concurrent I/O
- **Clear** — Shows only broken links with file paths and line numbers
- **Simple** — Easy to understand, modify, and contribute to
- **Focused** — Works with JupyterBook v1, v2, and plain Sphinx

---

## 📖 Background

> The Internet is flooded with broken links. Keeping documentation up-to-date is hard work.

Great documentation is **maintained** documentation. But checking every URL manually isn't feasible. And while Sphinx has a [linkcheck builder](https://www.sphinx-doc.org/en/master/usage/builders/index.html#module-sphinx.builders.linkcheck), it comes with limitations:

- Complex and intimidating codebase
- Difficult to customize or improve
- Output includes all links, not just broken ones
- Single-threaded — slower for large documentation sets

Linkaudit was created to fill this gap — a **simpler, faster, more focused** alternative.

> **Note:** The Sphinx linkcheck builder is great software that works well. Linkaudit isn't a replacement for everyone — it's an alternative for those who want simplicity and speed.

---

## 🎯 Who Is This For?

Linkaudit is ideal for:

- **JupyterBook users** — Supports both v1 (Sphinx-based) and v2
- **Sphinx documentation maintainers** — Works with `.rst` and `.md` files
- **Technical writers** — Need clear output with file paths and line numbers


```bash
# Run on your entire documentation directory
linkaudit check docs/

# Or check specific files
linkaudit check docs/guide.md docs/tutorial.rst
```

---

## ⚡ Quick Comparison

| Feature | Sphinx linkcheck | Linkaudit |
|---------|----------------:|----------:|
| Shows only broken links | ❌ No | ✅ Yes |
| File + line number for each broken link | ❌ No | ✅ Yes |
| Async I/O for speed | ❌ No | ✅ Yes |
| Simple, hackable codebase | ❌ Complex | ✅ Simple |
| Works with JupyterBook v1 & v2 | ✅ Yes | ✅ Yes |
| Works with plain Sphinx | ✅ Yes | ✅ Yes |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- A documentation project using JupyterBook or Sphinx

### Installation

```bash
pip install -U linkaudit
```

### Basic Usage

```bash
# Check all markdown/rst files in a directory
linkaudit check ./my-documentation/
```

### Using with Sphinx's built-in linkcheck

Sphinx's native approach still works great:

```bash
jb build --builder linkcheck PATH_SOURCE
```

Use Linkaudit when you want faster checks, cleaner output, or easier customization.

---

## 💡 Motivation

I created Linkaudit because:

1. **Sphinx's linkcheck code is complex** — The [implementation](https://www.sphinx-doc.org/en/master/_modules/sphinx/builders/linkcheck.html#CheckExternalLinksBuilder) is intimidating to modify or improve
2. **Pull requests take too long** — Getting changes into Sphinx's core is time-consuming with uncertain outcomes
3. **Output is cluttered** — I only want to see broken links, not a log of every successful check
4. **Manual fixes need context** — Showing file paths and line numbers makes fixing links frictionless
5. **Speed matters** — With hundreds or thousands of links, concurrent I/O (asyncio) makes a huge difference

> As I like to say: sometimes you just need to [make IT better](https://nocomplexity.com/business/).


## 📚 Table of Contents

```{tableofcontents}
```


