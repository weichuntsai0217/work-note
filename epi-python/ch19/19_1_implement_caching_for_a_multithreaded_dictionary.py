"""
  Use python 3.6.8
"""
import time # for testing
import random # for testing
import copy # for testing
import threading

mock_ans = {
  'a': ['aa', 'aaa'],
  'b': ['bb', 'bbb'],
  'c': ['cc', 'ccc'],
}
mock_src = [key for key in mock_ans]

def closest_in_dictionary(w):
  """
    This is just a mock function for testing.
  """
  global mock_ans
  time.sleep(1)
  return mock_ans[w]

class req(object):
  """
    This is just a mock class for testing.
  """
  @staticmethod
  def extract_word_to_check_from_request():
    global mock_src
    time.sleep(0.5)
    return mock_src[random.randint(0, len(mock_src) - 1)]

class resp(object):
  """
    This is just a mock class for testing.
  """
  @staticmethod
  def encode_into_response(closest_word, w):
    global mock_ans
    time.sleep(0.2)
    if closest_word == mock_ans[w]:
      print('[SUCCESS] {} -> {}'.format(w, closest_word))
    else:
      raise ValueError('[ERROR] {} -> {}'.format(w, closest_word))



class SpellCheckService(object):
  w_last = None
  closest_to_last_word = None
  lock = threading.Lock()

  @staticmethod
  def service(req, resp):
    w = req.extract_word_to_check_from_request()
    result = None
    with SpellCheckService.lock:
      if w == SpellCheckService.w_last:
        result = copy.deepcopy(SpellCheckService.closest_to_last_word)

    if result == None:
      result = closest_in_dictionary(w)
      with SpellCheckService.lock:
        SpellCheckService.w_last = w
        SpellCheckService.closest_to_last_word = result
    resp.encode_into_response(result, w)
    """
    For the above line 'resp.encode_into_response', I input w as the 2nd argument just for testing. In fact,
    we don't need to input w as the 2nd argument just like the solution on page 316 of EPI in python.
    """

def target_to_run(i):
  while True:
    SpellCheckService.service(req, resp)
    time.sleep(random.random())


def main():
  threads = [threading.Thread(target=target_to_run, args=(i, )) for i in range(3)]
  for i in range(3):
    threads[i].start()

  for i in range(3):
    threads[i].join()

if __name__ == '__main__':
  main()
