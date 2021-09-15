import MySQLdb as mysql
from rich.prompt import Prompt
from rich import style
from rich.console import Console

import pprint
import time
import json

from rich import style
console = Console()
db = mysql.connect(host='localhost', user='root',
                   password='root', db="INFORMATION_SCHEMA")
cur = db.cursor()

cur.execute('SHOW STATUS')
res = cur.fetchall()

r = dict(res)
# pprint.pprint(r)
console.print(
    f"Uptime => {r['Uptime']}", style='bold  italic green')
console.print(
    f"Threads_created => {r['Threads_created']}", style='bold  italic green')
console.print(
    f"Threads_connected => {r['Threads_connected']}", style='bold  italic green')
console.print(
    f"Threads_running => {r['Threads_running']}", style='bold  italic green')
console.print(
    f"Queries => {r['Queries']}", style='bold  italic green')
console.print(
    f"Max_used_connections => {r['Max_used_connections']}", style='bold  italic green')


cur.close()
