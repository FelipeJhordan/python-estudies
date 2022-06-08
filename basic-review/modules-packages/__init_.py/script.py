from paises import Sulamericanos
from paises import Europeus
from continentes import america
 
def main(args):
    sul = Sulamericanos()
    sul.print_paises()
 
    eu = Europeus()
    eu.print_paises()
 
 
    return
 
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))