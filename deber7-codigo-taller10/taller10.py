def proceso_evaluacion_formativa_ia():
    """
    Proceso de Evaluación Formativa de Competencias Digitales Asistida por IA
    Traducción en Python del pseudocódigo Taller 10.
    """
    while True:
        print("==========================================================")
        print(" PROCESO DE EVALUACIÓN FORMATIVA DE COMPETENCIAS DIGITALES")
        print("==========================================================")

        # FASE 1: DEFINICIÓN DE OBJETIVOS Y COMPETENCIAS
        print("1. Identificando Competencias Digitales (DigComp) y Objetivos de Aprendizaje...")
        print("2. Definiendo Criterios de Evaluación y Rúbricas (con apoyo de IA)...")

        # FASE 2: DISEÑO Y ADAPTACIÓN DE ACTIVIDADES
        print("3. Creando Actividades de Aprendizaje y Evaluación Digitales...")
        print("4. Integrando Herramientas de IA para Recopilación de Datos...")

        # FASE 3: IMPLEMENTACIÓN Y EVALUACIÓN
        print("5. Estudiantes completan actividades en el entorno digital...")
        print("6. Herramientas de IA capturan y analizan el desempeño en tiempo real...")

        # FASE 4: DECISIÓN Y RETROALIMENTACIÓN ASISTIDA POR IA
        respuesta_retro = input("\n¿El estudiante necesita retroalimentación inmediata? (si/no): ").strip().upper()

        if respuesta_retro == "SI":
            print("\n[7.a] Generando retroalimentación automatizada y recursos por IA...")
            print("Reorientando al estudiante hacia las actividades de aprendizaje...")
        else:
            print("\n[8] Herramientas de IA generan visualizaciones y diagnósticos de progreso individual y grupal.")

        # FASE 5: MONITORIZACIÓN Y AJUSTES DEL DOCENTE
        print("\n9. El docente revisa informes de la IA y ajusta la enseñanza y el apoyo...")

        # FASE 6: MEJORA CONTINUA (ITERACIÓN)
        print("10. Iteración del proceso de evaluación para fortalecer competencias.")

        continuar_iteracion = input("\n¿Desea iniciar un nuevo ciclo de mejora continua? (si/no): ").strip().upper()

        if continuar_iteracion == "NO":
            break

    print("\nProceso de evaluación asistida por IA finalizado exitosamente.")

if __name__ == "__main__":
    proceso_evaluacion_formativa_ia()