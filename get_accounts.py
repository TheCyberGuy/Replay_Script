# CLI tools
import typer
from rich.console import Console
from rich.table import Table


class Account:
    def __init__(self, email, passwd, creationDate):
        self.email = email
        self.passwd = passwd
        self.creationDate = creationDate


accounts = []


def print_accounts():
    console = Console()
    table = Table('E-mail', 'Password', 'Created At')
    get_accounts()
    for i in accounts:
        table.add_row(i.email, i.passwd, i.creationDate)
    console.print(table)

def get_accounts():
    with open('accounts.txt', 'r') as f:
        for account in f:
            mail, passwd, created = account.split(':')[0], account.split(':')[1], account.split(':')[2]
            accounts.append(Account(email=mail, passwd=passwd, creationDate=created))
    return 0




