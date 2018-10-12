def get_indices_of_item_weights(weights, limit):
  result = ()
  d = dict()
  i = 0
  for item in weights:
    d[item] = i
    i = i + 1
  
  for k,v in d.items():
    if len(d) is 1:
      return result
    if d[limit - k] is not None:
     result = (d[k], d[limit - k])
     return result

if __name__ == '__main__':
  # You can write code here to test your implementation using the Python repl
  pass 