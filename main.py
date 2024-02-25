from get_accounts import print_accounts

# CLI Tools
import typer
from rich.prompt import Prompt
import os 
# Creation tools
from fx_sign_up import signup
from getmail import mail_and_verification


class Menu:
    def __init__(self):
        self.options = {
            1: 'Automatikus fiók és e-mail',
            2: 'Manuális e-mail és automatikus registráció',
            3: 'Fiókok és adatok',
            9: 'Kilépés'
        }
    def show_choices(self):
        for key, value in self.options.items():
            print(f'{key} {value}')
    
    def choose(self):
        self.show_choices()
        choice = int(Prompt.ask("Válassz opciót: "))
        match choice:
            case 1:
                mail_and_verification()
            case 2:
                email = Prompt.ask("Adja meg az e-mailt: ")
                signup(email)
            case 3:
                print_accounts()
            case 9:
                exit()
            case _ :
                os.system('cls')
                print('Adjon meg egy valid menü pontot\n')
                self.show_choices()
                choice = int(Prompt.ask("Válassz opciót: "))


menu = Menu()

def main():
    menu.choose()


    
if __name__ == "__main__":
    typer.run(main)
