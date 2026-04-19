import argparse

def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('--encrypt', action='store_true')
    parser.add_argument('--decrypt', action='store_true')
    parser.add_argument('--path', type=str)
    parser.add_argument('--delete', action='store_true')
    parser.add_argument('--password', type=str)

    return parser.parse_args()