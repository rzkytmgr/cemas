import re
import os.path
from util import Logger
from termcolor import colored
from constant import AVAILABLE_SCANNER
from urllib3 import PoolManager, Timeout, Retry

class Core:
  
  def __init__(self, output_path: str, timeout: int) -> None:
    self.http = PoolManager(timeout=Timeout(total=timeout), retries=Retry(total=2, backoff_factor=0.1), headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 RuxitSynthetic/1.0 v935043067587085993 t2092535937092281841 athf552e454 altpriv cvcv=2 smf=0'})
    self.output_path = output_path
    self.log = Logger()
    pass

  def scan(self, target: str, cms_arg: list):
    try:
      response = self.http.request('GET', target)
      response_data = response.data.decode('utf-8').lower()
      rmatch = re.search('<meta name="generator" content="(.*?)"', response_data)
      
      if 'wordpress' in rmatch.group(1) and ('wp' in cms_arg or 'wordpress' in cms_arg):
        self.log.success(f'{target} - {colored("WordPress",color="light_green")}')
        self.append_target(target, 'WordPress.txt')
        pass
      elif 'joomla' in rmatch.group(1) and ('joom' in cms_arg or 'joomla' in cms_arg):
        self.log.success(f'{target} - {colored("Joomla",color="light_green")}')
        self.append_target(target, 'Joomla.txt')
        pass
      elif 'drupal' in rmatch.group(1) and ('dru' in cms_arg or 'drupal' in cms_arg):
        self.log.success(f'{target} - {colored("Drupal",color="light_green")}')
        self.append_target(target, 'Drupal.txt')
        pass
      elif 'Magento' in rmatch.group(1) and ('mage' in cms_arg or 'magento' in cms_arg):
        self.log.success(f'{target} - {colored("Magento",color="light_green")}')
        self.append_target(target, 'Magento.txt')
        pass
      else:
        self.log.info(f'{target} - {colored("Others",color="light_yellow")}')
        self.append_target(target, 'Others.txt')
        pass

    except Exception as e:
      self.log.error(f'{colored(f"{target} - Dead/Timeout/Error",color="light_red")}')
      self.append_target(target, 'ErrorOrTimeout.txt')
      pass
    pass
  
  def append_target(self, target: str, cms: str):
    os.makedirs(self.output_path, exist_ok=True)
    output_file_path = os.path.join(self.output_path, cms)
    if os.path.exists(output_file_path):
      with open(output_file_path, 'r') as file:
        if target in ''.join(file.readlines()):
          return None

    with open(output_file_path, 'a') as file:
      file.write(f'{target}\n')