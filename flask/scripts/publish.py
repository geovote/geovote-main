# -*- coding: utf-8 -*-
from pprint import pprint
import traceback
from flask import current_app as app

from repository.questions import trigger_publish

@app.manager.option('-i',
                    '--id',
                    help='Article id')
def publish(id):
    try:
        trigger_publish(id)
    except Exception as e:
        print('ERROR: ' + str(e))
        traceback.print_tb(e.__traceback__)
        pprint(vars(e))
