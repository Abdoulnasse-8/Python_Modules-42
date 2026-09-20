import alchemy

print("=== Alembic 4 ===")
print("Accessing the alchemy module using 'import alchemy'")
print(f"Testing create_air: {alchemy.create_air()}")
print("Now show that not all functions can be reached")
print("This will raise an exception!")
try:
    earth = alchemy.create_earth()
    print("Testing create_earth:", earth)
except AttributeError:
    print("Error: Earth element not found in alchemy module")
