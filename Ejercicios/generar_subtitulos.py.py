from datetime import timedelta

import whisper

# Ruta del video
VIDEO = "Akon - Ghetto (Official Music Video)(720P_HD).mp4"

# Cargar modelo
modelo = whisper.load_model("base")

# Transcribir
resultado = modelo.transcribe(VIDEO, language="en")


# Convertir segundos a formato SRT
def formato_tiempo(segundos):
    tiempo = timedelta(seconds=segundos)

    horas = tiempo.seconds // 3600
    minutos = (tiempo.seconds % 3600) // 60
    segundos = tiempo.seconds % 60
    milisegundos = int(tiempo.microseconds / 1000)

    return f"{horas:02}:{minutos:02}:{segundos:02},{milisegundos:03}"


# Crear archivo SRT
with open("subtitulos.srt", "w", encoding="utf-8") as archivo:

    for i, segmento in enumerate(resultado["segments"], start=1):

        inicio = formato_tiempo(segmento["start"])
        fin = formato_tiempo(segmento["end"])
        texto = segmento["text"].strip()

        archivo.write(f"{i}\n")
        archivo.write(f"{inicio} --> {fin}\n")
        archivo.write(f"{texto}\n\n")

print("Archivo subtitulos.srt generado correctamente")
