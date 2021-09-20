import MySQLdb as mysql

from rich.console import Console
from rich.prompt import Prompt
from rich.text import Text


console = Console()

db = mysql.connect(host='localhost', user='root',
                   password='root', db="INFORMATION_SCHEMA")
cur = db.cursor()


def cp(string):
    console.print(Text(string, style='bold #00FF00'))


def rp(string):
    console.print(Text(string, style='bold red'))


def pp(string):
    console.print(Text(string, style='bold italic #FF00FF '))


# defining error handler decorator
def Error_Handler(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except:
            rp(f'exception flew by! , {func.__name__} use sudo instead ')
        else:
            cp('commands executed ....')
        finally:
            cp('execution over !!!!')
            cp('-'*30)
    return wrapper


@Error_Handler
def show_db_info(cur):
    cur.execute('SHOW DATABASES')
    res = cur.fetchall()
    pp(f'{[i for i in res]}')


@Error_Handler
def show_fields(cur):
    cur.execute('SHOW STATUS')
    res = cur.fetchall()
    r = dict(res)
    result = {key: r[key]
              for key in r.keys() & {'Uptime', 'Threads_created', 'Threads_connected', 'Threads_running', 'Queries', 'Max_used_connections'}}
    pp(f'{result}')


@Error_Handler
def show_process_lst(cur):
    cur.execute('USE information_schema')
    cur.execute('select * from PROCESSLIST')
    res = cur.fetchall()
    pp(f'{[i for i in res]}')


def menu():
    cp('[1]show database info')
    cp('[2]show multiple fields')
    cp('[3]show process lists ')
    rp('[4]exit')


while True:
    menu()
    ch = Prompt.ask('Enter choice : ', choices=[
        str(x) for x in range(1, 5)], default='1')

    if ch == '1':
        show_db_info(cur)

    elif ch == '2':
        show_fields(cur)

    elif ch == '3':
        show_process_lst(cur)
    elif ch == '4':
        break

cur.close()
