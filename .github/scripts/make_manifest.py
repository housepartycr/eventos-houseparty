"""Genera galeria/galeria.json con las fotos de la carpeta galeria/ (las más nuevas primero)."""
import json, subprocess
from pathlib import Path

EXT = {".jpg", ".jpeg", ".png", ".webp", ".gif", ".avif"}
carpeta = Path("galeria")

def fecha_subida(p):
    r = subprocess.run(["git", "log", "--diff-filter=A", "--format=%ct", "--", str(p)],
                       capture_output=True, text=True)
    lineas = r.stdout.split()
    return int(lineas[-1]) if lineas else 0

fotos = [p for p in carpeta.iterdir() if p.is_file() and p.suffix.lower() in EXT]
fotos.sort(key=lambda p: (-fecha_subida(p), p.name.lower()))

salida = {"fotos": [p.name for p in fotos]}
(carpeta / "galeria.json").write_text(json.dumps(salida, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"{len(fotos)} fotos en la galería")
