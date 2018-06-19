#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Usage: python yaml_cfg_formatter.py js|firebase source.txt result.yaml """

import sys


def main():
    if sys.argv[1] != 'js' and sys.argv[1] != 'firebase':
        print('First argument must be "js" or "firebase"')
        sys.exit(1)
    result = ['%s\n' % item for item in ('''apiVersion: v1
data:
  %s: |+''' % ('cfg.js' if sys.argv[1] == 'js' else 'servolab-sandbox-firebase-adminsdk.json',)).splitlines()]

    with open(sys.argv[2], 'r') as src:
        result.extend(['    %s' % line for line in src.readlines()])

    result.extend(['%s\n' % item for item in ('''
kind: ConfigMap
metadata:
   name: %s-{{ template "api.fullname" . }}
''' % ('cfg-js' if sys.argv[1] == 'js' else 'firebase-json')).splitlines()])

    with open(sys.argv[3], 'w') as out:
        out.writelines(result)


if __name__ == '__main__':
    main()

