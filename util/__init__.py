from termcolor import colored

class Logger:
  def logger(self, text: str='', color: str='white', prefix: str="", prefix_color: str='light_yellow', attrs: list=[], end: str = '\n'):
    print(colored(text=prefix, color=prefix_color, attrs=['bold']), colored(text=text, color=color, attrs=attrs), end=end)

  def error(self, text: str, end: str = '\n'):
    self.logger(prefix_color='light_red', prefix='⟝ ', text=text, color='white', end=end)

  def success(self, text: str, end: str = '\n'):
    self.logger(prefix_color='light_green', prefix='⟝ ', text=text, color='white', end=end)

  def info(self, text: str, end: str = '\n'):
    self.logger(prefix_color='light_yellow', prefix='⟝ ', text=text, color='white', end=end)

  def unique(self, text: str, end: str = '\n'):
    self.logger(prefix_color='light_cyan', prefix='⟝ ', text=text, color='white', end=end)

  def tab(self, text: str, end: str = '\n'):
    self.logger(prefix_color='white', prefix='  ', text=text, color='white', end=end)

  def custom(self, text: str, color: str, attrs: list):
    self.logger(text=text, color=color, attrs=attrs)