class App:
  @staticmethod
  def run():
    from packages.astronomy import Astronomy
    from packages.args import args

    print("[-] STARTING, wait a few seconds...\n\n")
    
    args = args()
    
    if not args.curiosity and not args.planet:
      print("Use -h, you must have been confused...")
      exit(1)
    if args.curiosity and not args.planet:
      print("\nCURIOSITY:", Astronomy.curiosity())
      exit(0)
    
    Astronomy = Astronomy(args)
    url  = Astronomy.api()
    code = Astronomy.request(url)
    data = Astronomy.filter(code)
    
    if not args.file:
      pass
    else:
      Astronomy.write_file(str(data))
    if args.curiosity:
      print("\nCURIOSITY:", Astronomy.curiosity())
    print("*"*50)
    print("\n[+] Thanks for using!")


  @staticmethod
  def main():
    from packages.banner import art, clear
    import timeit
    
    ini = timeit.default_timer()
    clear()
    art()
    App.run()
    fin = timeit.default_timer()
    
    print("\n[+] RUNTIME: %f seconds\n" % (fin - ini))
    print("*"*50)
