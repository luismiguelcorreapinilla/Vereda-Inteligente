"""
JavaScript for Vereda Inteligente.

GeoSpatial Intelligence Lab
"""

JAVASCRIPT = r"""

<script>

import os
import sys
import webbrowser

import geopandas as gpd

# =====================================================
# RUTA BASE
# =====================================================

if getattr(sys, 'frozen', False):
    carpeta_base = os.path.dirname(sys.executable)
else:
    carpeta_base = os.path.dirname(os.path.abspath(__file__))

# =====================================================
# ARCHIVOS
# =====================================================

ruta_geojson = os.path.join(
    carpeta_base,
    "simijaca_completo.geojson"
)

ruta_html = os.path.join(
    carpeta_base,
    "visor_censo.html"
)

ruta_logo = os.path.join(
    carpeta_base,
    "logo.png"
)

ruta_logo = ruta_logo.replace("\\", "/")

# =====================================================
# CARGAR GEOJSON CATASTRAL
# =====================================================

print("Cargando GeoJSON...")

gdf = gpd.read_file(ruta_geojson)

print("Predios cargados:", len(gdf))

geojson_data = gdf.to_json()
# =====================================================
# HTML COMPLETO
# =====================================================

html = """
<!DOCTYPE html>
<html lang="es">

<head>

<meta charset="utf-8">

<title>Censo Veredal</title>

<meta name="viewport" content="width=device-width, initial-scale=1.0">

<link
rel="stylesheet"
href="https://unpkg.com/leaflet/dist/leaflet.css"
/>

<script src="https://unpkg.com/leaflet/dist/leaflet.js"></script>

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>

<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">

<style>

html, body {
    margin: 0;
    padding: 0;
    height: 100%;
    font-family: 'Poppins', sans-serif;
    background: #F4F6F7;
    color: #2C3E50;
}
#container {
    display: flex;
    height: 100vh;
}

#map {
    width: 68%;
    height: 100%;
}

#panel {
    width: 32%;
    height: 100%;
    overflow-y: auto;
    background: #ECF0F1;
    padding: 20px;
    box-sizing: border-box;
    border-left: 1px solid #D5D8DC;
}

h2 {
    font-size: 28px;
    font-weight: 700;
    color: #1E8449;
}

h3 {
    color: #2471A3;
    font-size: 18px;
    margin-bottom: 14px;
}

.section {
    background: #FCFCFC;
    padding: 18px;
    margin-bottom: 18px;
    border-radius: 14px;
    box-shadow: 0 3px 10px rgba(0,0,0,0.08);
    border: 1px solid #EAECEE;
}

input,
select,
textarea {
    width: 100%;
    margin-bottom: 12px;
    padding: 10px;
    box-sizing: border-box;
    border-radius: 10px;
    border: 1px solid #D5D8DC;
    background: white;
    font-size: 14px;
    transition: 0.2s;
}

input:focus,
select:focus,
textarea:focus {
    outline: none;
    border-color: #2471A3;
    box-shadow: 0 0 5px rgba(36,113,163,0.3);
}

textarea {
    height: 70px;
}

button {
    width: 100%;
    padding: 14px;
    background: #1E8449;
    color: white;
    border: none;
    cursor: pointer;
    font-size: 15px;
    font-weight: 600;
    margin-top: 12px;
    border-radius: 12px;
    transition: 0.2s;
}

button:hover {
    background: #27AE60;
    transform: translateY(-1px);
}

.codigo {
    background: #2471A3;
    color: white;
    padding: 14px;
    border-radius: 12px;
    margin-bottom: 18px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.15);
}

</style>

</head>

<body>

<div id="container">

<div id="map"></div>

<div id="panel">

<div style="
display:flex;
align-items:center;
gap:12px;
margin-bottom:20px;
">

<img src='__LOGO__' width='70' style='border-radius:12px;'>

<div>
<h2 style='margin:0;'>Mi Vereda Inteligente</h2>
<div style='color:#5D6D7E;font-size:13px;'>
Plataforma de Gestión Comunitaria
</div>
</div>

</div>

<h2>Censo Veredal</h2>

<div class="codigo">
<b>Código Encuesta:</b>
<div id="codigo_encuesta">SIN SELECCIÓN</div>
</div>

<form id="formulario">

<!-- IDENTIFICACIÓN -->

<div class="section">

<h3>Identificación</h3>

<label>Código Predial</label>
<input type="text" id="codigo_predial" readonly>

<label>Nombre representante</label>
<input type="text" id="representante">

<label>Teléfono</label>
<input type="text" id="telefono">

<label>Tiempo viviendo en la vereda</label>
<input type="text" id="tiempo_vereda">

</div>

<!-- FAMILIA -->

<div class="section">

<h3>Composición Familiar</h3>

<label>Total dependientes</label>
<input type="number" id="dependientes">

