# 📄 PDF Injector 💉

A minimal tool for injecting JavaScript content into PDF files  
using `pikepdf` and `reportlab`.

Simple. Fast. Effective.

---

### ✉️ Note

Certain vendors have already been informed.  
**Please do not report or contact them** — there's no action required on your part.

---

### ⚙️ Requirements

pikepdf
reportlab


Install dependencies with:

```bash
pip install -r requirements.txt
```

### 🎬 Usage

```python
python js_injector.py -f (template file / normal file).pdf -o (output file / evil one).pdf -c (js code / code that gets injected).js
```

```python
python js_injector.py -f file.pdf -o output.pdf -c evil.js
