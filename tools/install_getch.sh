#!/bin/bash
wget https://pypi.python.org/packages/source/g/getch/getch-1.0-python2.tar.gz#md5=586ea0f1f16aa094ff6a30736ba03c50 -O /tmp/getch.tar.gz
cd /tmp
sudo pip install getch.tar.gz && exit 0 || echo "You need pip and python-dev"
