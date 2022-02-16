from argparse import ArgumentParser, Namespace

from .client import FruitPalClient
from .util import default_to_env


def build_parser() -> ArgumentParser:
    parser = ArgumentParser()
    parser.add_argument('--base-url', action=default_to_env('FRUITPAL_BASE_URL'))

    actions = ['import-vendors', 'estimate']
    subparsers = parser.add_subparsers(dest='action')
    subparsers.required = True

    action_parsers = {action: subparsers.add_parser(action) for action in actions}
    action_parsers['import-vendors'].add_argument('path')
    action_parsers['estimate'].add_argument('commodity')
    action_parsers['estimate'].add_argument('unit_price')
    action_parsers['estimate'].add_argument('volume')
    return parser


def main():
    parser: ArgumentParser = build_parser()
    args: Namespace = parser.parse_args()
    client = FruitPalClient(base_url=args.base_url)

    if args.action == 'import-vendors':
        client.import_vendors(args.path)

    elif args.action == 'estimate':
        client.estimate(args.commodity, args.unit_price, args.volume)
