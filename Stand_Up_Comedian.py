import flet as ft
import flet_audio as fta
import random

jokes = {1: "Why don't skeletons fight each other? They don't have the guts.",
        2: "Why did the scarecrow win an award? Because he was outstanding in his field!",
        3: "What do you call a fake noodle? An impasta!",
        4: "How do you organize a space party? You planet!",
        5: "Why did the math book look sad? Because it had too many problems.",
        6: "What's brown and sticky? A stick.",
        7: "Why can't you explain puns to kleptomaniacs? They always take things literally.",
        8: "I told my wife she was drawing her eyebrows too high. She looked surprised.",
        9: "What's the best thing about Switzerland? I don't know, but the flag is a big plus.",
        10: "How do you make a tissue dance? Put a little boogie in it!",
        11: "Why don't eggs tell jokes? They'd crack each other up.",
        12: "What do you call a bear with no teeth? A gummy bear!",
        13: "Did you hear about the claustrophobic astronaut? He just needed a little space.",
        14: "Why don't scientists trust atoms? Because they make up everything!",
        15: "What did one wall say to the other wall? I'll meet you at the corner!",
        16: "Why did the bicycle fall over? Because it was two-tired!",
        17: "What do you call cheese that isn't yours? Nacho cheese!",
        18: "Why couldn't the leopard play hide and seek? Because he was always spotted.",
        19: "What did the grape say when it got stepped on? Nothing, it just let out a little wine.",
        20: "I'm reading a book about anti-gravity. It's impossible to put down!"
    }

def main(page: ft.Page):
    def random_choice(e):
        selected_joke = random.choice(jokes)
        joke.value = selected_joke
        audio.play()
        page.update()

    def dismissal(e):
        audio.seek(0)
        audio.pause()

    audio = fta.Audio(src="Risa.mp3")
    page.overlay.append(audio)
    page.horizontal_alignment="center"
    titulo = ft.Text("Jokes generator😂🤣", size= 50)
    boton = ft.FilledButton(text="Give me a joke", width=150, height=45, on_click=lambda _: page.open(bs))
    joke = ft.Text(random.choice(jokes))
    bs = ft.BottomSheet(on_dismiss=dismissal,
            content=ft.Container(
                padding=50,
                content=ft.Column(
                    tight=True,
                    controls=[
                        ft.Container(width=600, content=ft.Column(controls=[joke,
                        ft.ElevatedButton("Another joke?",on_click=random_choice),])),
                        
                    ],
                ),
            ),
        )     
        
    page.add(titulo,boton)

ft.app(target=main)