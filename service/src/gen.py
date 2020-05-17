#!/usr/bin/env python

import os
from os import system as run
from os.path import *
import sys
from sys import exit
import hashlib
from collections import Counter, defaultdict
import shutil

from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad, unpad

from pwn import *
import click

import random

context.log_level = 'debug'


@click.group()
def cli():
    pass


@cli.command()
@click.option('--debug', is_flag=True, default=False)
@click.option('--local', is_flag=True, default=False)
def genfiles(debug, local):
    '''It generates the token, state, and (encrypted) flag files, starting from
    the various locks and flag value.'''

    flag = 'OOO{r3VEr51nG_b4sH_5Cr1P7s_I5_lAm3_bU7_R3vErs1Ng_b4SH_is_31337}'

    token = os.urandom(32)
    enckey = os.urandom(32)

    keywords = [
        'unlockbabylock',
        'badr3d1r',
        'verysneaky',
        'leetness',
        'vneooo',
        'eval',
        'ret',
        'n3t',
        'sig',
        'yo',
        'aro',
        'fnx',
        'ifonly',
    ]

    def hashit(token, keyword):
        val = token + keyword + token
        h = hashlib.sha256(val).digest()
        return h

    def encit(val, key):
        val = pad(val, 16)
        cipher = AES.new(key, AES.MODE_CBC)
        out = cipher.encrypt(val)
        out = cipher.iv + out
        return out

    encflag = encit(flag, enckey)
    # just to make sure we don't leak it, destroy the flag
    flag = None

    state = enckey
    for kw in keywords:
        h = hashit(token, kw)
        assert len(state) == len(h)
        state = xor(state, h)

    print 'token: %s' % token.encode('hex')
    print 'state: %s' % state.encode('hex')
    print 'enckey: %s' % enckey.encode('hex')
    print 'encflag: %s' % encflag.encode('hex')

    target_dir = abspath(join(dirname(__file__), '../data'))
    if not isdir(target_dir):
        os.makedirs(target_dir)

    token_fp = join(target_dir, 'token')
    state_fp = join(target_dir, 'state')
    flag_fp = join(target_dir, 'flag')

    with open(token_fp, 'wb') as f:
        f.write(token)

    with open(state_fp, 'wb') as f:
        f.write(state)

    with open(flag_fp, 'wb') as f:
        f.write(encflag)

    print 'Generated files'
     

if __name__ == '__main__':
    cli()
