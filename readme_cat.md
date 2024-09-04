# Traductor de Fitxers SRT

Per Marc Alier, @granludo

Aquest projecte proporciona un script per traduir fitxers de subtítols SRT de l'anglès a un idioma de destinació especificat utilitzant el model GPT-4 d'OpenAI.

## Característiques

- Tradueix fitxers SRT mantenint el format original i el temps
- Suporta traducció per lots per millorar l'eficiència
- Interfície de línia de comandes per a un ús fàcil

## Requisits

- Python 3.6+
- Clau API d'OpenAI

## Instal·lació

1. Clona aquest repositori:
   ```
   git clone https://github.com/elteunomdusuari/srt-translator.git
   cd srt-translator
   ```

2. Instal·la els paquets requerits:
   ```
   pip install -r requirements.txt
   ```

3. Configura la teva clau API d'OpenAI:
   ```
   export OPENAI_API_KEY=your_key
   ```

## Ús

Per traduir un sol fitxer SRT:
    ```
    python3 translate_srt.py <fitxer_entrada> <fitxer_sortida> --source_language <idioma_origen> --target_language <idioma_desti>
    ```


Per traduir tots els fitxers SRT al directori actual:
    ```
    ./translate.sh <idioma_desti>
    ```
