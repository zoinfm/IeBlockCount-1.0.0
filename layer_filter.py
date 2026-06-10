# -*- coding: utf-8 -*-
"""
Módulo: layer_filter.py
Descripción: Filtra capas visibles y desbloqueadas.
Autor: @ZOIN_ZE
Fecha: 2026-06-10
Versión: 1.0
"""


class LayerFilter:
    """Verifica si una capa está visible y desbloqueada."""

    @staticmethod
    def is_visible_and_unlocked(doc, layer_name):
        """Retorna True si la capa está encendida, descongelada y no bloqueada."""
        try:
            layer = doc.Layers.Item(layer_name)
            return layer.LayerOn and not layer.Freeze and not layer.Lock
        except:
            return False