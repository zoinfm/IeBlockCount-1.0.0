# -*- coding: utf-8 -*-
"""
Módulo: attribute_reader.py
Descripción: Lee el valor de un atributo específico en un bloque.
Autor: @ZOIN_ZE
Fecha: 2026-06-10
Versión: 1.0
"""


class AttributeReader:
    """Lee el valor de un atributo específico en un bloque."""

    @staticmethod
    def get_attribute_value(block_ref, tag_name="$circuito"):
        """Retorna el valor del atributo (insensible a mayúsculas) o None."""
        try:
            for att in block_ref.GetAttributes():
                if att.TagString.upper() == tag_name.upper():
                    return att.TextString.strip()
        except:
            pass
        return None