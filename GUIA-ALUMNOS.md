# Guía paso a paso: cómo subir tu TP (primera vez con Git)

Esta guía es para quienes nunca usaron Git ni GitHub. Vas a necesitar una cuenta de GitHub (gratis) y tener Git instalado en tu computadora.

Hay dos caminos: **GitHub Desktop** (con interfaz gráfica, más fácil para empezar) o **terminal** (línea de comandos). Elegí el que te resulte más cómodo, el resultado es el mismo.

Las entregas son **individuales**: hacés tu propio fork, tu propia rama y tu propia carpeta para cada TP. No hay grupos. Tu carpeta se nombra `APELLIDO_NOMBRE_DNI` (ej: `PEREZ_JUAN_30111222`); hay un ejemplo con ese formato en `TRABAJOS PRACTICOS/TP1/`.

---

## 0. Requisitos previos

1. **Creá una cuenta en GitHub** (si no tenés): https://github.com/join
2. **Instalá Git**: https://git-scm.com/downloads (dejá todas las opciones por defecto durante la instalación)
3. *(Opcional, recomendado para principiantes)* **Instalá GitHub Desktop**: https://desktop.github.com/

---

## Camino A: con GitHub Desktop (recomendado si es tu primera vez)

### 1. Hacé fork del repositorio

1. Andá a https://github.com/coedomaximiliano/COL-PII-2026-2
2. Hacé click en el botón **Fork** (arriba a la derecha).
3. Confirmá con **Create fork**. Ahora tenés tu propia copia en `https://github.com/TU-USUARIO/COL-PII-2026-2`.

### 2. Cloná tu fork con GitHub Desktop

1. Abrí GitHub Desktop e iniciá sesión con tu cuenta de GitHub (`File > Options > Sign in`).
2. `File > Clone repository`.
3. Elegí tu fork (`TU-USUARIO/COL-PII-2026-2`) y una carpeta local donde guardarlo. Click en **Clone**.

### 3. Creá tu carpeta y agregá tus archivos

1. Abrí la carpeta local del repo (en GitHub Desktop: `Repository > Show in Explorer`).
2. Entrá a `TRABAJOS PRACTICOS/TPN/` (reemplazá `N` por el número del trabajo práctico que estás entregando, o `TP INTEGRADOR`).
3. Creá una carpeta con el formato `APELLIDO_NOMBRE_DNI`, por ejemplo `TRABAJOS PRACTICOS/TP1/PEREZ_JUAN_30111222/`.
4. Copiá ahí los archivos del TP.

### 4. Creá una rama

1. En GitHub Desktop, arriba dice "Current branch". Click ahí y luego **New branch**.
2. Nombrala `tpN-apellido_nombre_dni` (ej: `tp1-perez_juan_30111222`).
3. Click en **Create branch**.

### 5. Commit y push

1. GitHub Desktop va a mostrar los archivos nuevos que agregaste (columna izquierda).
2. Abajo a la izquierda, escribí un mensaje de commit, ej: `TP1: Perez Juan`.
3. Click en **Commit to tp1-perez_juan_30111222**.
4. Arriba a la derecha, click en **Push origin** (esto sube los cambios a tu fork en GitHub).

### 6. Abrí el Pull Request (una sola vez por entrega)

1. En GitHub Desktop aparece un botón **Create Pull Request** después del push (o entrá a tu fork en github.com).
2. Se abre GitHub en el navegador. Verificá que:
   - **base repository**: `coedomaximiliano/COL-PII-2026-2`, rama `main`
   - **head repository**: `TU-USUARIO/COL-PII-2026-2`, rama `tpN-apellido_nombre_dni`
3. Título del PR: `TP1: Perez Juan` (número de TP + tu nombre).
4. Click en **Create pull request**.

¡Listo! Ya está entregado. El docente va a revisar y puede pedir cambios o aprobarlo.

---

## Camino B: con terminal (Git Bash / PowerShell)

### 1. Configurá Git (solo la primera vez que usás Git en tu PC)

```
git config --global user.name "Tu Nombre"
git config --global user.email "tu-email@ejemplo.com"
```

