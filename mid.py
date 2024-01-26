def garmit_info():
    hp_g = 100
    attack_g = 5
    turn = 0

    while True:
        turn += 1
        print(f"Turn {turn}")

        hp_g -= attack_g

        print(f"HP: {hp_g}, Attack: {attack_g}")

        if hp_g <= 0:
            print("Game Over - Garmit defeated!")
            break

        input("Press Enter to continue to the next turn.")

garmit_info()