#!/usr/bin/python3.9

import binascii, argparse, sys

def TextToHex(x):
  result = binascii.hexlify(bytes(x.encode()))
  print('Result:\n',result)

def HexToText(x):
  result = binascii.unhexlify(bytes(x.encode()))
  print('Result:\n',result)

def main():
  parser = argparse.ArgumentParser(usage='hex-converter.py [OPTION] [INPUT]',epilog="\033[32;1mThx for using")
  
  parser.add_argument('-hex',help="Text to hex convert")
  parser.add_argument('-unhex',help='Hex to text convert')
  
  arg = parser.parse_args()
  
  if len(sys.argv) > 1:
    if arg.hex:
      TextToHex(arg.hex)
    if arg.unhex:
      HexToText(arg.unhex)
  else:
    parser.print_help()
    
if __name__ == '__main__':
  main()