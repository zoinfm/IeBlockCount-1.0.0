# 🧮 IE Block Count - Contador de Bloques por Circuito Eléctrico

[![Python 3.14](https://img.shields.io/badge/python-3.14-blue.svg)](https://www.python.org/downloads/)
[![AutoCAD](https://img.shields.io/badge/AutoCAD-2022%2B-red.svg)](https://www.autodesk.com/autocad)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Herramienta de automatización para AutoCAD que **cuenta bloques (luminarias, equipos) agrupándolos por el valor de su atributo `$circuito`** y calcula la **distancia Manhattan promedio** desde cada grupo hasta un bloque de tablero seleccionado por el usuario.

Ideal para ingenieros eléctricos, diseñadores de iluminación y profesionales que necesitan analizar planos de forma rápida y precisa, evitando errores manuales.

---

## 🚀 Características

- 🔌 Conexión directa a AutoCAD mediante `pyautocad`.
- 📌 Selección interactiva del bloque que representa el **tablero**.
- 🧩 Procesa solo bloques en **capas visibles y desbloqueadas** (mayor rendimiento).
- 🏷️ Lee el atributo `$circuito` de cada bloque (insensible a mayúsculas).
- 📊 Genera dos tablas:
  - **Conteo por tipo de bloque y circuito**: `(valor $circuito, nombre bloque, cantidad)`.
  - **Distancia Manhattan promedio por circuito**: desde los bloques hasta el tablero.
- 📋 Copia automática al portapapeles en formato tabulado, listo para pegar en **Excel**.
- 🧩 Código **modular** (clases separadas por responsabilidad), fácil de mantener y extender.

---

## 🛠️ Tecnologías utilizadas

- **Python 3.14** (compatible con versiones 3.8+)
- `pyautocad` – para interactuar con AutoCAD COM API.
- **Git** – control de versiones.

---

## 📦 Instalación

1. **Clona el repositorio**:
   ```bash
   git clone https://github.com/zoinfm/IeBlockCount-1.0.0.git
   cd IeBlockCount-1.0.0
