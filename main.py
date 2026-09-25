import client # Sets up a new agent.

def main() -> None:

    running: bool = True
    run_auto: str = input(f'Do you want to run the autoclient? (Y/N)')
    if run_auto.lower() == 'y':
        y: AutoClient = AutoClient()
    x: Client = Client()
    while running:
        to_do: str = input(f'What do you want to do? (A)ction or (R)un AutoClient or (C)hange Settings or (V)iew Status or Check (S)hip Status?\n')
        if to_do.lower() == 'a':
            x.action()
        elif to_do.lower() == 'r':
            y: AutoClient = AutoClient()
        elif to_do.lower() == 'c':
            x.change_settings()
        elif to_do.lower() == 'v':
            x.view_settings()
        elif to_do.lower() == 's':
            x.ship_status()
        else:
            continue


if __name__ == '__main__':
    main()