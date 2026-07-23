"""
HTML template for Vereda Inteligente.

GeoSpatial Intelligence Lab
"""

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="es">

<head>

<meta charset="utf-8">

<title>Vereda Inteligente</title>

<meta name="viewport"
content="width=device-width, initial-scale=1.0">

<link
rel="stylesheet"
href="https://unpkg.com/leaflet/dist/leaflet.css"
/>

<script src="https://unpkg.com/leaflet/dist/leaflet.js"></script>

<link rel="preconnect"
href="https://fonts.googleapis.com">

<link rel="preconnect"
href="https://fonts.gstatic.com"
crossorigin>

<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap"
rel="stylesheet">

<style>

{{STYLES}}

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

<img src="__LOGO__" width="70" style="border-radius:12px;">

<div>

<h2 style="margin:0;">Mi Vereda Inteligente</h2>

<div style="color:#5D6D7E;font-size:13px;">
Plataforma de Gestión Comunitaria
</div>

</div>

</div>

<h2>Censo Veredal</h2>

<div class="codigo">

<b>Código Encuesta:</b>

<div id="codigo_encuesta">

SIN SELECCIÓN

</div>

</div>

<form id="formulario">

</form>

</div>

</div>

<script>

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



</script>

</body>

</html>
"""
