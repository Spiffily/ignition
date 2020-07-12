#!/usr/bin/env python3
import os
from os import * # Import bash run abilities

desktop_session = os.environ['XDG_CURRENT_DESKTOP'].lower()
print(desktop_session)
