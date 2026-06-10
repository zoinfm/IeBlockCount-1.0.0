# -*- coding: utf-8 -*-
"""
Módulo: cad_connector.py
Descripción: Maneja la conexión con AutoCAD y la selección de objetos.
Autor: @ZOIN_ZE
Fecha: 2026-06-10
Versión: 1.0
"""


from pyautocad import Autocad


class CadConnector:
    """Maneja la conexión con AutoCAD y la selección de objetos."""

    def __init__(self):
        self.acad = None
        self.doc = None

    def connect(self):
        """Establece conexión con AutoCAD."""
        try:
            self.acad = Autocad(create_if_not_exists=True)
            self.doc = self.acad.doc
            print(f"✅ Conectado: {self.doc.Name}")
            return True
        except Exception as e:
            print(f"❌ Error de conexión: {e}")
            return False

    def select_objects(self, prompt_message, selection_set_name="SS_TEMP"):
        """Solicita al usuario seleccionar objetos en pantalla y retorna el SelectionSet."""
        print(prompt_message)
        try:
            # Eliminar selección previa si existe
            try:
                self.doc.SelectionSets.Item(selection_set_name).Delete()
            except:
                pass
            ss = self.doc.SelectionSets.Add(selection_set_name)
            ss.SelectOnScreen()
            print(f"📦 Seleccionados: {ss.Count} objetos.")
            return ss
        except Exception as e:
            print(f"❌ Error en selección: {e}")
            return None