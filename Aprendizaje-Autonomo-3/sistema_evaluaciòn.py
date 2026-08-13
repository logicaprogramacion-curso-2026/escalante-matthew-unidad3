import json
import os

# ==========================================
# CAPA 1: DATOS (Carga de preguntas)
# ==========================================
def cargar_examen(ruta_archivo: str) -> list:
    """Carga el banco de preguntas desde un archivo JSON."""
    if not os.path.exists(ruta_archivo):
        print(f"Error: El archivo '{ruta_archivo}' no existe.")
        return []
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as file:
            return json.load(file)
    except json.JSONDecodeError:
        print("Error al leer el archivo JSON. Verifica la sintaxis.")
        return []


# ==========================================
# CAPA 2: LÓGICA (Evaluación y Normalización)
# ==========================================
def normalizar_texto(texto: str) -> str:
    """Limpia la entrada eliminando espacios extra y pasando a minúsculas."""
    return texto.strip().lower()


def evaluar_respuesta(pregunta: dict, respuesta_usuario: str) -> tuple[bool, str]:
    """
    Compara la respuesta entregada con la respuesta correcta según el tipo.
    Aplica normalización a minúsculas y eliminación de espacios.
    """
    tipo = pregunta["tipo"]
    correcta = pregunta["respuesta_correcta"]

    if tipo in ["opcion_multiple", "verdadero_falso", "completar_espacio"]:
        resp_norm = normalizar_texto(respuesta_usuario)
        corr_norm = normalizar_texto(str(correcta))
        # Quitar acentos básicos para completar espacios
        resp_norm = resp_norm.replace('á','a').replace('é','e').replace('í','i').replace('ó','o').replace('ú','u')
        corr_norm = corr_norm.replace('á','a').replace('é','e').replace('í','i').replace('ó','o').replace('ú','u')
        
        es_correcta = (resp_norm == corr_norm)

    elif tipo in ["opcion_multiple_varias", "emparejamiento"]:
        # Convierte respuestas separadas por coma en una lista limpia y ordenada
        resp_lista = [normalizar_texto(x) for x in respuesta_usuario.split(",") if x.strip()]
        
        if tipo == "opcion_multiple_varias":
            es_correcta = sorted(resp_lista) == sorted([normalizar_texto(x) for x in correcta])
        else: # emparejamiento (mantiene el orden estricto de coincidencia)
            es_correcta = resp_lista == [normalizar_texto(x) for x in correcta]

    else:
        es_correcta = False

    retro = "" if es_correcta else pregunta.get("retroalimentacion_error", "Respuesta incorrecta.")
    return es_correcta, retro


# ==========================================
# CAPA 3: CLI (Interfaz de Línea de Comandos)
# ==========================================
def ejecutar_examen(preguntas: list):
    """Controla el flujo de presentación del examen y entrega los resultados."""
    if not preguntas:
        print("No hay preguntas disponibles para el examen.")
        return

    puntaje_total = 0.0
    puntaje_maximo = sum(p["puntaje"] for p in preguntas)
    resultados = []

    print("\n" + "=" * 50)
    print("      INICIO DEL EXAMEN AUTOMÁTICO")
    print("=" * 50)

    for idx, p in enumerate(preguntas, 1):
        print(f"\nPregunta {idx} [{p['puntaje']} pts]")
        print(p["pregunta"])

        if "opciones" in p:
            for opt in p["opciones"]:
                print(f"  {opt}")

        respuesta = input("\n> Tu respuesta: ")
        es_correcta, retro = evaluar_respuesta(p, respuesta)

        if es_correcta:
            puntaje_total += p["puntaje"]

        resultados.append({
            "numero": idx,
            "pregunta": p["pregunta"],
            "correcta": es_correcta,
            "respuesta_dada": respuesta,
            "puntaje_obtenido": p["puntaje"] if es_correcta else 0,
            "retroalimentacion": retro
        })

    # Imprimir Reporte Final
    print("\n" + "=" * 50)
    print("           RESUMEN DE RESULTADOS")
    print("=" * 50)
    print(f"PUNTAJE FINAL: {puntaje_total:.2f} / {puntaje_maximo:.2f}\n")

    for r in resultados:
        estado = "Correcta" if r["correcta"] else "Incorrecta"
        print(f"Pregunta {r['numero']}: [{estado}] - {r['puntaje_obtenido']} pts")
        if not r["correcta"]:
            print(f"   Retroalimentación: {r['retroalimentacion']}")
    print("=" * 50)


def menu_principal():
    """Menú interactivo CLI."""
    while True:
        print("\n=== SISTEMA DE EVALUACIÓN EDUCATIVA ===")
        print("1. Seleccionar y responder examen (preguntas.json)")
        print("2. Salir")
        
        opcion = input("\nSelecciona una opción (1-2): ").strip()

        if opcion == "1":
            archivo = "preguntas.json"
            preguntas = cargar_examen(archivo)
            if preguntas:
                ejecutar_examen(preguntas)
        elif opcion == "2":
            print("Saliendo del sistema. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intenta nuevamente.")


if __name__ == "__main__":
    menu_principal()