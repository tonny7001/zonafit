import os
import re
from tkinter import Tk, filedialog, messagebox


def formatear_tiempo(segundos):
    horas = int(segundos // 3600)
    minutos = int((segundos % 3600) // 60)
    segs = int(segundos % 60)
    milisegundos = int((segundos - int(segundos)) * 1000)

    return f"{horas:02}:{minutos:02}:{segs:02},{milisegundos:03}"


def convertir_lrc_a_srt(archivo_lrc):
    datos = []

    with open(archivo_lrc, "r", encoding="utf-8") as f:
        lineas = f.readlines()

    patron = r"\[(\d+):(\d+\.\d+)\](.*)"

    for linea in lineas:
        match = re.match(patron, linea)

        if match:
            minutos = int(match.group(1))
            segundos = float(match.group(2))
            texto = match.group(3).strip()

            tiempo_total = minutos * 60 + segundos

            if texto:
                datos.append((tiempo_total, texto))

    if not datos:
        raise ValueError("No se encontraron líneas sincronizadas en el archivo LRC.")

    nombre_srt = os.path.splitext(archivo_lrc)[0] + ".srt"

    with open(nombre_srt, "w", encoding="utf-8") as srt:

        for i in range(len(datos)):

            inicio = datos[i][0]

            if i < len(datos) - 1:
                fin = datos[i + 1][0]
            else:
                fin = inicio + 3

            srt.write(f"{i + 1}\n")
            srt.write(f"{formatear_tiempo(inicio)} --> {formatear_tiempo(fin)}\n")
            srt.write(f"{datos[i][1]}\n\n")

    return nombre_srt


def main():

    root = Tk()
    root.withdraw()

    archivo_lrc = filedialog.askopenfilename(
        title="Selecciona un archivo LRC", filetypes=[("Archivos LRC", "*.lrc")]
    )

    if not archivo_lrc:
        print("No se seleccionó ningún archivo.")
        return

    try:
        archivo_srt = convertir_lrc_a_srt(archivo_lrc)

        messagebox.showinfo(
            "Conversión completada",
            f"Archivo SRT creado correctamente:\n\n{archivo_srt}",
        )

        print(f"SRT generado: {archivo_srt}")

    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error:\n\n{e}")

        print(f"Error: {e}")


if __name__ == "__main__":
    main()
