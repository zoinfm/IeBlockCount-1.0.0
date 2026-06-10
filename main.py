# -*- coding: utf-8 -*-
"""
Módulo: main.py
Descripción: Punto de entrada del programa. Orquesta la conexión, selección,
             análisis y visualización de resultados.
Autor: @ZOIN_ZE
Fecha: 2026-06-10
Versión: 1.0
"""


from cad_connector import CadConnector
from layer_filter import LayerFilter
from block_geometry import BlockGeometry
from attribute_reader import AttributeReader
from circuit_analyzer import CircuitAnalyzer
from output_formatter import OutputFormatter

def main():
    print("\n🔌 Conectando con AutoCAD...")
    cad = CadConnector()
    if not cad.connect():
        return

    # 1. Selección del bloque tablero
    ss_tablero = cad.select_objects(
        ">>> En AutoCAD, SELECCIONE el bloque que representa el TABLERO y presione ENTER <<<",
        "SS_TABLERO"
    )
    if not ss_tablero or ss_tablero.Count == 0:
        print("❌ No se seleccionó ningún bloque. Abortando.")
        return
    obj_tablero = ss_tablero.Item(0)
    if obj_tablero.ObjectName != "AcDbBlockReference":
        print("❌ El objeto seleccionado no es un bloque. Abortando.")
        return
    tablero_pos = BlockGeometry.get_center(obj_tablero)
    print(f"✅ Tablero: {obj_tablero.Name} | Centro: ({tablero_pos[0]:.2f}, {tablero_pos[1]:.2f})")
    ss_tablero.Delete()

    # 2. Selección de bloques a analizar
    ss_bloques = cad.select_objects(
        ">>> En AutoCAD, SELECCIONE los bloques (luminarias, equipos) que contienen el atributo y presione ENTER <<<",
        "SS_BLOQUES"
    )
    if not ss_bloques:
        return

    analyzer = CircuitAnalyzer(tablero_pos)
    processed = 0
    for i in range(ss_bloques.Count):
        obj = ss_bloques.Item(i)
        if obj.ObjectName != "AcDbBlockReference":
            continue
        if not LayerFilter.is_visible_and_unlocked(cad.doc, obj.Layer):
            continue
        valor = AttributeReader.get_attribute_value(obj, "$circuito")
        if valor:
            pos = BlockGeometry.get_center(obj)
            analyzer.add_block(valor, obj.Name, pos)
            processed += 1
    ss_bloques.Delete()

    if processed == 0:
        print("⚠️ No se encontraron bloques con atributo '$circuito' en capas visibles/desbloqueadas.")
        return

    # 3. Obtener resultados
    summary = analyzer.get_summary()
    type_counts = analyzer.get_type_counts()

    # 4. Mostrar en consola
    OutputFormatter.print_average_table(summary)
    OutputFormatter.print_type_counts(type_counts)
    OutputFormatter.print_summary(summary)

    # 5. Copiar al portapapeles
    OutputFormatter.copy_to_clipboard(summary, type_counts)

    print("\n🎯 Análisis finalizado.")

if __name__ == "__main__":
    main()