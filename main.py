
from pyscript import display, document

# Dictionary containing non-metal elements
non_metals = {
    # Symbol: (Element Name, Atomic Number, Atomic Mass)
    'H': ('Hydrogen', 1, 1.008),
    'He': ('Helium', 2, 4.0026),
    'C': ('Carbon', 6, 12.011),
    'N': ('Nitrogen', 7, 14.007),
    'O': ('Oxygen', 8, 15.999),
    'F': ('Fluorine', 9, 18.998),
    'Ne': ('Neon', 10, 20.180),
    'P': ('Phosphorus', 15, 30.974),
    'S': ('Sulfur', 16, 32.06),
    'Cl': ('Chlorine', 17, 35.45),
    'Ar': ('Argon', 18, 39.948),
    'Se': ('Selenium', 34, 78.971),
    'Br': ('Bromine', 35, 79.904),
    'Kr': ('Krypton', 36, 83.798),
    'I': ('Iodine', 53, 126.90),
    'Xe': ('Xenon', 54, 131.29),
    'Rn': ('Radon', 86, 222),
}


# Function to search for element information
def get_element_info(e):

    # Get the entered element symbol
    element1 = document.getElementById("element-input").value.strip().title()

    # Retrieve element information using .get()
    element, atomic_number, atomic_mass = non_metals.get(
        element1,
        ("Element not found", "-", "-")
    )

    # Display the result
    if element == "Element not found":
        document.getElementById("result").innerHTML = (
            "Element does not exist in the non-metals list."
        )

    else:
        document.getElementById("result").innerHTML = f"""
        <b>Element Symbol:</b> {element1}<br>
        <b>Element Name:</b> {element}<br>
        <b>Atomic Number:</b> {atomic_number}<br>
        <b>Atomic Mass:</b> {atomic_mass}<br>
        """
