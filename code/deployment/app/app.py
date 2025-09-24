import flet as ft
import requests
import os

API_URL = os.environ.get("API_URL", "http://localhost:8000/predict")

def main(page: ft.Page):
    page.title = "Lifeboat Predictor"
    page.window_width = 500
    page.window_height = 700
    page.bgcolor = ft.Colors.WHITE


    prediction_box = ft.Container(
        content=ft.Text(value="", size=20, color=ft.Colors.BLACK),
        border=ft.border.all(1, ft.Colors.BLACK),  # рамка
        border_radius=5,                           # скругление углов
        padding=10,                                # внутренний отступ
        alignment=ft.alignment.center,             # текст по центру
        width=400,                                 # ширина
        height=60                                  # высота
    )

    # Поля ввода
    pclass_input = ft.TextField(label="Pclass (1, 2, 3)", hint_text="Enter Pclass", keyboard_type=ft.KeyboardType.NUMBER)
    sex_input = ft.Dropdown(
        label="Sex",
        hint_text="Select Sex",
        options=[ft.dropdown.Option("male"), ft.dropdown.Option("female")]
    )
    age_input = ft.TextField(label="Age", hint_text="Enter Age", keyboard_type=ft.KeyboardType.NUMBER)
    fare_input = ft.TextField(label="Fare", hint_text="Enter Fare", keyboard_type=ft.KeyboardType.NUMBER)
    def predict_click(e):
        try:
            data = {
                "Pclass": int(pclass_input.value),
                "Sex": sex_input.value,
                "Age": float(age_input.value),
                "Fare": float(fare_input.value)
            }
            response = requests.post(API_URL, json=data)
            if response.status_code == 200:
                pred = response.json().get("prediction")
                prediction_box.content.value = f"Prediction: {'Survived' if pred==1 else 'Did not survive'}"
            else:
                prediction_box.content.value = f"API error: {response.status_code}"
        except Exception as ex:
            prediction_box.content.value  = f"Error: {ex}"
        page.update()

    predict_button = ft.ElevatedButton(
        text="Predict",
        on_click=predict_click,
        bgcolor=ft.Colors.BLACK,
        color=ft.Colors.WHITE,
        width=200,
        height=50
    )

    
    
    stack = ft.Stack(
        controls=[
            ft.Container(
                content=ft.Column([
                    pclass_input,
                    sex_input,
                    age_input,
                    fare_input,
                    ft.Container(height=20),
                    predict_button,
                    ft.Container(height=20),
                    prediction_box
                ], alignment=ft.MainAxisAlignment.CENTER),
                padding=40,
                width=400,
                height=700,
                bgcolor=ft.Colors.TRANSPARENT
            )
        ]
    )

    page.add(stack)

if __name__ == "__main__":
    ft.app(target=main, view=ft.WEB_BROWSER, port=8550, host="0.0.0.0")

