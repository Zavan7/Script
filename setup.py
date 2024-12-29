from cx_Freeze import setup, Executable

# Substitua 'meu_script.py' pelo nome do seu arquivo Python
executables = [Executable("script.py")]

setup(
    name="MeuPrograma",
    version="1.0.1",
    description="Meu script para BF, facilitando tarefas do dia a dia",
    executables=executables,
)