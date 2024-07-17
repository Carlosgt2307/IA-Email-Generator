# Email Generator

## Descripción
Email Generator es una aplicación web que utiliza la API de Google Generative AI para generar correos electrónicos personalizados. La aplicación permite a los usuarios especificar el autor, receptor, tono, asunto, contexto, longitud del correo y opcionalmente añadir líneas implícitas y descripciones de archivos adjuntos.

## Instalación

- Generamos una clonación del repositorio
```
git clone https://github.com/Carlosgt2307/IA-Email-Generator.git
```

- Crear y Activar un Entorno Virtual:
```
py -m venv venv
venv\Scripts\activate
```

- Crear y Activar un Entorno Virtual:
```
pip install -r requirements.txt
```

- Configurar Variables de Entorno: Crea un archivo .env en el directorio raíz del proyecto y añade tu clave de API
```
API_KEY=YOUR_API_KEY_HERE
```
## Uso

- Ejecutar la Aplicación:
```
python app.py
```
- Abrir en el Navegador: Ve a http://127.0.0.1:5000 en tu navegador para usar la aplicación.
