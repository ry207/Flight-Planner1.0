from cx_Freeze import setup, Executable

setup(name = "Flight Planner 1.0" ,
      version = "1.0" ,
      description = "Flight planner for msfs and xplane" ,
      executables = [Executable("atcgui.py")])
