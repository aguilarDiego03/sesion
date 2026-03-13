import flet as ft

def main(page: ft.Page):
    page.title = "Inicio de sesion"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    usuario_valido = "admin@gmail.com"
    password_valido = "123"

    mensaje = ft.Text()

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

    def login(e):

        if correo.value == "" or contraseña.value == "":
            mensaje.value = "Error: Debes llenar todos los campos"
            mensaje.color = "red"
            page.update()
            return

        if "@" not in correo.value or "." not in correo.value:
            mensaje.value = "Error: Ingresa un correo válido"
            mensaje.color = "red"
            page.update()
            return

        if correo.value == usuario_valido and contraseña.value == password_valido:
            page.clean()

            page.add(
                ft.Column(
                    [
                        ft.Text("Felicidades, has iniciado sesión", size=30, weight=ft.FontWeight.BOLD),
                        ft.Text("Bienvenido al sistema")
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                )
            )
        else:
            mensaje.value = "Correo o contraseña incorrectos"
            mensaje.color = "red"
            page.update()

    inicio = ft.ElevatedButton(
        "Iniciar sesion",
        on_click=login
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
                ft.Row([inicio, crear], alignment=ft.MainAxisAlignment.CENTER),
                mensaje
            ],
            spacing=15,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )

ft.app(target=main)
