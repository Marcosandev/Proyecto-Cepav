import flet as ft

# Pila global para almacenar el historial de controles de la página
_history_stack = []

def navigate(page: ft.Page, view_class, *args, **kwargs):
   
    if page.controls:
        _history_stack.append(list(page.controls))
    
    page.clean()
    
    # Instanciar la nueva vista
  
    view = view_class(page, *args, **kwargs)
    
    # Insertamos la vista principal al principio para que quede detrás de elementos flotantes (como Navbar)

    page.controls.insert(0, view)
    page.update()

def go_back(page: ft.Page):
    """
    Función para el botón de retroceso: restaura la vista anterior.
    """
    if _history_stack:
        previous_controls = _history_stack.pop()
        page.clean()
        page.controls.extend(previous_controls)
        page.update()
    else:
        print("No hay historial para volver atrás.")
