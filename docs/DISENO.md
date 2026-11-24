# Sistema de Diseño y Landing Page — Pecados Sabor del Cielo

Este documento registra la identidad visual, la paleta de colores oficial, la tipografía, las secciones y los recursos gráficos implementados en la landing page.

---

## 1. Paleta de colores oficial

Definida en variables CSS dentro de `static/css/styles.css`:

| Variable CSS | Código HEX | Nombre | Uso principal |
| :--- | :--- | :--- | :--- |
| `--color-espresso` | `#291C0E` | Espresso Oscuro | Títulos principales, botones primarios, panel izquierdo de Historia, footer y textos de alto contraste |
| `--color-cocoa` | `#6E473B` | Cacao Tostado | Palabra destacada del Hero (`pecado.`), acentos editoriales, etiquetas eyebrow, iconos y degradados cálidos |
| `--color-caramel` | `#A78D78` | Caramelo Suave | Subtítulos sobre fondos oscuros, bordes de acento y detalles tipográficos secundarios |
| `--color-oat` | `#BEB5A9` | Avena Cálida | Divisores finos, bordes de botones secundarios y texto sutil sobre fondo espresso |
| `--color-cream` | `#E1D4C2` | Crema Pergamino | Panel tipográfico de Historia, textos claros sobre oscuro, hover de botones y acentos cálidos |
| `--color-canvas` | `#F6F0E8` | Marfil Cálido (derivado) | Fondo principal de la página y máscara luminosa del Hero |
| `--color-surface` | `#FBF8F4` | Superficie Clara (derivado) | Tarjetas internas y banda de pilares |

---

## 2. Tipografía

- **Titulares y marca (`--font-serif`)**: `Playfair Display` (fallback: `Georgia`, serif) — aporta carácter editorial y artesanal al wordmark, título principal del hero, encabezados de sección y nombres de productos.
- **Interfaz y cuerpo (`--font-sans`)**: `Plus Jakarta Sans` (fallback: `system-ui`, sans-serif) — garantiza legibilidad en navegación, botones tipo píldora, precios, métricas y textos descriptivos.

---

## 3. Secciones de la Landing Page (`core/templates/core/home.html`)

1. **Barra de navegación (`templates/partials/_navbar.html`)**:
   - Transparente sobre el Hero al cargar y transición suave a fondo crema translúcido (`is-scrolled`) al desplazarse.
   - Emblema circular oficial (`static/img/logo-pecados.png`) a la izquierda junto al wordmark `PECADOS / SABOR DEL CIELO`, navegación principal, ícono de bolsa con contador interactivo, botón CTA `Hacer Pedido` y menú colapsable para móvil.
2. **Hero editorial**:
   - Fotografía a pantalla completa (`static/img/hero-cafe.jpg`) con degradado cálido de izquierda a derecha para máxima legibilidad del título.
   - Botón principal (`Explorar el Menú`), enlace visual (`Conoce Nuestra Historia`) y franja de 3 métricas (`10K+`, `4.9 ★`, `100%`).
3. **Favoritos de temporada (`#menu-favoritos`)**:
   - Encabezado editorial de 3 columnas con acceso a `/productos/`.
   - Grilla responsiva de 4 tarjetas verticales con fotografía a sangre, degradado espresso inferior, categoría, nombre, notas de sabor, precio y botón circular `+` con notificación toast y contador.
4. **Nuestra Historia (`#nuestra-historia`)**:
   - Composición en 3 paneles: bloque oscuro `#291C0E` con narrativa y CTA, fotografía central (`static/img/story-table.jpg`) y panel crema `#E1D4C2` con manifiesto tipográfico.
5. **Pilares de marca**:
   - Franja de 4 atributos (*Origen Sostenible*, *Horneo Diario*, *Espacios Acogedores*, *Bebidas de Autor*) con iconos SVG en línea y divisores sutiles.
6. **Footer oscuro (`templates/partials/_footer.html`)**:
   - Fondo `#291C0E`, wordmark, formulario de boletín con validación en cliente, enlaces sociales circulares y barra legal inferior.

---

## 4. Recursos fotográficos (`static/img/`)

| Archivo | Uso |
| :--- | :--- |
| `static/img/logo-pecados.png` | Logo oficial circular en la barra de navegación superior izquierda y favicon |
| `static/img/hero-cafe.jpg` | Fotografía principal del Hero (interior de cafetería artesanal en luz cálida) |
| `static/img/menu-latte.jpg` | Tarjeta 1: Latte Clásico |
| `static/img/menu-iced-vanilla.jpg` | Tarjeta 2: Vainilla Helada |
| `static/img/menu-chocolate-cake.jpg` | Tarjeta 3: Pecado de Chocolate |
| `static/img/menu-croissant.jpg` | Tarjeta 4: Croissant de Almendras |
| `static/img/story-table.jpg` | Panel fotográfico central de Nuestra Historia |
