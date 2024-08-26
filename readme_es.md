# Traductor de Archivos SRT

Por Marc Alier, @granludo

Este proyecto proporciona un script para traducir archivos de subtítulos SRT del inglés a un idioma de destino especificado utilizando el modelo GPT-4 de OpenAI.

## Características

- Traduce archivos SRT manteniendo el formato original y el tiempo
- Admite traducción por lotes para mejorar la eficiencia
- Interfaz de línea de comandos para un uso fácil

## Requisitos

- Python 3.6+
- Clave API de OpenAI

## Instalación

1. Clona este repositorio:
   ```
   git clone https://github.com/tuusuario/srt-translator.git
   cd srt-translator
   ```

2. Instala los paquetes requeridos:
   ```
   pip install openai tqdm
   ```

3. Configura tu clave API de OpenAI:
   Crea un archivo llamado `mykey.json` en el directorio padre del script con el siguiente contenido:
   ```json
   {
     "key": "tu-clave-api-de-openai-aquí"
   }
   ```

## Uso

Para traducir un solo archivo SRT:


    ```
 python3 translate_srt.py <archivo_entrada> <archivo_salida> --source_language <idioma_origen> --target_language <idioma_destino>
    ```

Para traducir todos los archivos SRT en el directorio actual:

    ```
    ./translate.sh <idioma_destino>
    ```