Script cliente:
from pyModbusTCP.client import ModbusClient
from time import sleep
SERVER_HOST="192.168.0.12"
SERVER_PORT=502
c=ModbusClient(host=SERVER_HOST,port=SERVER_PORT,auto_open=True)
c.open()
while True:
    if c.is_open():
        regs=c.read_input_registers(reg_addr=10,reg_nb=1)
        print(regs)
        sleep(3)
    else:
        print("can't connect")
        sleep(3)
Script servidor:
from pyModbusTCP.server import ModbusServer , DataBank
DataBank.set_words(address=10,word_list=[15])
server=ModbusServer(host="192.168.0.12",port=502,no_block=True)
server.start()
while True:
    pass
