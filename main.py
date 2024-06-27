import pathlib

import playsound
import requests
import typer

app = typer.Typer()


@app.command()
def main(url: str):
    resp = requests.get(url)
    sound = pathlib.Path("audio.mp3")
    sound.write_bytes(resp.content)

    playsound.playsound(sound)


if __name__ == "__main__":
    app()