<label>Niños 0-5</label>
<input type="number" id="ninos_5">

<label>Niños 6-12</label>
<input type="number" id="ninos_12">

<label>Jóvenes 13-17</label>
<input type="number" id="jovenes">

<label>Adultos mayores</label>
<input type="number" id="adultos">

<label>Personas discapacidad</label>
<input type="number" id="discapacidad">

</div>

<!-- ECONOMÍA -->

<div class="section">

<h3>Economía</h3>

<label>¿Tiene emprendimiento?</label>
<select id="emprendimiento">
<option value="">Seleccionar</option>
<option value="si">Sí</option>
<option value="no">No</option>
</select>

<label>¿Cuál emprendimiento?</label>
<input type="text" id="tipo_emprendimiento">

<label>¿Es productor?</label>
<select id="productor">
<option value="">Seleccionar</option>
<option value="si">Sí</option>
<option value="no">No</option>
</select>

<label>¿Qué produce?</label>
<input type="text" id="produce">

<label>Escala producción</label>
<select id="escala">
<option value="">Seleccionar</option>
<option value="autoconsumo">Autoconsumo</option>
<option value="local">Venta local</option>
<option value="comercial">Comercial</option>
</select>

</div>

<!-- SERVICIOS -->

<div class="section">

<h3>Servicios Públicos</h3>

<label>Agua</label>
<select id="agua">
<option value="">Seleccionar</option>
<option value="si">Sí</option>
<option value="no">No</option>
</select>

<label>Energía</label>
<select id="energia">
<option value="">Seleccionar</option>
<option value="si">Sí</option>
<option value="no">No</option>
</select>

<label>Internet</label>
<select id="internet">
<option value="">Seleccionar</option>
<option value="si">Sí</option>
<option value="no">No</option>
</select>

<label>Alcantarillado</label>
<select id="alcantarillado">
<option value="">Seleccionar</option>
<option value="si">Sí</option>
<option value="no">No</option>
</select>

<label>Gas</label>
<select id="gas">
<option value="">Seleccionar</option>
<option value="si">Sí</option>
<option value="no">No</option>
</select>

<label>Recolección basura</label>
<select id="basura">
<option value="">Seleccionar</option>
<option value="si">Sí</option>
<option value="no">No</option>
</select>

</div>

<!-- SALUD -->

<div class="section">

<h3>Salud</h3>

<label>¿Tiene EPS?</label>
<select id="eps">
<option value="">Seleccionar</option>
<option value="si">Sí</option>
<option value="no">No</option>
</select>

<label>Problemas respiratorios</label>
<select id="respiratorios">
<option value="">Seleccionar</option>
<option value="si">Sí</option>
<option value="no">No</option>
</select>

<label>Problemas gastrointestinales</label>
<select id="gastro">
<option value="">Seleccionar</option>
<option value="si">Sí</option>
<option value="no">No</option>
</select>

<label>Problemas piel</label>
<select id="piel">
<option value="">Seleccionar</option>
<option value="si">Sí</option>
<option value="no">No</option>
</select>

<label>Posibles causas ambientales</label>
<textarea id="causas"></textarea>

<label>Observaciones salud</label>
<textarea id="obs_salud"></textarea>

</div>

<!-- SEGURIDAD -->

<div class="section">

<h3>Seguridad</h3>

<label>¿Ha sufrido robos?</label>
<select id="robos">
<option value="">Seleccionar</option>
<option value="si">Sí</option>
<option value="no">No</option>
</select>

<label>Problemas de microtráfico</label>
<select id="microtrafico">
<option value="">Seleccionar</option>
<option value="si">Sí</option>
<option value="no">No</option>
</select>

<label>Necesita cámaras</label>
<select id="camaras">
<option value="">Seleccionar</option>
<option value="si">Sí</option>
<option value="no">No</option>
</select>

<label>Sector inseguro</label>
<textarea id="sector_inseguro"></textarea>

<label>Observaciones seguridad</label>
<textarea id="obs_seguridad"></textarea>

</div>

<!-- PARTICIPACIÓN -->

<div class="section">

<h3>Participación Comunitaria</h3>

<label>Pertenece a la Junta</label>
<select id="junta">
<option value="">Seleccionar</option>
<option value="si">Sí</option>
<option value="no">No</option>
</select>

<label>Participa reuniones</label>
<select id="reuniones">
<option value="">Seleccionar</option>
<option value="si">Sí</option>
<option value="no">No</option>
</select>

<label>Ha recibido beneficios alcaldía</label>
<select id="beneficios">
<option value="">Seleccionar</option>
<option value="si">Sí</option>
<option value="no">No</option>
</select>

</div>

<!-- OBSERVACIONES -->

<div class="section">

<h3>Observaciones</h3>

<textarea id="observaciones"></textarea>

</div>

