"""curses interface for bite"""

from snakeoil.cli.arghparse import ArgumentParser

from ..tui import Client


argparser = ArgumentParser(
    color=False, quiet=False, verbose=False,
    description=__doc__, script=(__file__, __name__))

config_opts = argparser.add_argument_group('Config options')
config_opts.add_argument(
    '-c', '--connection',
    help='use a configured connection')
config_opts.add_argument(
    '--config-file',
    help='read an alternate configuration file')

service_opts = argparser.add_argument_group('Service options')
service_opts.add_argument(
    '-b', '--base',
    help='base URL of service')
service_opts.add_argument(
    '-s', '--service',
    help='service type')

connect_opts = argparser.add_argument_group('Connection options')
connect_opts.add_argument(
    '-k', '--insecure', action='store_false', dest='verify',
    help='skip SSL certificate verification')
connect_opts.add_argument(
    '-C', '--concurrent', type=int,
    help='maximum number of allowed concurrent requests to a service')
connect_opts.add_argument(
    '--timeout', type=int, metavar='SECONDS',
    help='amount of time to wait before timing out requests (defaults to 30 seconds)')


@argparser.bind_main_func
def main(options, out, err):
    client = Client(**vars(options))
    client.run()
