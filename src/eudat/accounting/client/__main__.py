# -*- coding: utf-8 -*-
"""
=======================
eudat.accounting.client
=======================

Command line handling
"""

import argparse
import logging
import sys

from eudat.accounting.client import __version__, LOG


def main(argv=sys.argv):
    """Main function called from console command
    """
    logging.basicConfig()
    exit_code = 1
    try:
        app = Application(argv)
        app.run()
        exit_code = 0
    except KeyboardInterrupt:
        exit_code = 0
    except Exception as exc:
        LOG.exception(exc)
    sys.exit(exit_code)


class Application(object):
    """The main Application class

    :param argv: The command line as a list as ``sys.argv``
    """
    def __init__(self, argv):
        ap = argparse.ArgumentParser()
        ap.add_argument('--version', action='version', version=__version__)
        ap.add_argument('value', help='The value to be recorded')
        ap.add_argument('unit', help='The unit of measurement for the value provided')
        ap.add_argument('-b', '--base_url', default='https://acct.eudat.eu',
                        help='base URL of the accounting server to use. '\
                        'Default: https://accnt.eudat.eu')

        ap.add_argument('-u', '--user', default='',
                        help='user id used for logging into the server. '\
                        'If not provided it is looked up in the environment variable '\
                        '"ACCOUNTING_USER". ' \
                        'Default: "" - aka not set')

        ap.add_argument('-p', '--password', default='',
                        help='password used for logging into the server. '\
                        'If not provided it is looked up in the environment variable '\
                        '"ACCOUNTING_PW". ' \
                        'Default: "" - aka not set')

        ap.add_argument('-d', '--domain', default='eudat',
                        help='name of the domain holding the account. '\
                        'Default: eudat')

        ap.add_argument('-a', '--account', default='',
                        help='account to be used. Typically the (P)ID of the '\
                        'resource to be accounted. '\
                        'Default: "" - not set - Should be a positional argument maybe?')

        ap.add_argument('-k', '--key', default='',
                        help='key used to refer to the record. '\
                        'If not set the accounting server will create the key. '\
                        'Default: "" - not set')

        ap.add_argument('-t', '--type', default='storage',
                        help='type of the resource accounted. '\
                        'Default: storage')

        ap.add_argument('-n', '--number', default='',
                        help='number of objects associated with this accounting record. '\
                        'This is EUDAT specific. '\
                        'Default: "" - not set')

        ap.add_argument('-m', '--measure_time', default='',
                        help='measurement time of the accounting record if different '\
                        'from the current time. '\
                        'Default: "" - not set')

        ap.add_argument('-v', '--verbose', action='store_true',
                        help='return the key of the accounting record created. '\
                        'Default: off')

        self.args = ap.parse_args(args=argv[1:])
        """Arguments of your app"""

    def run(self):
        # FIXME: Replace below sample with your code
        print("Hey! It works ;o)")


if __name__ == '__main__':
    main()
