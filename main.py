def ini():
  from packages.run import run
  import timeit
  
  ini = timeit.default_timer()
  run()
  fin = timeit.default_timer()
  print("RUNTIME: %f seconds" % (fin - ini))
  print("")

if __name__ == '__main__':
  ini()