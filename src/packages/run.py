class App:
  @staticmethod
  def main(args) -> None:
    """Main function to run the program
    """
    from src.packages.astronomy import Astronomy
    from main import typeAnim

    if not args.curiosity and not args.planet:
      typeAnim("Use -h, you must have been confused...")
      exit(1)

    if args.curiosity and not args.planet:
      typeAnim(f"\nCURIOSITY: {Astronomy.curiosity()}")
      exit(0)

    typeAnim("[-] STARTING, wait a few seconds...\n\n")

    astro = Astronomy(args)
    code  = astro.request()
    data  = astro._filter(code)

    if not args.file:
      pass
    else:
      astro.write_file(str(data))

    if args.curiosity:
      typeAnim(f"\nCURIOSITY: {Astronomy.curiosity()}")

    typeAnim("*"*50)
    typeAnim("\n[+] Thanks for using!")


  @staticmethod
  def run(args) -> None:
    """This function use main() and count the time
    """
    from src.interface.ui import clear, banner
    from main import typeAnim
    import timeit

    ini = timeit.default_timer()
    clear()
    banner()
    App.main(args)
    fin = timeit.default_timer()
    
    typeAnim("\n[+] RUNTIME: %f seconds\n" % (fin - ini))
    typeAnim("*"*50)
