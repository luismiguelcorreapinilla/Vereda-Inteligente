"""
CSS styles for Vereda Inteligente.

GeoSpatial Intelligence Lab
"""

STYLES = """

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


<style>
"""

}
