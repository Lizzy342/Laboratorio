"""Ejecuta las pruebas y el reporte de cobertura con un solo comando:  python run.py"""
import subprocess
import sys

PY = sys.executable


def run(*args):
    return subprocess.run([PY, *args]).returncode


try:
    import coverage  # noqa: F401
except ImportError:
    print("Instalando coverage...")
    run("-m", "pip", "install", "-q", "coverage")

print("\n=== REPORTE DE EJECUCION DE PRUEBAS ===\n")
codigo = run("-m", "unittest", "discover", "-s", "tests", "-v")

print("\n=== REPORTE DE COBERTURA DE CODIGO ===\n")
run("-m", "coverage", "run", "--branch", "--source=src",
    "-m", "unittest", "discover", "-s", "tests")
run("-m", "coverage", "report", "-m")

sys.exit(codigo)