<button type="button" onclick="guardarDatos()">
GUARDAR CENSO
</button>

<button type="button" onclick="exportarJSON()">
EXPORTAR JSON
</button>

</form>

</div>

</div>

<script>

var datos = __GEOJSON__;

var map = L.map('map').setView([5.5, -73.85], 17);

L.tileLayer(
'https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png',
{
    attribution: '&copy; OpenStreetMap &copy; CARTO',
    subdomains: 'abcd',
    maxZoom: 22
}
).addTo(map);

// =====================================
// VARIABLES
// =====================================

var selectedFeature = null;
var selectedLayer = null;

var censos = {};
var coloresGuardados = {};

// =====================================
// GENERAR CÓDIGO
// =====================================

function generarCodigoEncuesta(codigo){

    if(!codigo) return "SIN_CODIGO";

    codigo = codigo.toString();

    var parte = codigo.substring(16);

    parte = parte.replace(/^0+/, '');
    parte = parte.replace(/0+$/, '');

    return parte;
}

// =====================================
// ESTILO BASE
// =====================================

function estilo(feature){

    return {
        color: "black",
        weight: 1,
        fillColor: "#3388ff",
        fillOpacity: 0.3
    };
}

// =====================================
// CARGAR DATOS FORMULARIO
// =====================================

function cargarFormulario(d){

    document.getElementById("representante").value =
        d.representante || "";

    document.getElementById("telefono").value =
        d.telefono || "";

    document.getElementById("tiempo_vereda").value =
        d.tiempo_vereda || "";

    document.getElementById("dependientes").value =
        d.dependientes || "";

    document.getElementById("ninos_5").value =
        d.ninos_5 || "";

    document.getElementById("ninos_12").value =
        d.ninos_12 || "";

    document.getElementById("jovenes").value =
        d.jovenes || "";

    document.getElementById("adultos").value =
        d.adultos || "";

    document.getElementById("discapacidad").value =
        d.discapacidad || "";

    document.getElementById("emprendimiento").value =
        d.emprendimiento || "";

    document.getElementById("tipo_emprendimiento").value =
        d.tipo_emprendimiento || "";

    document.getElementById("productor").value =
        d.productor || "";

    document.getElementById("produce").value =
        d.produce || "";

    document.getElementById("escala").value =
        d.escala || "";

    document.getElementById("agua").value =
        d.agua || "";

    document.getElementById("energia").value =
        d.energia || "";

    document.getElementById("internet").value =
        d.internet || "";

    document.getElementById("alcantarillado").value =
        d.alcantarillado || "";

    document.getElementById("gas").value =
        d.gas || "";

    document.getElementById("basura").value =
        d.basura || "";

    document.getElementById("eps").value =
        d.eps || "";

    document.getElementById("respiratorios").value =
        d.respiratorios || "";

    document.getElementById("gastro").value =
        d.gastro || "";

    document.getElementById("piel").value =
        d.piel || "";

    document.getElementById("causas").value =
        d.causas || "";

    document.getElementById("obs_salud").value =
        d.obs_salud || "";

    document.getElementById("robos").value =
        d.robos || "";

    document.getElementById("microtrafico").value =
        d.microtrafico || "";

    document.getElementById("camaras").value =
        d.camaras || "";

    document.getElementById("sector_inseguro").value =
        d.sector_inseguro || "";

    document.getElementById("obs_seguridad").value =
        d.obs_seguridad || "";

    document.getElementById("junta").value =
        d.junta || "";

    document.getElementById("reuniones").value =
        d.reuniones || "";

    document.getElementById("beneficios").value =
        d.beneficios || "";

    document.getElementById("observaciones").value =
        d.observaciones || "";

}

// =====================================
// CLICK PREDIO
// =====================================

function onEachFeature(feature, layer){

    layer.on('click', function(){

        // =========================
        // RESTAURAR ANTERIOR
        // =========================

        if(selectedLayer && selectedFeature){

            var codigoAnterior =
                selectedFeature.properties.CODIGO;

            if(coloresGuardados[codigoAnterior]){

                selectedLayer.setStyle({
                    fillColor:
                        coloresGuardados[codigoAnterior],
                    fillOpacity:0.6,
                    color:"black",
                    weight:1
                });

            } else {

                selectedLayer.setStyle({
                    fillColor:"#3388ff",
                    fillOpacity:0.3,
                    color:"black",
                    weight:1
                });

            }

        }

        // =========================
        // NUEVO SELECCIONADO
        // =========================

        selectedFeature = feature;
        selectedLayer = layer;

        layer.setStyle({
            fillColor:"yellow",
            fillOpacity:0.7
        });

        var codigo =
            feature.properties.CODIGO || "";

        document.getElementById(
            "codigo_predial"
        ).value = codigo;

        document.getElementById(
            "codigo_encuesta"
        ).innerHTML =
            generarCodigoEncuesta(codigo);

        // =========================
        // SI YA EXISTE CENSO
        // =========================

        if(censos[codigo]){

            cargarFormulario(
                censos[codigo]
            );

        } else {

            document.getElementById(
                "formulario"
            ).reset();

            document.getElementById(
                "codigo_predial"
            ).value = codigo;

            document.getElementById(
                "codigo_encuesta"
            ).innerHTML =
                generarCodigoEncuesta(codigo);

        }

    });

}

