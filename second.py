from shiny import ui, render, App

app_ui = ui.page_fluid(
    ui.input_text(id='text1',label='Insert first value',value='3'),
    ui.input_text(id='text2',label='Insert second value',value='4'),
    ui.output_text_verbatim('txt')
)

def server(input, output, session):
    @output
    @render.text
    def txt():
        if input.text1() == '' or input.text2() == '':
            result = ''
        else:
            result = int(input.text1()) * int(input.text2())
        return f'Multiplied values are equal to: {result}'

app = App(app_ui, server)