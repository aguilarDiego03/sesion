import flet as ft

def main(page: ft.Page):
    page.title = "Inicio de sesion"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    #page.bgcolor = ft.Colors.RED_
    
    usuario_valido ="admin@gamil.com"
    password_valido ="123"
    


    contraseña = ft.TextField(
        label="Contraseña",
        password=True,
        can_reveal_password=True,
        prefix_icon=ft.Icons.KEY,
        width=300
    )
    
    correo = ft.TextField(
        label="Correo electrónico",
        border_color=ft.Colors.BLUE,
        prefix_icon=ft.Icons.EMAIL,
        width=300
    )

    inicio = ft.ElevatedButton(
        "Iniciar sesion"
    )

    crear = ft.ElevatedButton(
        "Crear cuenta"
    )

    page.add(
        ft.Column(
            controls=[
                ft.Text("Inicio de sesion", size=20, weight=ft.FontWeight.BOLD),
                correo,
                contraseña,
                ft.Row([inicio, crear], alignment=ft.MainAxisAlignment.CENTER)
            ],
            spacing=15,
            horizontal_alignment = ft.CrossAxisAlignment.CENTER
        )
    )

def login(e):
    if correo.value == usuario_valido and contraseña.value == password_valido:
        mensaje.value="Inicio de sesion exitoso"
        mensaje.color="green"
    else:
        mensaje.value="Correo o contraseñas inorrectos"
        mensaje.color="red"
        

ft.app(target=main)