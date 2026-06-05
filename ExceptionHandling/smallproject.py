class MiniProject(Exception):
    pass

def chai(flavour, cups):
    menu = {
        "chai": 10,
        "mint": 20
    }

    try:
        if flavour not in menu:
            raise ValueError("Flavour is not present")

        if not isinstance(cups, int):
            raise TypeError("Cups must be an integer")

        total = menu[flavour] * cups

        print(f"{cups} cups of {flavour} chai = ₹{total}")

    except Exception as e:
        print("Error:", e)


chai("chai", 5)