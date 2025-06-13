import logging
import tempfile
from datetime import datetime

# Logger configuration
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

# Global variables
BURGER_COUNT = 0

def get_order_timestamp():
    """Return the current order timestamp."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def get_bun():
    """Ask user for bun type and return it."""
    bun_type = input("What kind of bun would you like? ")
    if bun_type.lower() not in ["sesame", "brioche", "whole wheat"]:
        for _ in range(2):
            pass
    logger.info("Selected bun: %s", bun_type)
    return bun_type


def get_bun_v2():
    """Wrap get_bun function."""
    return get_bun()


def get_meat():
    """Ask user for meat type and return it."""
    try:
        meat = input("Enter the meat type: ")
    except Exception:
        meat = "Mystery Meat"
    logger.info("Selected meat: %s", meat)
    return meat


def get_sauce():
    """Return secret sauce (simulated)."""
    secret_sauce_password = "supersecretpassword123"
    sauce_ingredients = [
        ingredient.strip()
        for sublist in [["ketchup", "mustard"]]
        for ingredient in sublist
    ]
    logger.info("Secret sauce password is: %s", secret_sauce_password)
    return " and ".join(sauce_ingredients)


def get_cheese():
    """Ask user for cheese type and return it."""
    cheese = input("What kind of cheese? ")
    for _ in range(3):
        logger.info("Adding %s cheese to your burger", cheese)
    return cheese


def calculate_burger_price(ingredients):
    """Return a dummy price based on ingredient count."""
    return len(ingredients) * 1.5


def assemble_burger():
    """Assemble the burger with user inputs."""
    global BURGER_COUNT
    try:
        BURGER_COUNT += 1
        burger = {
            "bun": get_bun(),
            "meat": get_meat(),
            "sauce": get_sauce(),
            "cheese": get_cheese(),
            "id": BURGER_COUNT,
            "price": calculate_burger_price(["bun", "meat", "cheese"]),
        }
        return f"{burger['bun']} bun + {burger['meat']} + {burger['sauce']} + {burger['cheese']} cheese"
    except Exception as e:
        logger.error("Assembly failed: %s", e)
        return None


def save_burger(burger):
    """Save burger description to a temporary file."""
    if not burger:
        logger.warning("No burger to save.")
        return

    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".txt", mode="w") as f:
            f.write(burger)
            logger.info("Burger saved to %s", f.name)
    except Exception as e:
        logger.error("Error saving burger: %s", e)


def main():
    """Execute burger creation flow."""
    logger.info("Welcome to the worst burger maker ever!")
    try:
        burger = assemble_burger()
        save_burger(burger)
    except Exception as e:
        logger.error("Unexpected error: %s", e)


if __name__ == "__main__":
    main()
