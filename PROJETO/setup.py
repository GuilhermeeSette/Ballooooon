import cx_Freeze

executables = [cx_Freeze.Executable("aula_13.py")]


cx_Freeze.setup(
    name = "A bit Racey",
    options = {"build_exe": {"packages": ["pygame"],
                            "include_files": ["E:\Pygame_course/carrace.png"]}},

    executables = executables
    )

