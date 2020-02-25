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

import serial
import threading
import time


class SerialHandler:

    def __init__(self, **kwds):
        # init internal parameters
        self.lock = threading.Lock()
        self.serial: serial.Serial = None
        self.polling_interval = 0.01
        self.polling_enabled = False
        self.polling_thread_die = False
        # create background polling thread
        self.polling_thread = threading.Thread(target=self.poll)
        self.polling_thread.start()

    def open(self, port, baudrate):
        # acquire serial lock
        with self.lock:
            # open the serial connection
            self.serial = serial.Serial(port=port,
                                        baudrate=baudrate,
                                        bytesize=serial.EIGHTBITS,
                                        parity=serial.PARITY_NONE,
                                        stopbits=serial.STOPBITS_ONE,
                                        timeout=None,  # blocking
                                        xonxoff=False,
                                        rtscts=False,
                                        write_timeout=None,  # blocking
                                        inter_byte_timeout=None,
                                        exclusive=None)
        # call connection_made event
        self.connection_made()
        # enable polling
        self.polling_enabled = True

    def close(self):
        # indicate polling thread to exit
        self.polling_thread_die = True
        # wait for thread to exit
        self.polling_thread.join()
        # acquire serial lock
        with self.lock:
            # close connection
            self.serial.close()
        # call connection_lost event
        self.connection_lost()

    def poll(self):
        # check for new data
        while not self.polling_thread_die:
            # check if polling is enabled
            if self.polling_enabled:
                # acquire lock
                with self.lock:
                    # check if data is available
                    if self.serial.in_waiting > 0:
                        # read all available data and call data_received event
                        self.data_received(data=self.serial.read(self.serial.in_waiting))
            # sleep for polling_interval seconds
            time.sleep(self.polling_interval)

    @staticmethod
    def to_bytes(data):
        # check data type
        if type(data) == bytes:
            # nothing to do
            return data
        elif type(data) == str:
            # encode string using utf-8
            return data.encode("utf-8")

    def write(self, data, blocking=True):
        # acquire serial lock
        with self.lock:
            self.serial.write(SerialHandler.to_bytes(data))
            if blocking:
                while self.serial.out_waiting > 0:
                    time.sleep(self.polling_interval)

    def read(self, blocking=True):
        # acquire lock
        with self.lock:
            if blocking:
                # block till data ending with newline is available
                return self.serial.readline()
            else:
                # read all available data
                return self.serial.read(self.serial.in_waiting)

    def write_read_atomic_blocking(self, data, no_lines=1):
        # acquire serial lock
        with self.lock:
            # write data
            self.serial.write(SerialHandler.to_bytes(data))
            # wait for response
            if no_lines > 1:
                response = list()
                for i in range(no_lines):
                    response.append(self.serial.readline())
                return response
            elif no_lines == 1:
                return self.serial.readline()
            else:
                raise RuntimeError("Unable to read {} lines".format(no_lines))

    def data_received(self, data):
        print("data reveiced event: {}".format(data))

    def connection_made(self):
        print("connection made event")

    def connection_lost(self):
        print("connection lost event")


if __name__ == "__main__":
    # instantiate handler
    handler = SerialHandler()
    # open the serial port
    handler.open("/dev/ttyUSB0", 19200)
    # ping modem: AT -> AT OK
    print(handler.write_read_atomic_blocking("AT\n", no_lines=2))
    # let the connection open for another 60 seconds.
    time.sleep(10)
    # close serial
    handler.close()

    """
    # instantiate handler
    handler = SerialHandler()
    # open the serial port
    handler.open("/dev/pts/2", 9600)  # loopback device
    if handler.write_read_atomic_blocking("Hello World!\n") == handler.to_bytes("Hello World!\n"):
        print("Successful!")
    # let the connection open for another 60 seconds.
    time.sleep(60)
    # close serial
    handler.close()
    """

"""
    Todo:
        add timeout to blocking calls
        catch all sort of exceptions
        add testing
        add function description
        add verbose level system
"""