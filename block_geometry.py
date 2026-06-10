# -*- coding: utf-8 -*-
"""
Módulo: block_geometry.py
Descripción: Funciones para obtener posición real de bloques y calcular distancias.
Autor: @ZOIN_ZE
Fecha: 2026-06-10
Versión: 1.0
"""


import math


class BlockGeometry:
    """Funciones para obtener posición real de bloques y distancias."""

    @staticmethod
    def get_center(obj):
        """Retorna el centro del bounding box del bloque (x, y)."""
        try:
            min_p, max_p = obj.GetBoundingBox()
            center_x = (float(min_p[0]) + float(max_p[0])) / 2.0
            center_y = (float(min_p[1]) + float(max_p[1])) / 2.0
            return (center_x, center_y)
        except:
            return (float(obj.InsertionPoint[0]), float(obj.InsertionPoint[1]))

    @staticmethod
    def manhattan_distance(p1, p2):
        """Distancia Manhattan entre dos puntos (x1,y1) y (x2,y2)."""
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])