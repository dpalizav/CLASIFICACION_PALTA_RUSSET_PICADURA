"""Ejecuta el EDA con el Python activo y conserva el notebook si hay un error."""
from pathlib import Path
import sys
import nbformat
from nbclient import NotebookClient
from jupyter_client import KernelManager


def main():
    ruta = Path(__file__).resolve().with_name("01_EDA.ipynb")
    notebook = nbformat.read(ruta, as_version=4)
    gestor = KernelManager(kernel_name="python3")
    # Usar el Python del entorno desde el que se ejecuta el script.
    gestor.kernel_spec.argv = [sys.executable, "-m", "ipykernel_launcher", "-f", "{connection_file}"]
    cliente = NotebookClient(notebook, km=gestor, timeout=1200,
                             resources={"metadata": {"path": str(ruta.parent)}})
    try:
        cliente.execute()
        nbformat.validate(notebook)
    except Exception:
        print("El EDA no terminó. Se conservó el notebook anterior con sus salidas.", file=sys.stderr)
        raise
    finally:
        if gestor.has_kernel:
            gestor.shutdown_kernel(now=True)

    # Guardar únicamente una ejecución completa y validada.
    nbformat.write(notebook, ruta)
    print("EDA completado: notebook actualizado y reportes en 7. resultados/eda.")


if __name__ == "__main__":
    main()
