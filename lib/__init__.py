import re
import os
from argparse import ArgumentTypeError
from constant import AVAILABLE_SCANNER


def get_filepath(filename: str):
  return os.path.join(os.path.dirname(__file__), '..', filename)

def arg_file_validator(filename: str):
  if not filename.endswith('.txt'):
    raise ArgumentTypeError('only accept .txt file extension')

  if not os.path.exists(get_filepath(filename)):
    raise ArgumentTypeError('your input doesn\'t seems to be a file')

  return filename

def arg_cms_validator(cms: str):
  pattern = r"^\{(.*)\}$"
  match = re.match(pattern, cms)

  if match is None:
    raise ArgumentTypeError('make sure you use this pattern {cms} or leave it without -c/--cms flag')

  cms = cms[1:-1].split(',')
  if not ''.join(cms):
    raise ArgumentTypeError('the cms argument cannot be empty')
  
  for c in cms:
    if c not in AVAILABLE_SCANNER:
      raise ArgumentTypeError(f'we cannot recognized the \'{c}\' cms what you input')

  return cms
