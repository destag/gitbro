#!/usr/bin/env python3

"""Module for aggregating git repos."""

import sys
import logging
import argparse
import glob
import pathlib
import subprocess
import re


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        '-p', '--pathname',
        dest='pathname',
        default='.',
        help='Pathnema',
    )
    parser.add_argument(
        '-f', '--fetch',
        dest='fetch',
        action='store_true',
        help='flag',
    )
    args = parser.parse_args()

    for repo_path in pathlib.Path(args.pathname).glob('**/.git'):
        git_repo = repo_path.absolute()
        print(git_repo.parts[-2])
        r = subprocess.run(['git', '--git-dir={repo}'.format(repo=git_repo), 'status', '-sb'], stdout=subprocess.PIPE).stdout.decode('utf-8')
        stat_line = r.split('\n')[0]
        match = re.match(r'## (?P<localbranch>[\w\/]*)...(?P<remotebranch>\w*)', stat_line)
        print(match.group('localbranch') + '---' + match.group('remotebranch'))
        if args.fetch:
            r = subprocess.run(['git', '--git-dir={repo}'.format(repo=git_repo), 'fetch'], stdout=subprocess.PIPE)
        # print(pathlib.Path(path).absolute().split())

if __name__ == '__main__':
    main()

