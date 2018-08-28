import os
from farmware_process import MyFarmware
from CeleryPy import log
import sys

if __name__ == "__main__":
    FARMWARE_NAME = "prueba_1_moverFB"
    log('los patitos dicen cuacua', message_type='info', title=FARMWARE_NAME)
    reload(sys)
    sys.setdefaultencoding('utf8')
    try:
        farmware = MyFarmware(FARMWARE_NAME)
    except Exception as e:
        log(e, message_type='error', title=FARMWARE_NAME + " : init")
        raise Exception(e)
    else:
        try:
            farmware.run()
        except Exception as e:
            log(e,message_type='error', title=FARMWARE_NAME + " : run")
raise Exception(e)