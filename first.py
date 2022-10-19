from shiny import ui, render, App

app_ui = ui.page_fluid(
    ui.input_slider('slider', min=0, max=10, value=5),
    ui.output_text_verbatim('txt')
)

def server(input, output, session):
    @output
    @render.text
    def txt():
        return f'Double is {input.slider()*2}'

app = App(app_ui, server)
