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
   TRABAJOS PRACTICOS/TPN/APELLIDO_NOMBRE_DNI/
   ```
   Reemplazá `TPN` por `TP1`, `TP2`, `TP3` o `TP INTEGRADOR`, y `APELLIDO_NOMBRE_DNI` por tus datos (ej: `PEREZ_JUAN_30111222`). Hay una carpeta de ejemplo con ese formato en `TRABAJOS PRACTICOS/TP1/`.

4. **Creá una rama** para la entrega:
   ```
   git checkout -b tpN-apellido_nombre_dni
   ```

5. **Commiteá y pusheá** a tu fork:
   ```
   git add "TRABAJOS PRACTICOS/TPN/APELLIDO_NOMBRE_DNI"
   git commit -m "TPN: Apellido Nombre"
   git push origin tpN-apellido_nombre_dni
   ```

6. **Abrí un Pull Request** desde tu fork hacia `coedomaximiliano/COL-PII-2026-2` (rama `main`).

## Reglas

- Subí código **únicamente** dentro de tu propia carpeta. No modifiques archivos de otros alumnos.
- **Un solo PR por entrega**: correcciones posteriores van como nuevos commits en la misma rama, no un PR nuevo.
- El título del PR debe indicar el TP y tu nombre, ej: `TP1: Juan Perez`.
