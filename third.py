from shiny import ui, render, App
import pandas as pd

app_ui = ui.page_fluid(
    ui.output_text('text1'),
    ui.output_ui('ui1'),
    ui.output_table('table1')
)

def server(input, output, session):
    @output
    @render.text
    def text1():
        return f'Hello and goodbye'
    
    @output
    @render.ui
    def ui1():
        return ui.HTML("<p>And they say it's easy")
    
    @output
    @render.table
    def table1():
        df = pd.DataFrame({'id':['A','B','C'], 'value':[2,4,6]})
        return df

app = App(app_ui,server)
