# Step 0. Load libraries and custom modules
from shiny import ui, render, App

# Step 1. Design interface
app_ui = ui.page_fluid(
    ui.input_slider('slider', 'choose', min=0, max=10, value=5),
    ui.output_text_verbatim('txt')
)

# Step 2. Design server logic
def server(input, output, session):
    @output
    @render.text
    def txt():
        return f'Double is {input.slider()*2}'

# Step 3. Create application
app = App(app_ui, server)