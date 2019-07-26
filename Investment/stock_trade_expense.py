import yaml

def is_dealer_valid(config, raw_data):
  valid_dealer_names = set()
  for d in config['securities_dealers']:
    valid_dealer_names.add(d['dealer_name'])

  for d in raw_data['securities_dealers']:
    if d['dealer_name'] not in valid_dealer_names:
      raise ValueError(
        '"{}" is not a valid dealer name. Please check "stock_trade_expense_config.yaml" for more details.'.format(
          d['dealer_name']))
  

def get_expense():
  config = None
  with open('stock_trade_expense_config.yaml', 'r') as stream:
    config = yaml.load(stream)

  raw_data = None
  with open('stock_trade_expense_input.yaml', 'r') as stream:
    raw_data = yaml.load(stream)

  is_dealer_valid(config, raw_data)
  
  


def show_expense(data):
  pass

def main():
  show_expense(get_expense())

if __name__ == '__main__':
  main()