// =====================================
// GEOJSON
// =====================================

var geojson = L.geoJSON(datos, {
    style: estilo,
    onEachFeature: onEachFeature
}).addTo(map);

map.fitBounds(
    geojson.getBounds()
);

// =====================================
// GUARDAR
// =====================================

function guardarDatos(){

    if(!selectedFeature){

        alert("Seleccione un predio");

        return;
    }

    var datosFormulario = {

        codigo_predial:
            document.getElementById("codigo_predial").value,

        codigo_encuesta:
            document.getElementById("codigo_encuesta").innerHTML,

        representante:
            document.getElementById("representante").value,

        telefono:
            document.getElementById("telefono").value,

        tiempo_vereda:
            document.getElementById("tiempo_vereda").value,

        dependientes:
            document.getElementById("dependientes").value,

        ninos_5:
            document.getElementById("ninos_5").value,

        ninos_12:
            document.getElementById("ninos_12").value,

        jovenes:
            document.getElementById("jovenes").value,

        adultos:
            document.getElementById("adultos").value,

        discapacidad:
            document.getElementById("discapacidad").value,

        emprendimiento:
            document.getElementById("emprendimiento").value,

        tipo_emprendimiento:
            document.getElementById("tipo_emprendimiento").value,

        productor:
            document.getElementById("productor").value,

        produce:
            document.getElementById("produce").value,

        escala:
            document.getElementById("escala").value,

        agua:
            document.getElementById("agua").value,

        energia:
            document.getElementById("energia").value,

        internet:
            document.getElementById("internet").value,

        alcantarillado:
            document.getElementById("alcantarillado").value,

        gas:
            document.getElementById("gas").value,

        basura:
            document.getElementById("basura").value,

        eps:
            document.getElementById("eps").value,

        respiratorios:
            document.getElementById("respiratorios").value,

        gastro:
            document.getElementById("gastro").value,

        piel:
            document.getElementById("piel").value,

        causas:
            document.getElementById("causas").value,

        obs_salud:
            document.getElementById("obs_salud").value,

        robos:
            document.getElementById("robos").value,

        microtrafico:
            document.getElementById("microtrafico").value,

        camaras:
            document.getElementById("camaras").value,

        sector_inseguro:
            document.getElementById("sector_inseguro").value,

        obs_seguridad:
            document.getElementById("obs_seguridad").value,

        junta:
            document.getElementById("junta").value,

        reuniones:
            document.getElementById("reuniones").value,

        beneficios:
            document.getElementById("beneficios").value,

        observaciones:
            document.getElementById("observaciones").value

    };

    var codigo =
        datosFormulario.codigo_predial;

    censos[codigo] =
        datosFormulario;

    // =========================
    // COLOR
    // =========================

    var color = "#3388ff";

    if(datosFormulario.junta == "si"){
        color = "green";
    }

    if(datosFormulario.robos == "si"){
        color = "red";
    }

    coloresGuardados[codigo] =
        color;

    selectedLayer.setStyle({
        fillColor: color,
        fillOpacity: 0.6
    });

    alert("Censo guardado");

}

// =====================================
// EXPORTAR JSON
// =====================================

function exportarJSON(){

    var dataStr =
        "data:text/json;charset=utf-8," +
        encodeURIComponent(
            JSON.stringify(
                Object.values(censos),
                null,
                2
            )
        );

    var dlAnchor =
        document.createElement('a');

    dlAnchor.setAttribute(
        "href",
        dataStr
    );

    dlAnchor.setAttribute(
        "download",
        "censo_veredal.json"
    );

    document.body.appendChild(dlAnchor);

    dlAnchor.click();

    dlAnchor.remove();

}

</script>
</body>
</html>
"""



# =====================================================
# INSERTAR GEOJSON
# =====================================================

html = html.replace(
    "__GEOJSON__",
    geojson_data
)

# =====================================================
# INSERTAR LOGO
# =====================================================

html = html.replace(
    "__LOGO__",
    "file:///" + ruta_logo
)
# =====================================================
# GUARDAR HTML
# =====================================================

with open(
    ruta_html,
    "w",
    encoding="utf-8"
) as f:

    f.write(html)

print("VISOR CENSO GENERADO")

# =====================================================
# ABRIR VISOR
# =====================================================

webbrowser.open(
    "file://" + ruta_html
)

<script>
