#!/usr/bin/env python

import os

class Q(object):

    def __init__(self, userid="x", state="y", guess="z"):
        self.userid = userid
        self.state = state
        self.guess = guess

    def unicode(self):
        print self.userid, self.state, self.guess


def setup():
    q1 = Q()
    q2 = Q("user1", "CA", "poppy")
    q3 = Q("user2", "TX", "bluebonnet")
    q4 = Q("user1", "TX", "cosmos")
    
    mylist = [q1, q2, q3, q4]
    
    for m in mylist:
        m.unicode()
    
    return mylist


