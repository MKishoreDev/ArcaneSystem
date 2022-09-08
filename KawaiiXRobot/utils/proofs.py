import re
import shlex

from io import StringIO
from typing import Dict, Tuple
from argparse import ArgumentParser

class Proofs:
       def _init_(self, proofs):
          self.proof = None