### 2. Hacé fork del repositorio

1. Andá a https://github.com/coedomaximiliano/COL-PII-2026-2
2. Click en **Fork** (arriba a la derecha) y confirmá con **Create fork**.

### 3. Cloná tu fork

```
git clone https://github.com/TU-USUARIO/COL-PII-2026-2.git
cd COL-PII-2026-2
```

(Reemplazá `TU-USUARIO` por tu usuario de GitHub)

### 4. Creá una rama para la entrega

```
git checkout -b tp1-perez_juan_30111222
```

(Reemplazá `tp1-perez_juan_30111222` por `tpN-apellido_nombre_dni` según corresponda)

### 5. Creá tu carpeta y agregá tus archivos

Creá la carpeta `TRABAJOS PRACTICOS/TP1/PEREZ_JUAN_30111222/` (con el número de TP y tu apellido, nombre y DNI) y copiá ahí los archivos.

### 6. Agregá, commiteá y pusheá los cambios

```
git add "TRABAJOS PRACTICOS/TP1/PEREZ_JUAN_30111222"
git commit -m "TP1: Perez Juan"
git push origin tp1-perez_juan_30111222
```

La primera vez que hagas `push` es posible que se abra una ventana del navegador pidiéndote iniciar sesión en GitHub. Iniciá sesión y el push va a continuar solo.

### 7. Abrí el Pull Request (una sola vez por entrega)

1. Terminada la push, la terminal te va a mostrar un link para crear el Pull Request (o entrá a tu fork en github.com, va a aparecer un botón **Compare & pull request**).
2. Verificá que la base sea `coedomaximiliano/COL-PII-2026-2` rama `main`.
3. Título del PR: `TP1: Perez Juan`.
4. Click en **Create pull request**.

---

## Flujo del día a día mientras programás

Esto se repite cada vez que te sientas a programar, una vez que ya existe la rama `tpN-apellido_nombre_dni`:

1. **Pararte en la rama correcta**:
   ```
   git checkout tpN-apellido_nombre_dni
   ```
2. **Programar** dentro de `TRABAJOS PRACTICOS/TPN/APELLIDO_NOMBRE_DNI/`.
3. **Guardar el avance** con commits chicos y seguidos (no uno solo gigante al final):
   ```
   git add "TRABAJOS PRACTICOS/TPN/APELLIDO_NOMBRE_DNI"
   git commit -m "agrego validación de X"
   ```
4. **Subir el avance**:
   ```
   git push origin tpN-apellido_nombre_dni
   ```
   El primer push sugiere crear el Pull Request; los siguientes pushes a la misma rama lo actualizan solos, sin hacer nada más.

Repetí los pasos 1 a 4 cada sesión de trabajo.

*Si usás GitHub Desktop, es el mismo flujo con los botones equivalentes: **Fetch origin / Pull origin** antes de programar, y **Commit** + **Push origin** después de cada avance.*

---

## Si tenés que corregir algo después de entregar

No hace falta abrir un PR nuevo: alcanza con modificar los archivos en la carpeta local, y repetir el `commit` + `push` en la **misma rama**. El Pull Request se actualiza solo con los nuevos cambios.

```
git add "TRABAJOS PRACTICOS/TP1/PEREZ_JUAN_30111222"
git commit -m "TP1: correcciones"
git push origin tp1-perez_juan_30111222
```

---

## Problemas comunes

- **"Nombre de carpeta ya existe" o error al abrir PR**: asegurate de no haber tocado archivos fuera de tu propia carpeta.
- **No me aparece el botón "Create pull request"**: entrá directamente a `https://github.com/TU-USUARIO/COL-PII-2026-2/pull/new/tpN-apellido_nombre_dni`.
- **Me pide usuario y contraseña y falla**: GitHub ya no acepta contraseña por línea de comandos. Dejá que se abra la ventana del navegador para iniciar sesión (Git Credential Manager), o usá GitHub Desktop.

Ante cualquier duda, consultá al docente antes de la fecha límite de entrega.
