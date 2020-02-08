#!/usr/bin/env python3
# encoding: utf-8

"""
MIT License

Copyright (c) 2020 cellular-modem, Andreas Kuster

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

__author__ = "Andreas Kuster"
__copyright__ = "Copyright 2020, cellular-modem, Andreas Kuster"
__license__ = "MIT"

from cellular_modem.abstract_modem import AbstractModem
from cellular_modem.io.serial_handler import SerialHandler


class SIM800(AbstractModem, SerialHandler):

    def __init__(self, pin=None, **kwds):
        super().__init__(**kwds)
        self.pin = pin

    def send_sms(self):
        raise NotImplementedError()

    def receive_sms(self):
        print("sms received")

    def data_received(self, data):
        print("data received: {}".format(data))

    def connection_made(self):
        print("connection made")

    def connection_lost(self):
        print("connection closed")
