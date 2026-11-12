"""Silent Auction

Each bidder enters a name and a bid. As soon as the bid is placed, the screen
is cleared so the next bidder cannot see it. The highest bid wins.
A bid must be at least the starting price.
"""

import os


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def read_number(prompt, minimum=None):
    """Keep asking until a valid number (>= minimum, if given) is entered."""
    while True:
        raw = input(prompt).strip()
        try:
            value = float(raw)
        except ValueError:
            print("Please enter a valid number.")
            continue
        if value <= 0:
            print("The amount must be greater than 0.")
            continue
        if minimum is not None and value < minimum:
            print(f"Your bid must be at least the starting price ({minimum:g}).")
            continue
        return value


def main():
    bids = {}  # name -> amount

    clear_screen()
    print("=== SILENT AUCTION ===\n")
    item = input("What is being auctioned? ").strip() or "Mystery Item"
    starting_price = read_number("Starting price: ")

    while True:
        clear_screen()
        print(f"=== SILENT AUCTION: {item} ===")
        print(f"Starting price: {starting_price:g}\n")

        name = input("Your name: ").strip()
        if not name:
            print("Name cannot be empty.")
            input("Press Enter to continue...")
            continue

        if name.lower() in (n.lower() for n in bids):
            print("This name has already placed a bid. Please use a different name.")
            input("Press Enter to continue...")
            continue

        amount = read_number("Your bid: ", minimum=starting_price)
        bids[name] = amount

        # Clear the screen right after the bid is placed
        clear_screen()
        print("Your bid has been recorded. Thank you!\n")
        input("Press Enter to hand over to the next bidder...")
        clear_screen()

        while True:
            more = input("Is there another bidder? (y/n): ").strip().lower()
            if more in ("y", "n"):
                break
            print("Please enter y or n.")
        if more == "n":
            break

    clear_screen()
    print(f"=== AUCTION RESULT: {item} ===\n")

    if not bids:
        print("No bids were placed. The auction is cancelled.")
        return

    highest = max(bids.values())
    winners = [n for n, a in bids.items() if a == highest]

    print(f"Total bidders: {len(bids)}")

    if len(winners) == 1:
        print(f"\nWinner: {winners[0]}")
        print(f"Winning bid: {highest:g}")
    else:
        print(f"\nIt's a tie! These bidders all bid the highest amount ({highest:g}):")
        for w in winners:
            print(f"  - {w}")


if __name__ == "__main__":
    main()