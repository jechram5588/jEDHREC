# Jedhrec

Gestor de mazos de Magic: The Gathering (Commander). Muestra los mazos agrupados por tipo de carta, con imágenes, símbolos de maná y precios. Permite editarlos y exportarlos de vuelta a CSV.

- **Versión local:** [Jedhrec.html](Jedhrec.html). Se abre con doble clic en cualquier navegador. Empieza vacía: importa tus CSV o restaura un respaldo.
- **Versión en línea:** la carpeta `herramientas/site/` publicada como página (ver [Regenerar la página](#regenerar-la-página)).

## Contenido de la carpeta

| Archivo | Qué es |
|---|---|
| `Jedhrec.html` | La versión local de la página, sin mazos. |
| `herramientas/` | Código fuente de la página y scripts para regenerarla (ver [Regenerar la página](#regenerar-la-página)). |
| `privado/` | Tus archivos personales: CSV, la página con tus mazos incluidos, respaldos. **No se sube a git** (está en `.gitignore`). |

Tampoco se suben los CSV, los respaldos `jedhrec-respaldo*.json`, ni lo que se genera a partir de tus mazos (`herramientas/sf/meta.json`, `herramientas/sf/img/`, `herramientas/site/`).

## Formato de los CSV

Columnas separadas por **tabulador**, con esta cabecera:

```
QuantityX	Name	Edition	Foil	Price
1x	Sol Ring	Commander 2016		$2.00
1x	Thrasios, Triton Hero	Commander 2016	Foil	$25.99
```

- `QuantityX`: cantidad con una `x` al final (`1x`, `13x`).
- `Name`: nombre en inglés. Las cartas de dos caras van como `Cara A // Cara B`.
- `Foil`: `Foil` o vacío.
- `Price`: precio en dólares.

Al importar, el nombre del mazo es la parte del nombre de archivo antes del primer `_`. Por ejemplo, `MiMazo_2026_Oct_27_20-47.csv` crea el mazo **MiMazo**. Si ya existe un mazo con ese nombre, se reemplaza su lista de cartas.

Al importar se abre una ventana para confirmar el nombre y elegir el tipo: **Mazo de Commander** o **Lista de cartas** (ver [Tipos de mazo](#tipos-de-mazo)).

**Combinar varios CSV en un mazo:** elige o arrastra varios archivos a la vez. La ventana pregunta además si quieres **combinarlos en un solo mazo** (con el nombre que escribas) o crear **un mazo por archivo**. En los dos casos, los archivos con el mismo nombre de mazo se juntan, y una carta que aparece en varios archivos con la misma edición y foil queda en una sola fila con las copias sumadas.

## Tipos de mazo

| | Mazo de Commander | Lista de cartas |
|---|---|---|
| Contador | `N / 100` (verde con 100 exactas) | `N cartas` |
| Comandante | Se adivina por el nombre del mazo y se puede marcar en la ficha | No tiene |
| Miniatura | La del comandante | La de la **carta de portada**: en la ficha de cualquier carta, **Usar como portada**. Solo es la imagen; no cambia colores ni la exportación |
| Colores | Los del comandante (sin comandante: los de todas sus cartas) | Se eligen en **Editar mazo**: **Automático** (el color de todas sus cartas juntas, según su coste de maná: a diferencia de la identidad de Commander, una carta negra con flashback blanco cuenta solo como negra; debajo se ve qué cartas aportan cada color), **los de la carta de portada**, o **elegidos a mano** (ninguno = incoloro). Automático y portada se recalculan solos al cambiar las cartas |
| Menú **Mazos ▾** | Agrupado por número de colores | A lo ancho del menú, en su sección, **Listas de cartas** |

El tipo se elige al importar, al crear un mazo nuevo, o después con el lápiz (**Editar mazo**). Al pasar un mazo a lista se quita su comandante y pasa a ser la portada; al volver a Commander se adivina otra vez por el nombre.

## Uso

### Página principal
Al abrir la página se ven dos secciones: **Mis mazos** (los de Commander) y, debajo, **Listas de cartas** (solo si tienes alguna). Cada una muestra sus totales y una tarjeta por mazo con su comandante, colores, N / 100, valor, foils, coste medio, y cuántas cartas hay de cada tipo (la curva de maná se ve al abrir el mazo). Con **Ordenar** (a la derecha) se ordenan las dos secciones por colores, número de colores, nombre, valor, coste medio o cantidad de foils. Al hacer clic en una tarjeta se abre el mazo. Para volver, pulsa el título **Jedhrec** arriba a la izquierda.

### Barra superior
- **Mazos ▾**: muestra el nombre completo del comandante del mazo abierto (o el nombre del mazo si no tiene comandante). Al abrirlo, un menú con los mazos agrupados por identidad de color: Monocolor, Dos colores, Tres colores, Cuatro o más. Cada mazo muestra sus símbolos de color y el nombre de la combinación (Izzet, Jund, Temur…). Al pie aparecen los totales de la colección.
- Junto al menú, dos botones con icono (el nombre aparece al pasar el ratón): **Importar CSV** (también se pueden arrastrar los archivos a la página) y **Nuevo mazo**.
- **Búsqueda**: busca una carta en todos los mazos y muestra en cuáles está, con qué edición y cuántas copias. Junto a la caja están los botones de color (blanco, azul, negro, rojo, verde e incoloro): filtran por el color de la carta, según su coste de maná, y funcionan también sin escribir nada (por ejemplo, solo negro = todas tus cartas negras). Con colores marcados aparece en **Resultados** el menú **Colores**: **Alguno de esos** (la carta tiene al menos uno), **Incluye todos** (los tiene todos y puede tener otros) o **Exactamente esos** (ni más ni menos). En los dos últimos, **Incoloro** solo cuenta si no marcas ningún color. La × quita los colores. Se muestran hasta 120 cartas; si hay más, escribe parte del nombre para acotar. En **Resultados** están las mismas opciones que en Cartas compatibles: **Tipo**, **Ordenar** (nombre, tipo y nombre, precio o coste) y **Vista** (**Lista**, **Cuadrícula** con deslizador de tamaño, o **Tabla** con una fila por copia). En Cuadrícula y Tabla, **Ir** abre el mazo donde está la carta y **Zoom** la muestra en grande. Se recuerdan para la próxima vez.
- **Guardar** (ver [Dónde se guardan los cambios](#dónde-se-guardan-los-cambios)), **Respaldo** y **Tema** (claro u oscuro).

### Cabecera del mazo
- Miniatura del comandante; al hacer clic se abre su ficha. Si el mazo tiene dos (partners), las miniaturas se ven una detrás de otra, aquí y en la página principal; al pasar el ratón, la de atrás pasa al frente.
- Contador **N / 100**: verde si el mazo tiene exactamente 100 cartas.
- Valor, foils, coste medio (sin tierras), cartas distintas y cuántas hay de cada tipo (criaturas, tierras, instantáneos, conjuros, artefactos…), más la curva de maná (sin contar tierras).
- Botones con icono (el nombre aparece al pasar el ratón): **+ Agregar carta** (abre una ventana con cantidad, nombre, edición, precio y foil; arriba se puede pegar el enlace de Scryfall de la impresión y pulsar **Cargar** para llenar el nombre, la edición, el precio y la imagen, solo en la versión local); abajo, **Agregar desde CSV…** suma las cartas de uno o varios CSV al mazo sin borrar las que ya tiene: una carta que ya está con la misma edición y foil solo suma copias. Con la ventana abierta también se pueden arrastrar los CSV, **Exportar** (ver abajo), **Editar mazo** (lápiz: nombre y tipo), **Cartas compatibles** (destellos, solo en mazos de Commander; ver abajo), **Duplicar** y la papelera roja para **Eliminar mazo** (pide confirmación).
- Debajo, la barra: a la izquierda el filtro de cartas del mazo, el **filtro de precio**, **Agrupar** y **Ordenar** (menús desplegables); a la derecha **Vista** y **Ocultar verificadas**.
- **Filtro de precio** ($ mín – máx): muestra solo las cartas cuyo precio por copia está en ese rango, en las tres vistas. Se puede dejar vacío un extremo (solo `5` en mín = $5 o más). La × lo quita. Se aplica a todos los mazos mientras navegas y no se recuerda al recargar la página.

### Cartas compatibles
En un mazo de Commander, el botón **Cartas compatibles** (destellos) abre la lista de todas las cartas que tienes en tus otros mazos y listas cuya **identidad de color** encaja con la del comandante y que este mazo aún no tiene (sin tierras básicas). Si el mazo no tiene comandante marcado, se usan los colores de todas sus cartas.

- Arriba, el filtro por nombre (lupa) y, a su lado, **Ocultar las que están en mazos**. Debajo, **Tipo**, **Ordenar** (por tipo, precio o coste) y **Vista**. Al pasar el ratón se ve la imagen a la izquierda.
- **Vista**, como en el mazo: **Lista** (una tarjeta por carta con todas sus copias), **Cuadrícula** (nombre, tipo e imagen; debajo, dónde está y su precio, con **Mover** y **Zoom**, que muestra la carta en grande y se cierra con un clic o Esc; un deslizador junto a **Vista** cambia su tamaño) o **Tabla** (una fila por copia: carta, coste, tipo, dónde está, cantidad, edición y precio). Se recuerda para la próxima vez.
- **Ocultar las que están en mazos** (ojo) deja solo las copias que tienes en listas de cartas, para no desarmar otro mazo de Commander; se recuerda para la próxima vez.
- Cada carta muestra dónde está (primero las listas; las que están en otro mazo de Commander llevan la etiqueta **mazo**), con edición, foil y precio.
- **Mover** quita una copia de ahí y la pone en este mazo; **Copiar** la agrega sin quitarla. La carta desaparece de la lista en cuanto ya está en el mazo.

### Exportar
| Formato | Resultado |
|---|---|
| **CSV (Excel)** | El mismo formato de tus archivos, con columnas separadas por tabulador. |
| **Moxfield** | Una lista de texto lista para importar en Moxfield: `1 Sol Ring (C16) 272 *F*`. El comandante va primero, `*F*` marca los foils y el código de edición sale del nombre de la edición. La impresión (edición y número de colección) se toma, en este orden, del enlace de Scryfall de la carta (ficha), de la imagen elegida si viene de Scryfall (así el arte coincide), o de su edición; los números que faltan se buscan en Scryfall al abrir **Exportar** (solo en la versión local). Si alguna carta queda sin número, el diálogo lo indica: Moxfield elegirá un arte de esa edición. |

Para pasar un mazo a Moxfield: crea un mazo nuevo (formato Commander), pulsa **Import** y pega la lista. Si Moxfield no reconoce solo al comandante, márcalo en el mazo.

### Vistas
| Vista | Para qué |
|---|---|
| **Lista** | Grupos en columnas, con el coste de maná de cada carta. Al pasar el ratón, la imagen aparece a la izquierda. |
| **Cuadrícula** | Las imágenes de las cartas, una por una, separadas por grupos. Junto a **Ordenar** hay un deslizador para cambiar el tamaño de las cartas (se recuerda para la próxima vez). |
| **Tabla** | Edición rápida: cantidades, edición, foil, precio y eliminar. Indica si una carta también está en otros mazos. |

En Lista y Cuadrícula se puede **agrupar** por Tipo, Coste, Color o sin grupos, y **ordenar** por Nombre, Coste o Precio. Los grupos se pliegan con ▾.

### Verificar cartas contra la carta real
Cada carta tiene una marca ✓ para indicar que ya comparaste su imagen y edición con la carta física: en la esquina de cada carta en Cuadrícula, al final de cada fila en Lista, en la primera columna de Tabla y con el botón **Marcar como verificada** de la ficha. La marca es por mazo (la misma carta en otro mazo se verifica aparte).

El botón **Ocultar verificadas** (en la barra del mazo) esconde las ya marcadas para ver solo las que faltan, y muestra el avance (por ejemplo `3/82` cartas distintas). En Tabla se puede ordenar por la columna ✓.

### Ficha de carta
Se abre al hacer clic en una carta. Desde ahí se puede:
- Cambiar la cantidad, la edición, el precio y el foil.
- Marcarla como **comandante** (se admiten dos, para partners).
- **Enlace de Scryfall**: se puede editar. Si la edición, el precio o la imagen no son los de tu carta, pega el enlace de la impresión correcta (`https://scryfall.com/card/…`) y pulsa **Cargar datos**: llena la edición, el precio (el foil si la carta es foil) y la imagen; se guardan al pulsar **Listo**. Si el enlace es de otra carta (por ejemplo, una que se importó con el nombre equivocado), también cambia el nombre, el tipo y el coste en todas las vistas, y si era el comandante lo sigue siendo. El enlace queda guardado en esa copia y también se usa para el número de colección al exportar a Moxfield. Solo en la versión local; en la línea el enlace se guarda pero la edición y el precio hay que escribirlos a mano.
- **Mover a** otro mazo o lista: eliges el destino y cuántas copias (si tiene más de una). **Mover** la quita de este mazo; **Copiar** la deja en los dos. Se lleva su edición, precio, foil, imagen, enlace y la marca de verificada; si el destino ya tiene esa carta con la misma edición y foil, solo suma copias. Si era el comandante y se mueven todas sus copias, el mazo queda sin comandante.
- Buscarla en StarCityGames, o quitarla del mazo.
- **Cambiar imagen**, ver más abajo.

## Imágenes

| | Versión en línea | Versión local |
|---|---|---|
| Origen de las imágenes | Hojas de imágenes incluidas en la página (`img/s0.jpg`…`s10.jpg`, 60 cartas cada una) | Directamente desde Scryfall (requiere internet) |
| Cartas nuevas | Salen sin imagen, solo con el nombre | Se buscan solas en Scryfall |
| Galería de impresiones al cambiar imagen | No disponible (muestra un enlace a Scryfall) | Sí |
| Pegar imagen (Ctrl+V) o subir archivo | Sí | Sí |

La versión en línea no puede conectarse a sitios externos, así que no puede consultar Scryfall.

**Cambiar imagen:** el cambio se aplica a esa copia de la carta, porque una misma carta puede ser de ediciones distintas en cada mazo. Si la carta está en varios mazos, aparece una casilla para aplicarlo a todas las copias. Al elegir una impresión de la galería también cambian la edición, el precio y el enlace de Scryfall. Para copiar la imagen desde Scryfall: clic derecho sobre la imagen, «Copiar imagen», y luego Ctrl+V en la página.

**Cartas de doble cara** (transformables, MDFC como los Pathways, y reversibles): en la versión local, su imagen lleva un botón ⟳ que le da la vuelta, en la cuadrícula, en la vista previa de la lista y en la ficha. Las cartas divididas (Life // Death) y las de aventura tienen una sola imagen y no llevan botón. La versión en línea todavía no muestra el reverso, porque sus hojas de imágenes solo incluyen el frente.

Los símbolos de maná son los SVG oficiales de Scryfall y van incluidos en la página.

## Dónde se guardan los cambios

**Versión en línea**
- Mientras editas, los cambios quedan como borrador en el navegador.
- **Guardar** (o Ctrl+S) los escribe en `decks.json`, dentro de la página publicada. Desde ese momento se ven en cualquier equipo.
- Las imágenes pegadas o subidas se guardan en el almacén de archivos de la página en cuanto las agregas. El cambio de imagen de la carta solo se conserva al pulsar **Guardar**.

**Versión local**
- Todo se guarda en el almacenamiento del navegador (`localStorage`), no en el archivo `.html`.
- **Guardar** (o Ctrl+S) escribe todos los mazos en un archivo de respaldo `.json` en tu computadora. La primera vez pregunta dónde guardarlo; después sobrescribe ese mismo archivo sin preguntar (en Chrome y Edge; en otros navegadores lo descarga). Junto al botón se ve «Sin guardar» si hay cambios que aún no están en el archivo, o la hora del último guardado.
- Si se abre el archivo en otro navegador o equipo, o se borran los datos de navegación, esos cambios no están o se pierden.
- Las imágenes pegadas ocupan espacio ahí (el navegador da unos 5 MB).

**Las dos versiones no se sincronizan entre sí.** Para pasar un mazo de una a otra, usa **Exportar CSV** en una e **Importar CSV** en la otra, o el respaldo completo (abajo).

### Respaldo (para no perder nada al cambiar de PC)
- **Respaldo → Descargar respaldo** baja un archivo `jedhrec-respaldo-AAAA-MM-DD.json` con todos los mazos: comandantes, ediciones, precios, foils, imágenes cambiadas y los datos de las cartas. Guárdalo en una USB, la nube o el correo.
- **Respaldo → Restaurar desde archivo…** (o arrastrar el `.json` a la página, o elegirlo con **Importar CSV**) **reemplaza todos los mazos** por los del respaldo, previa confirmación. En la versión en línea, pulsa **Guardar** después.
- El diálogo muestra la fecha del último respaldo descargado en ese navegador.
- **Respaldo → Borrar todo** (abajo en el diálogo) elimina todos los mazos para empezar desde cero, previa confirmación. Descarga un respaldo antes si quieres conservarlos. En la versión en línea, pulsa **Guardar** después. En la versión local queda vacía en ese navegador; si la abres en otro navegador o se borran los datos de navegación, vuelven a aparecer los mazos incluidos en el archivo `.html`.

## Regenerar la página

Los scripts de `herramientas/` necesitan Python 3 con Pillow (`pip install pillow`) y conexión a internet.

| Script | Qué hace |
|---|---|
| `fetch_sf.py <carpeta_csv> sf` | Consulta Scryfall: tipo, coste, identidad de color e imagen de cada carta de los CSV. Escribe `sf/meta.json` y descarga las imágenes a `sf/img/`. |
| `fetch_symbols.py` | Descarga los símbolos de maná que usan las cartas a `sf/symbols.json`. |
| `fetch_sets.py` | Descarga la tabla de nombres de edición y sus códigos (para la exportación a Moxfield) a `sf/sets.json`. |
| `build2.py <carpeta_csv> site <html_local>` | Genera desde los CSV las hojas de imágenes (`site/img/`), `site/decks.json`, `site/index.html` y la versión local. |
| `rebuild_pages.py <html_local>` | Solo cambia el código de las páginas (`site/index.html` y la versión local) a partir de `template.html`, sin tocar los datos. |

`template.html` es el código fuente de la página. `__DATA__`, `__SYMBOLS__` y `__SETS__` son marcadores que los scripts reemplazan.

`rebuild_pages.py` con una ruta que no existe crea una página sin mazos; así se genera el `Jedhrec.html` del repositorio.

Regeneración completa con tus CSV en `privado/`, ejecutada desde `herramientas/`:

```sh
PYTHONHASHSEED=0 python fetch_sf.py ../privado sf
python fetch_symbols.py
python fetch_sets.py
python build2.py ../privado site ../privado/JEDHREC.html
python rebuild_pages.py ../privado/JEDHREC.html
```

Solo cambios de código: `python rebuild_pages.py ../privado/JEDHREC.html` (tu página) y, para la del repositorio, borra `../Jedhrec.html` y ejecuta `python rebuild_pages.py ../Jedhrec.html`.

> `PYTHONHASHSEED=0` hace que los nombres de las imágenes descargadas sean los mismos en cada ejecución.

Después hay que publicar la carpeta `site/` en la versión en línea. Eso se hace desde Claude Code.

> **Cuidado:** `build2.py` vuelve a crear `decks.json` desde los CSV. Si se publica, **reemplaza lo guardado en la versión en línea**. Antes de regenerar, exporta los mazos que hayas editado. Para cambios que solo afectan al código, usa `rebuild_pages.py` y publica solo `site/index.html`.

## Pendientes conocidos

- Un mazo sin comandante asignado calcula su identidad de color con todas sus cartas, y puede no ser correcta.
- Las cartas agregadas en la versión en línea no tienen imagen hasta que se regenere la página o se les pegue una.
