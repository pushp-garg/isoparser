TEST_DATA = [
    ("isoparser/test/test.iso",
    {b'a': b'==> /dev/urandom <==\n\xbf\x91BL\x91\xb3$\x9cfRa\t\x8f\x88\x84\xf6\xebd\xc2:T03\xdc\xfe\x07\xe5}\xbb|?\xd7 V\xff\x98\xb7\xc6\xc8r7\x08\xcb\t\xb5\xa4\x05`\x82\xa6\x91\xee\xf8\xf3mFw/d\x95\x035\xfc\xac\x88\x1e*C\xcb\xa7',
                   b'a long name of a directory WITH some \xc5\x82\xc5\x82 UTF8 \xc4\x85\xc5\x82 characters and with some comas (,) and very long\xc5\x82': {b'rrrrcooo': b''},
                   b'a long name of a directory without any UTF8 characters, but with some comas and very long': {b'aeu': b'',
                       b'content': b'pR\xb7\x04\xc8\xd5caa\x12@o\xc0\xe6/-\xb4+b\xf5}+\x046\x9e\xf3\x13\x97\xe1r4\xc4\xe8M\xdcC\xa4\x87\x90"?\x19\xc3\xa4\x9a\xbdK\x1bq\xbb\x18\x13|\\\x89\x0bpT\x1d9m\xdd\t\xd0`g%\xead\xd3'},
                   b'a very long name': b'',
                   b'a\xc5\x82\xc3\xb3k long name with UTF characters.\xc5\x9ba\xc5\x82\xc5\x82.txt': b'',
                   b'directory': {b'test': b''},
                   b'one': b'',
                   b'something': b"\x01\x98\t\x14\x87\xc6\xee\xd3\x8e\xdfLX\xc2\x04\xd8\xe4f\x1fA\xef\x8c\xc0S\xa2\xe2\x0c\xc3\xad\xec\x8e\x9d\xe1\x1e\xde\x83\x8a\x935\x11\x98\x0c\x97\xd9\x80\x98\xa5\x8c\xac\xb7\x99D\x82HT'\x88x\x85\x91y\x99\xc4E\xc4\x14\xba\xeb\xba\xb3\xc1"}

     ),
    ("isoparser/test/test2.iso",
    {b'At per quod error tantas, dicta euripidis et vel?': b'At per quod error tantas, dicta euripidis et vel? Probatus maiestatis pri et. Debet adversarium reprehendunt vis in, qui novum dicit posidonium ex, no facer forensibus constituto mea. Et mel tincidunt consequuntur, mei posse numquam dignissim in.\n\nEros senserit eu mel, ne possim quodsi per? Idque aeque mel ad! Lorem tibique deseruisse id eos. Odio rebum ex sea. Veniam ponderum ei sit, porro tibique quo id, elit conceptam duo et? Ea doctus gubergren sed, has ipsum conclusionemque no.\n',
     b'nemque vis ut, no sanctus nonumes repudiandae sit. Mel ei numquam tibique, latine aliquam ius id?': {b'ADicant iuvaret tibique vim ut? Nam te deleniti indoctum! Ex nihil nominati mei, at doctus blandit mea, \xc4\x85\xc5\x9b\xc5\x82\xc4\x99\xc3\xa9\xc5\x84\xc4\x85oando pertinax periculis est ex? Nonumy vivendum postulant t\xc2\xa2\xc2\xa2\xc2\xa4\xc2\xa5u': b'Postea appetere et his, eu eos eleifend persecuti? Ei eum case intellegam, ex propriae placerat cum, malis laboramus conclusionemque qui ea! Eos ei saepe altera facilis, dicam oporteat mediocritatem qui et. Eu oratio sapientem vis, everti admodum ad has, an electram tincidunt nam. Possim cetero atomorum id mei, in vocent convenire posidonium his. Te ullum saepe duo, te consequat urbanitas susc\n',
     b'Dicant iuvaret tibique vim ut? Nam te deleniti indoctum! Ex nihil nominati mei, at doctus blandit mea, quando pertinax periculis est ex? Nonumy vivendum postulant mei et. Duo cu propriae detraxit theophrastu': b'Postea appetere et his, eu eos eleifend persecuti? Ei eum case intellegam, ex propriae placerat cum, malis laboramus conclusionemque qui ea! Eos ei saepe altera facilis, dicam oporteat mediocritatem qui et. Eu oratio sapientem vis, everti admodum ad has, an electram tincidunt nam. Possim cetero atomorum id mei, in vocent convenire posidonium his. Te ullum saepe duo, te consequat urbanitas susc\n', b'\xc2\xa4': {b'Dicant iuvaret tibique vim ut? Nam te deleniti indoctum! Ex nihil nominati mei, at doctus blandit mea, quando pertinax periculis est ex? Nonumy vivendum postulant mei et. Duo c\xc5\x82\xc4\x99\xc4\x85\xc3\xb3\xc3\xb3\xc3\xb3u propriae detraxit theophrast\xc2\xa2\xc2\xa2\xc2\xa4\xc2\xa5u': b'Postea appetere et his, eu eos eleifend persecuti? Ei eum case intellegam, ex propriae placerat cum, malis laboramus conclusionemque qui ea! Eos ei saepe altera facilis, dicam oporteat mediocritatem qui et. Eu oratio sapientem vis, everti admodum ad has, an electram tincidunt nam. Possim cetero atomorum id mei, in vocent convenire posidonium his. Te ullum saepe duo, te consequat urbanitas susc\n',
     b'Dolorum lucilius intellegebat ad mel, pri integre imperdiet ut? In purto diceret': b'Dolorum lucilius intellegebat ad mel, pri integre imperdiet ut? In purto diceret eos, alterum fabellas vix ut, ne his magna mutat labore? Cu meis dolor hendrerit sea, vis et alterum aliquando, per ipsum exerci noster et? Ne saepe congue sed, definiebas interesset sit ei. Clita pericula deseruisse eu cum, in cum convenire moderatius? Sea zril choro ne. Mea mazim persecuti concludaturque cu.\n',
     b'empty': b'',
     b'iso': {b'a': b'==> /dev/urandom <==\n\xbf\x91BL\x91\xb3$\x9cfRa\t\x8f\x88\x84\xf6\xebd\xc2:T03\xdc\xfe\x07\xe5}\xbb|?\xd7 V\xff\x98\xb7\xc6\xc8r7\x08\xcb\t\xb5\xa4\x05`\x82\xa6\x91\xee\xf8\xf3mFw/d\x95\x035\xfc\xac\x88\x1e*C\xcb\xa7',
     b'a long name of a directory WITH some \xc5\x82\xc5\x82 UTF8 \xc4\x85\xc5\x82 characters and with some comas (,) and very long\xc5\x82': {b'rrrrcooo': b''},
     b'a long name of a directory without any UTF8 characters, but with some comas and very long': {b'aeu': b'',
     b'content': b'pR\xb7\x04\xc8\xd5caa\x12@o\xc0\xe6/-\xb4+b\xf5}+\x046\x9e\xf3\x13\x97\xe1r4\xc4\xe8M\xdcC\xa4\x87\x90"?\x19\xc3\xa4\x9a\xbdK\x1bq\xbb\x18\x13|\\\x89\x0bpT\x1d9m\xdd\t\xd0`g%\xead\xd3'},
     b'a very long name': b'',
     b'a\xc5\x82\xc3\xb3k long name with UTF characters.\xc5\x9ba\xc5\x82\xc5\x82.txt': b'',
     b'directory': {b'test': b''},
     b'one': b'',
     b'something': b"\x01\x98\t\x14\x87\xc6\xee\xd3\x8e\xdfLX\xc2\x04\xd8\xe4f\x1fA\xef\x8c\xc0S\xa2\xe2\x0c\xc3\xad\xec\x8e\x9d\xe1\x1e\xde\x83\x8a\x935\x11\x98\x0c\x97\xd9\x80\x98\xa5\x8c\xac\xb7\x99D\x82HT'\x88x\x85\x91y\x99\xc4E\xc4\x14\xba\xeb\xba\xb3\xc1"},
     b'vix eu cibo patrioque. Luptatum mnesarchum vim ex, vocibus molestie corrumpit ad cum. Consul everti eos a': b''}},
     b'test2': {b',': {},
     b',,': {},
     b'7': b'',
     b';': b'',
     b'a': b'',
     b'b': b'',
     b'dir': {b"'": b'', b'\\-\\-\\-\\-\\-': b''}},
     b'\xc4\x85\xc5\x9b\xc5\x82\xc3\xa9\xc3\xb3\xc4\x99\xc2\xbd\xc2\xbd\xc3\xa9\xe2\x80\x9e\xc2\xa4\xc2\xa4\xc2\xa4\xc2\xa2\xc2\xa4\xc2\xa4\xe2\x80\x9e\xc4\x85\xc2\xbb\xc2\xbb.\xc4\x85\xc4\x99\xc4\x99\xc3\xb3\xc2\xa2': b'Dicit alterum nominati te his, ne pro utinam ignota, vim posse altera at? Sanctus offendit convenire mea ut, an pri menandri repudiare efficiantur, an pro deserunt definitionem? His cu suas ignota detraxit! Sed cu ludus antiopam, pro no omnesque comprehensam, sea ea postea noster volumus. Ad quo ubique meliore consequat. Te nam feugiat vulputate assueverit, cum et nihil mucius omittam!\n\nMea audire insolens vituperatoribus an, labore quaeque quo ea, te alii salutatus has! Ei has iriure expetendis. Ex mel rebum aliquid voluptatibus, minim primis ad eos, ei eam habeo reformidans. No vis virtute voluptua. Veri essent appetere an eum, ne est libris bonorum. Ea eam sententiae referrentur.\n'}),
]
