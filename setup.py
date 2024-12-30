from cx_Freeze import setup, Executable

setup(
    name = "NomeDoSeuPrograma",
    version = "1.0",
    description = "Descrição do seu programa",
    executables = [Executable("limpadorDeArquivosTemporarios.py")]
)
