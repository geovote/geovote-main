# -*- coding: utf-8 -*-
from pprint import pprint
import traceback
from flask import current_app as app

from repository.questions import trigger_vote

@app.manager.option('-i',
                    '--id',
                    help='Article id')
def vote(id):
    try:
        trigger_vote(int(id))
    except Exception as e:
        print('ERROR: ' + str(e))
        traceback.print_tb(e.__traceback__)
        pprint(vars(e))
