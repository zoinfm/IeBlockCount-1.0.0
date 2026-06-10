# -*- coding: utf-8 -*-
"""
Módulo: output_formatter.py
Descripción: Muestra resultados en consola y copia al portapapeles.
Autor: @ZOIN_ZE
Fecha: 2026-06-10
Versión: 1.0
"""


import subprocess


class OutputFormatter:
    """Muestra resultados en consola y copia al portapapeles."""

    @staticmethod
    def print_average_table(summary):
        """Imprime tabla de distancias promedio por circuito."""
        print("\n📊 DISTANCIA MANHATTAN PROMEDIO AL TABLERO POR VALOR DE CIRCUITO")
        print("-" * 80)
        print(f"{'Valor $circuito':<25} | {'Cantidad bloques':<18} | {'Dist. Manhattan promedio':<25}")
        print("-" * 80)
        for valor, total, avg_dist in summary:
            print(f"{valor:<25} | {total:<18} | {avg_dist:<25.2f}")

    @staticmethod
    def print_type_counts(type_counts):
        """Imprime tabla de conteo por tipo de bloque y circuito."""
        print("\n" + "=" * 110)
        print("📋 CONTEO POR TIPO DE BLOQUE Y CIRCUITO")
        print("=" * 110)
        print(f"{'Valor $circuito':<25} | {'Nombre del Bloque':<35} | {'Cantidad':<10}")
        print("-" * 80)
        for valor, nombre, cant in type_counts:
            print(f"{valor:<25} | {nombre:<35} | {cant:<10}")

    @staticmethod
    def print_summary(summary):
        """Imprime resumen por valor de circuito."""
        print("\n" + "=" * 110)
        print("📌 RESUMEN POR VALOR DE CIRCUITO")
        print("=" * 110)
        for valor, total, avg_dist in summary:
            print(f"{valor:<25} : {total} bloques | Dist. promedio: {avg_dist:.2f}")

    @staticmethod
    def copy_to_clipboard(summary, type_counts):
        """Copia datos al portapapeles en formato tabulado para Excel."""
        excel_data = "=== DISTANCIAS MANHATTAN PROMEDIO ===\n"
        excel_data += "Valor $circuito\tCantidad bloques\tDistancia Manhattan promedio\n"
        for valor, total, avg in summary:
            excel_data += f"{valor}\t{total}\t{avg:.2f}\n"

        excel_data += "\n=== CONTEO POR TIPO DE BLOQUE ===\n"
        excel_data += "Valor $circuito\tNombre Bloque\tCantidad\n"
        for valor, nombre, cant in type_counts:
            excel_data += f"{valor}\t{nombre}\t{cant}\n"

        excel_data += "\n=== RESUMEN POR CIRCUITO ===\n"
        excel_data += "Valor $circuito\tTotal bloques\tDistancia promedio\n"
        for valor, total, avg in summary:
            excel_data += f"{valor}\t{total}\t{avg:.2f}\n"

        try:
            proc = subprocess.Popen('clip', stdin=subprocess.PIPE, close_fds=True, shell=True)
            proc.communicate(input=excel_data.encode('utf-8'))
            print("\n[✔] Datos completos copiados al portapapeles (Ctrl+V en Excel).")
        except Exception as e:
            print(f"\n[!] No se pudo copiar al portapapeles: {e}")