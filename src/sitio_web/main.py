from nicegui import ui

@ui.page('/')
def pagina_principal():
    ui.label('Welcome').classes('text-2xl font-bold')
    ui.markdown('Contador')
    
    contador = {'valor': 0}
    etiqueta = ui.label(f'Contador: {contador["valor"]}')
    
    def incrementar():
        contador['valor'] += 1
        etiqueta.text = f'Contador: {contador["valor"]}'
        ui.notify('¡Sumaste 1!')
    
    ui.button('Contar', on_click=incrementar, color='blue')

# Configuración para producción
ui.run(
    host='0.0.0.0',
    port=8080,
    reload=False
)
