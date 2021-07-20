class App:
  @staticmethod
  def main(args) -> None:
    """Main function to run the program
    """
    from src.packages.astronomy import Astronomy

    if not args.curiosity and not args.planet:
      print("Use -h, you must have been confused...")
      exit(1)

    if args.curiosity and not args.planet:
      print("\nCURIOSITY:", Astronomy.curiosity())
      exit(0)

    print("[-] STARTING, wait a few seconds...\n\n")

    astro = Astronomy(args)
    code  = astro.request()
    data  = astro._filter(code)

    if not args.file:
      pass
    else:
      astro.write_file(str(data))

    if args.curiosity:
      print("\nCURIOSITY:", Astronomy.curiosity())

    print("*"*50)
    print("\n[+] Thanks for using!")


  @staticmethod
  def run(args) -> None:
    """This function use main() and count the time
    """
    from src.interface.ui import clear, banner
    import timeit

    ini = timeit.default_timer()
    clear()
    banner()
    App.main(args)
    fin = timeit.default_timer()
    
    print("\n[+] RUNTIME: %f seconds\n" % (fin - ini))
    print("*"*50)
