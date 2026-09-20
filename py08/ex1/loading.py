import sys
import importlib


REQUIRED_MODULES = ["pandas", "numpy", "matplotlib"]
OPTIONAL_MODULES = ["requests"]


def check_module(name: str):
    try:
        module = importlib.import_module(name)
        version = getattr(module, "__version__", "unknown")
        print(f"[OK] {name} ({version}) - ready")
        return module
    except ImportError:
        print(f"[MISSING] {name} - not installed")
        return None


def check_dependencies():
    print("LOADING STATUS: Loading programs...")
    print("Checking dependencies:")

    modules = {}

    for mod in REQUIRED_MODULES:
        modules[mod] = check_module(mod)

    for mod in OPTIONAL_MODULES:
        module = check_module(mod)
        if module:
            modules[mod] = module

    return modules


def show_install_instructions():
    print("\nTo install dependencies:")

    print("\nUsing pip:")
    print("pip install -r requirements.txt")

    print("\nUsing Poetry:")
    print("poetry install")


def analyze_data(modules):
    numpy = modules["numpy"]
    pandas = modules["pandas"]
    matplotlib = modules["matplotlib"]

    print("\nAnalyzing Matrix data...")

    data = numpy.random.rand(1000)

    df = pandas.DataFrame({
        "values": data
    })

    print(f"Processing {len(df)} data points...")

    print("Generating visualization...")

    matplotlib.pyplot.hist(df["values"], bins=30)
    matplotlib.pyplot.title("Matrix Data Distribution")
    matplotlib.pyplot.savefig("matrix_analysis.png")

    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


def main():
    modules = check_dependencies()

    if any(modules.get(m) is None for m in REQUIRED_MODULES):
        print("\nERROR: Missing required dependencies.")
        show_install_instructions()
        sys.exit(1)

    analyze_data(modules)


if __name__ == "__main__":
    main()
