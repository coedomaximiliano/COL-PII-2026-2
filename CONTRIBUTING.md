# Cómo contribuir

Cada alumno sube su código mediante fork + pull request. Las entregas son **individuales**. Nadie tiene permiso de escritura directa sobre este repositorio.

## Pasos

1. **Fork**: hacé fork de este repositorio a tu cuenta de GitHub (botón "Fork" arriba a la derecha).

2. **Cloná tu fork**:
   ```
   git clone https://github.com/TU-USUARIO/COL-PII-2026-2.git
   cd COL-PII-2026-2
   ```

3. **Creá tu carpeta** dentro del trabajo práctico correspondiente:
   ```
   TRABAJOS PRACTICOS/TPN/TU-USUARIO/
   ```
   Reemplazá `TPN` por `TP1`, `TP2`, `TP3` o `TP INTEGRADOR`, y `TU-USUARIO` por tu usuario de GitHub.

4. **Creá una rama** para la entrega:
   ```
   git checkout -b tpN-tu-usuario
   ```

5. **Commiteá y pusheá** a tu fork:
   ```
   git add "TRABAJOS PRACTICOS/TPN/TU-USUARIO"
   git commit -m "TPN: tu-usuario"
   git push origin tpN-tu-usuario
   ```

6. **Abrí un Pull Request** desde tu fork hacia `coedomaximiliano/COL-PII-2026-2` (rama `main`).

## Reglas

- Subí código **únicamente** dentro de tu propia carpeta. No modifiques archivos de otros alumnos.
- **Un solo PR por entrega**: correcciones posteriores van como nuevos commits en la misma rama, no un PR nuevo.
- El título del PR debe indicar el TP y tu usuario, ej: `TP1: juanperez`.
