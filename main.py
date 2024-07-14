import flet as ft
import youtube as module


def main(page: ft.Page):
    page.add(ft.Text(value="Video Downloader"))
    tb1 = ft.TextField(label="Youtube URL", bgcolor="green")
    page.add(tb1)
    button = ft.FilledButton(text='Start', on_click=lambda event: onchange(tb1.value,page))
    page.add(button)
    
    

def onclick(event):
    print(f'Descargando el video desde: {event}')
    module.downloader(event)
    
def onchange(event,page:ft.Page):
    print('test')
    module.getname(event,page)
    module.getresolutions(event,page)

def setpage(page:ft.Page):
    page.add(ft.Text(value="Video Downloader"))
    tb1 = ft.TextField(label="Youtube URL", bgcolor="green",on_change=lambda event: onchange(tb1.value,page))
    page.add(tb1)

def clearpage(page:ft.Page):
    page.clean()
    



ft.app(target=main)


