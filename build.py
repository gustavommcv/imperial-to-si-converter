import PyInstaller.__main__
import platform
import sys


def build():
    try:
        print("Iniciando empacotamento. Isso pode levar alguns minutos...")

        # O separador de ambiente para adicionar dados no PyInstaller difere por SO
        sep = ";" if platform.system() == "Windows" else ":"

        PyInstaller.__main__.run(
            [
                "main.py",
                "--name=imperial-to-si-converter",
                "--onefile",  # Gera apenas um único arquivo .exe
                "--console",  # Necessário para TUI de terminal como o Textual
                f"--add-data=ui/styles.tcss{sep}ui",  # Trazendo os estilos CSS
                "--clean",  # Limpa builds anteriores
                "--noconfirm",  # Substitui output sem perguntar
                "--log-level=WARN",  # Reduz verbosidade
            ]
        )

        print("\nSucesso! O executável foi gerado na pasta 'dist/'.")
    except Exception as e:
        print(f"Erro ao gerar o executável: {e}")
        sys.exit(1)


if __name__ == "__main__":
    build()
