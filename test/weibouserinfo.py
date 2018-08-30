#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import urllib.request
import mybase
import ssl
import re

ssl._create_default_https_context = ssl._create_unverified_context