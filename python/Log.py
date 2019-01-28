#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os


class Log:
    'Log util'

    # Log info
    @staticmethod
    def info(msg):
        print '\033[1;30;50m'
        print msg
        print '\033[0m'

    # Log error
    @staticmethod
    def error(msg):
        print '\033[1;31;50m'
        print msg
        print '\033[0m'
