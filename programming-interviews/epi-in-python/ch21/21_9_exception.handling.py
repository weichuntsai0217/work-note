"""
  Use python 3.6.8
"""
"""
  Question: Briefly describe handling in Python, paying special attention to the roles played
  by try, except, else, finally, and raise. Rewrite the following function `get_col_sum` using exceptions
  to make it more robust.
  ```
  # The function you must modify:
  def get_col_sum(filename, col):
    import csv
    csv_file = open(filename)
    csv_reader = csv.reader(csv_file)
    running_sum = 0
    for row in csv_reader:
      value = row[col]
      running_sum += int(value)
    csv_file.close()
    print('Sum =', str(running_sum))
  ```

  The error handling code structure is like this:
  try:
    `the code we want to run.`
  except `Some Error`:
    `the code to run when error happened in try block.`
  else:
    `the code to run when no error happened (everything is successful) in try block.`
  finally:
    ```
      the code must run after try except/else. Note that even we have return in try except/else, finally block would
      always be run.
    ```

  raise is used to trigger error by developers and the if raise an error, the code after raise would not be run.

  For basic usage, please refer to the code in `main`

"""

class ColSumCsvParseException(Exception):
  def __init__(self, *args):
    Exception.__init__(self, *args)
    self.line_number = args[1]

def get_col_sum(filename, col):
  import csv
  csv_file = open(filename) # this line may raise IOError, propagate to caller.
  csv_reader = csv.reader(csv_file)
  running_sum = 0
  line_number = 0
  try:
    for row in csv_reader:
      if col >= len(row):
        raise IndexError('Not enough netries in row', str(row))
      value = row[col]
      try:
        running_sum += int(value)
      except ValueError:
        print('Cannot convert', value, 'to int, ignoring')
      line_number += 1
  except csv.Error:
    print('In csv.Error handler')
    raise ColSumCsvParseException('Error processing csv', line_number)
  else:
    print('Sum =', str(running_sum))
  finally:
    csv_file.close()
    return running_sum


def example(use_error=False):
  # This is just a basic usage review.
  try:
    if use_error:
      raise IOError('IOError happened.')
    print('Everything is OK.')
  except IOError:
    print('I got an IOError')
    return 'failure'
  else:
    return 'success'
  finally:
    print('Here is finally.') 

def main():
  print('\n=== No error example ===')
  res_success = example()
  print(res_success)

  print('\n=== With error example ===')
  res_failure = example(True)
  print(res_failure)

if __name__ == '__main__':
  main()
