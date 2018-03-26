# Create users for the ecommerce portion of the tutorial
# Ecommerce users engage in 1 or more sessions where they explore a site like Amazon or Ebay then
# potentially add items to a shopping cart, checkout, and complete a purchase.

from uuid import uuid4
from datetime import datetime, timedelta
from scipy.stats import norm, nbinom, beta, randint, uniform

local_epoch = datetime(2017, 1, 1)
sessions_zero_inflation = 0.3


def fuzz_time(dt):
    return dt + timedelta(days=randint.rvs(0, 365)) + timedelta(hours=norm.rvs(12, 4))


class User(object):

    def __init__(self):
        # total sessions this user will have:
        self.num_sessions = 1 + int(uniform.rvs() > sessions_zero_inflation) * nbinom.rvs(4, beta.rvs(12, 10))
        self.first_session = fuzz_time(local_epoch)

        self.session_starts = [fuzz_time(self.first_session) for i in range(self.num_sessions - 1)] + [self.first_session]

        self.next_session = self.first_session
        self.guid = uuid4()

        self._current_cart = 0  # num items currently in cart


    def __str__(self):
        return "{0}: {1}".format(self.guid, self.first_session)

    def augment_event(self, event, session_id):
        event['user'] = self.guid
        event['id'] = uuid4()
        event['session_id'] = session_id
        return event

    def session(self):
        """Emit data for a single session"""
        events = []
        sid = uuid4()
        self._current_cart = 0
        rolling_time = self.next_session
        state = 'land_homepage' if uniform.rvs() < .7 else 'land_item'
        event = {'timestamp': rolling_time, 'event': state}
        events.append(self.augment_event(event, sid))

        while 1:
            state, rolling_time = self.update_state(state, rolling_time)
            if not state:
                break
            event = {'timestamp': rolling_time, 'event': state}
            events.append(self.augment_event(event, sid))

        self.next_session = rolling_time
        return events

    def update_state(self, state, rolling_time):
        # land, land_item, add_to_cart, enter_checkout, enter_address, enter_ccard, complete
        r = uniform.rvs()
        new_state = ''
        if state == 'land_homepage':
            if r < .8:
                new_state = 'land_item'
                rolling_time += timedelta(minutes=1 + nbinom.rvs(1, .5))
        elif state == 'land_item':
            if r < .3:
                new_state = 'land_item'
                rolling_time += timedelta(minutes=1 + nbinom.rvs(2, .5))
            elif r < .7:
                new_state = 'add_to_cart'
                rolling_time += timedelta(minutes=1 + nbinom.rvs(2, .5))
            elif self._current_cart > 0 and r < .8:
                new_state = 'enter_checkout'
                rolling_time += timedelta(minutes=1 + nbinom.rvs(4, .5))
        elif state == 'add_to_cart':
            if r < .6:
                new_state = 'enter_checkout'
                rolling_time += timedelta(minutes=1 + nbinom.rvs(1, .5))
            elif r < .9:
                new_state = 'land_item'
                rolling_time += timedelta(minutes=1 + nbinom.rvs(4, .5))
        elif state == 'enter_checkout':
            if r < .98:
                new_state = 'enter_address'
                rolling_time += timedelta(minutes=1 + nbinom.rvs(1, .8))
        elif state == 'enter_address':
            if r < .97:
                new_state = "enter_ccard"
                rolling_time += timedelta(minutes=1 + nbinom.rvs(1, .9))
        elif state == 'enter_ccard':
            if r < .9:
                new_state = 'complete'
                rolling_time += timedelta(minutes=1 + nbinom.rvs(1, .8))
        return new_state, rolling_time

    def create_data(self):
        """ Create data until out of sessions """
        all_events = []
        for i in range(self.num_sessions):
            self.next_session = self.session_starts[i]
            all_events.extend(self.session())
        return all_events



if __name__ == '__main__':
    user = User()
    print(user)
    events = user.create_data()
    for e in events:
        print(e)
