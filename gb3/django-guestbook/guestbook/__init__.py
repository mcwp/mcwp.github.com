from guestbook.models import State
import logging

state_names = [
    'California',
    'Oregon',
    'Nevada',
    'Utah',
    'Arizona',
    ]

#logging.info('State names %s', type(state_names))

for n in state_names:
    logging.info('try state %s', n)
#    x = State(n)
    x = State.objects.create(name=n)
#    x.save()

logging.info('x is %s', str(x))
logging.info(dir(x))
logging.info('x name is %s', str(x.name))
