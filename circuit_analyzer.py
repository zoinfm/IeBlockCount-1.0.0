# -*- coding: utf-8 -*-
"""
Módulo: circuit_analyzer.py
Descripción: Procesa bloques, cuenta por tipo y acumula distancias Manhattan.
Autor: @ZOIN_ZE
Fecha: 2026-06-10
Versión: 1.0
"""


from collections import defaultdict


class CircuitAnalyzer:
    """Procesa los bloques: cuenta por tipo y acumula distancias Manhattan."""

    def __init__(self, tablero_pos):
        self.tablero_pos = tablero_pos
        self.count_by_type = defaultdict(int)  # (valor, nombre_bloque) -> cantidad
        self.sum_dist_by_value = defaultdict(float)
        self.count_by_value = defaultdict(int)

    def add_block(self, circuit_value, block_name, block_pos):
        """Agrega un bloque al análisis."""
        key = (circuit_value, block_name)
        self.count_by_type[key] += 1

        dist = block_geometry.BlockGeometry.manhattan_distance(block_pos, self.tablero_pos)
        self.sum_dist_by_value[circuit_value] += dist
        self.count_by_value[circuit_value] += 1

    def get_average_distances(self):
        """Retorna dict {valor: promedio_distancia}."""
        avg = {}
        for val in self.sum_dist_by_value:
            avg[val] = self.sum_dist_by_value[val] / self.count_by_value[val]
        return avg

    def get_summary(self):
        """Retorna lista de tuplas (valor, total_bloques, promedio_dist) ordenada."""
        avg = self.get_average_distances()
        summary = [(val, self.count_by_value[val], avg[val]) for val in self.count_by_value]
        summary.sort(key=lambda x: x[0])  # ordenar por valor
        return summary

    def get_type_counts(self):
        """Retorna lista de tuplas (valor, nombre_bloque, cantidad) ordenada."""
        items = [(val, nombre, cant) for (val, nombre), cant in self.count_by_type.items()]
        items.sort(key=lambda x: (x[0], x[1]))
        return items