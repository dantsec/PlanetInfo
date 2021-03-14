def art():
  print("""
                                                                     ..;===+.
                                                                .:=iiiiii=+=
                                                             .=i))=;::+)i=+,
                                                          ,=i);)I)))I):=i=;
                                                       .=i==))))ii)))I:i++
                                                     +)+))iiiiiiii))I=i+:'
                                .,:;;++++++;:,.       )iii+:::;iii))+i='
                             .:;++=iiiiiiiiii=++;.    =::,,,:::=i));=+'
                           ,;+==ii)))))))))))ii==+;,      ,,,:=i))+=:
                         ,;+=ii))))))IIIIII))))ii===;.    ,,:=i)=i+
                        ;+=ii)))IIIIITIIIIII))))iiii=+,   ,:=));=,
                      ,+=i))IIIIIITTTTTITIIIIII)))I)i=+,,:+i)=i+
                     ,+i))IIIIIITTTTTTTTTTTTI))IIII))i=::i))i='
                    ,=i))IIIIITLLTTTTTTTTTTIITTTTIII)+;+i)+i`
                    =i))IIITTLTLTTTTTTTTTIITTLLTTTII+:i)ii:'
                   +i))IITTTLLLTTTTTTTTTTTTLLLTTTT+:i)))=,
                   =))ITTTTTTTTTTTLTTTTTTLLLLLLTi:=)IIiii;
                  .i)IIITTTTTTTTLTTTITLLLLLLLT);=)I)))))i;
                  :))IIITTTTTLTTTTTTLLHLLLLL);=)II)IIIIi=:
                  :i)IIITTTTTTTTTLLLHLLHLL)+=)II)ITTTI)i=
                  .i)IIITTTTITTLLLHHLLLL);=)II)ITTTTII)i+
                  =i)IIIIIITTLLLLLLHLL=:i)II)TTTTTTIII)i'
                +i)i)))IITTLLLLLLLLT=:i)II)TTTTLTTIII)i;
              +ii)i:)IITTLLTLLLLT=;+i)I)ITTTTLTTTII))i;
             =;)i=:,=)ITTTTLTTI=:i))I)TTTLLLTTTTTII)i;
           +i)ii::,  +)IIITI+:+i)I))TTTTLLTTTTTII))=,
         :=;)i=:,,    ,i++::i))I)ITTTTTTTTTTIIII)=+' -->PLANET INFO DISPLAY <--
       .+ii)i=::,,   ,,::=i)))iIITTTTTTTTIIIII)=+    -->DEVELOPED BY: DANTALION <--
      ,==)ii=;:,,,,:::=ii)i)iIIIITIIITIIII))i+:'
     +=:))i==;:::;=iii)+)=  `:i)))IIIII)ii+'
   .+=:))iiiiiiii)))+ii;
  .+=;))iiiiii)));ii+
 .+=i:)))))))=+ii+
.;==i+::::=)i=;
,+==iiiiii+,
`+=+++;
  """)

def clear():
  import os
  os.system(['clear', 'cls'][os.name == 'nt'])

def run():
  from packages.astronomy import Astronomy
  from packages.args import args
  from packages.curiosity import curiosity
  import timeit
  
  ini = timeit.default_timer()
  print("[+] STARTING...\n\n\n")
  args = args()
  if not args.curiosity and not args.planet:
    print("Use -h, you must have been confused...")
    exit(1)
  if args.curiosity and not args.planet:
    print("\nCURIOSITY:", curiosity())
    exit(1)
  Astronomy = Astronomy(args)
  url  = Astronomy.planet_url()
  code = Astronomy.request(url)
  data = Astronomy.filter(code)
  if not args.file:
    print(data[0:0])
  else:
    Astronomy.write_file(str(data))
  if args.curiosity:
    print("\n\n")
    print("CURIOSITY:", curiosity())

  fin = timeit.default_timer()

  print("\n[+] RUNTIME: %f seconds\n" % (fin - ini))
  print("[+] Thanks for using!")
