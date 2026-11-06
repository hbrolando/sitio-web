from nicegui import ui
import os  # Para leer variables del entorno

@ui.page('/')
def pagina_principal():
    ui.label('¡Welcome').classes('text-2xl font-bold')
    ui.markdown('Contador')
    
    contador = {'valor': 0}
    etiqueta = ui.label(f'Contador: {contador["valor"]}')
    
    def incrementar():
        contador['valor'] += 1
        etiqueta.text = f'Contador: {contador["valor"]}'
        ui.notify('¡Sumaste 1!')
    
    ui.button('Haz clic aquí', on_click=incrementar, color='blue')

# Puerto automático: 8080 en local, el que asigne Render en la nube
puerto = int(os.getenv('PORT', 8080))

ui.run(
    host='0.0.0.0',
    port=puerto,
    reload=True
)
