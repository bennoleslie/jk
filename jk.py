#!/usr/bin/env python3
"""A very simple/stupid assembler for the jk language.

Usage: ./jk.py example.jk | arm-none-eabi-as
"""
import argparse
import sys

def strip_empty(lines):
    """Strip the lines, and only yield non-empty lines."""
    for l in lines:
        l = l.strip()
        if len(l) != 0:
            yield l


def remove_comments(lines):
    """Remove any comment lines."""
    for l in lines:
        if not l.startswith('#'):
            yield l


def split(lst, val):
    """Split a list in two around val."""
    try:
        idx = lst.index(val)
    except ValueError:
        return lst, []
    return lst[:idx], lst[idx + 1:]


def as_opinvokes(lines):
    """Convert liens to OpInvoke instances."""
    for l in lines:
        parts = l.split()
        (oper, *args), ret = split(parts, '=>')
        args = [x[1:] for x in args]
        ret = [x[1:] for x in ret]
        yield OpInvoke(oper, args, ret)


class OpInvoke:
    """OpInvoke represents the invocation of an operation."""
    def __init__(self, name, args, rets):
        self.name = name
        self.args = args
        self.rets = rets

    def asm(self):
        """Return the raw assembler for this operation."""
        if self.name in ['sub', 'add']:
            return '\t{}\t{}, {}, {}\n'.format(self.name, self.rets[0], self.args[0], self.args[1])

    def __str__(self):
        return "<OpInvoke {} {} => {}>".format(self.name, self.args, self.rets)


def jk_compile(source, output):
    """Compile a jk source file into the output file."""
    for oi in as_opinvokes(remove_comments(strip_empty(source.readlines()))):
        output.write(oi.asm())


def main(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('source', help="Source file")

    args = parser.parse_args(argv[1:])

    with open(args.source) as f:
        jk_compile(f, sys.stdout)

    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
