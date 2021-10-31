class Sudoku:
    def __init__(self):
        self.numbers = [[0 for i in range(9)] for j in range(9)]

    def load(self, filename):
        f = open(filename, "r")
        r = 1
        for line in f:
            c = 1
            # each line contains a row
            for s in line.split():
                self.set(r, c, int(s))
                c += 1

            r += 1

    def get(self, r, c):
        return self.numbers[r - 1][c - 1]

    def set(self, r, c, value):
        self.numbers[r - 1][c - 1] = value

    def read_sol(self, sol):
        # sol = {115: True, 259: True, 386: True, 418: True, 456: True, 548: True, 617: True, 772: True, 851: True, 895: True, 111: False, 112: False, 113: False, 114: False, 116: False, 117: False, 118: False, 119: False, 121: False, 122: False, 123: False, 124: False, 125: False, 126: False, 127: False, 128: True, 129: False, 131: False, 132: False, 133: False, 134: False, 135: False, 136: True, 137: False, 138: False, 139: False, 141: False, 142: False, 143: False, 144: True, 145: False, 146: False, 147: False, 148: False, 149: False, 151: False, 152: True, 153: False, 154: False, 155: False, 156: False, 157: False, 158: False, 159: False, 161: True, 162: False, 163: False, 164: False, 165: False, 166: False, 167: False, 168: False, 169: False, 171: False, 172: False, 173: False, 174: False, 175: False, 176: False, 177: False, 178: False, 179: True, 181: False, 182: False, 183: False, 184: False, 185: False, 186: False, 187: True, 188: False, 189: False, 191: False, 192: False, 193: True, 194: False, 195: False, 196: False, 197: False, 198: False, 199: False, 211: False, 212: False, 213: True, 214: False, 215: False, 216: False, 217: False, 218: False, 219: False, 221: True, 222: False, 223: False, 224: False, 225: False, 226: False, 227: False, 228: False, 229: False, 231: False, 232: False, 233: False, 234: False, 235: False, 236: False, 237: True, 238: False, 239: False, 241: False, 242: False, 243: False, 244: False, 245: True, 246: False, 247: False, 248: False, 249: False, 251: False, 252: False, 253: False, 254: False, 255: False, 256: False, 257: False, 258: False, 261: False, 262: False, 263: False, 264: False, 265: False, 266: True, 267: False, 268: False, 269: False, 271: False, 272: False, 273: False, 274: True, 275: False, 276: False, 277: False, 278: False, 279: False, 281: False, 282: False, 283: False, 284: False, 285: False, 286: False, 287: False, 288: True, 289: False, 291: False, 292: True, 293: False, 294: False, 295: False, 296: False, 297: False, 298: False, 299: False, 311: False, 312: False, 313: False, 314: True, 315: False, 316: False, 317: False, 318: False, 319: False, 321: False, 322: False, 323: False, 324: False, 325: False, 326: False, 327: False, 328: False, 329: True, 331: False, 332: True, 333: False, 334: False, 335: False, 336: False, 337: False, 338: False, 339: False, 341: False, 342: False, 343: True, 344: False, 345: False, 346: False, 347: False, 348: False, 349: False, 351: False, 352: False, 353: False, 354: False, 355: False, 356: False, 357: False, 358: True, 359: False, 361: False, 362: False, 363: False, 364: False, 365: False, 366: False, 367: True, 368: False, 369: False, 371: False, 372: False, 373: False, 374: False, 375: True, 376: False, 377: False, 378: False, 379: False, 381: False, 382: False, 383: False, 384: False, 385: False, 387: False, 388: False, 389: False, 391: True, 392: False, 393: False, 394: False, 395: False, 396: False, 397: False, 398: False, 399: False, 411: False, 412: False, 413: False, 414: False, 415: False, 416: False, 417: False, 419: False, 421: False, 422: False, 423: False, 424: False, 425: True, 426: False, 427: False, 428: False, 429: False, 431: False, 432: False, 433: False, 434: True, 435: False, 436: False, 437: False, 438: False, 439: False, 441: False, 442: False, 443: False, 444: False, 445: False, 446: False, 447: False, 448: False, 449: True, 451: False, 452: False, 453: False, 454: False, 455: False, 457: False, 458: False, 459: False, 461: False, 462: False, 463: True, 464: False, 465: False, 466: False, 467: False, 468: False, 469: False, 471: True, 472: False, 473: False, 474: False, 475: False, 476: False, 477: False, 478: False, 479: False, 481: False, 482: True, 483: False, 484: False, 485: False, 486: False, 487: False, 488: False, 489: False, 491: False, 492: False, 493: False, 494: False, 495: False, 496: False, 497: True, 498: False, 499: False, 511: False, 512: False, 513: False, 514: False, 515: False, 516: False, 517: False, 518: False, 519: True, 521: False, 522: False, 523: False, 524: False, 525: False, 526: True, 527: False, 528: False, 529: False, 531: True, 532: False, 533: False, 534: False, 535: False, 536: False, 537: False, 538: False, 539: False, 541: False, 542: False, 543: False, 544: False, 545: False, 546: False, 547: False, 549: False, 551: False, 552: False, 553: False, 554: False, 555: False, 556: False, 557: True, 558: False, 559: False, 561: False, 562: True, 563: False, 564: False, 565: False, 566: False, 567: False, 568: False, 569: False, 571: False, 572: False, 573: True, 574: False, 575: False, 576: False, 577: False, 578: False, 579: False, 581: False, 582: False, 583: False, 584: False, 585: True, 586: False, 587: False, 588: False, 589: False, 591: False, 592: False, 593: False, 594: True, 595: False, 596: False, 597: False, 598: False, 599: False, 611: False, 612: False, 613: False, 614: False, 615: False, 616: False, 618: False, 619: False, 621: False, 622: True, 623: False, 624: False, 625: False, 626: False, 627: False, 628: False, 629: False, 631: False, 632: False, 633: True, 634: False, 635: False, 636: False, 637: False, 638: False, 639: False, 641: True, 642: False, 643: False, 644: False, 645: False, 646: False, 647: False, 648: False, 649: False, 651: False, 652: False, 653: False, 654: False, 655: True, 656: False, 657: False, 658: False, 659: False, 661: False, 662: False, 663: False, 664: True, 665: False, 666: False, 667: False, 668: False, 669: False, 671: False, 672: False, 673: False, 674: False, 675: False, 676: False, 677: False, 678: True, 679: False, 681: False, 682: False, 683: False, 684: False, 685: False, 686: False, 687: False, 688: False, 689: True, 691: False, 692: False, 693: False, 694: False, 695: False, 696: True, 697: False, 698: False, 699: False, 711: False, 712: False, 713: False, 714: False, 715: False, 716: True, 717: False, 718: False, 719: False, 721: False, 722: False, 723: True, 724: False, 725: False, 726: False, 727: False, 728: False, 729: False, 731: False, 732: False, 733: False, 734: False, 735: False, 736: False, 737: False, 738: False, 739: True, 741: False, 742: False, 743: False, 744: False, 745: False, 746: False, 747: True, 748: False, 749: False, 751: False, 752: False, 753: False, 754: True, 755: False, 756: False, 757: False, 758: False, 759: False, 761: False, 762: False, 763: False, 764: False, 765: True, 766: False, 767: False, 768: False, 769: False, 771: False, 773: False, 774: False, 775: False, 776: False, 777: False, 778: False, 779: False, 781: True, 782: False, 783: False, 784: False, 785: False, 786: False, 787: False, 788: False, 789: False, 791: False, 792: False, 793: False, 794: False, 795: False, 796: False, 797: False, 798: True, 799: False, 811: False, 812: True, 813: False, 814: False, 815: False, 816: False, 817: False, 818: False, 819: False, 821: False, 822: False, 823: False, 824: True, 825: False, 826: False, 827: False, 828: False, 829: False, 831: False, 832: False, 833: False, 834: False, 835: False, 836: False, 837: False, 838: True, 839: False, 841: False, 842: False, 843: False, 844: False, 845: False, 846: True, 847: False, 848: False, 849: False, 852: False, 853: False, 854: False, 855: False, 856: False, 857: False, 858: False, 859: False, 861: False, 862: False, 863: False, 864: False, 865: False, 866: False, 867: False, 868: False, 869: True, 871: False, 872: False, 873: False, 874: False, 875: False, 876: False, 877: True, 878: False, 879: False, 881: False, 882: False, 883: True, 884: False, 885: False, 886: False, 887: False, 888: False, 889: False, 891: False, 892: False, 893: False, 894: False, 896: False, 897: False, 898: False, 899: False, 911: True, 912: False, 913: False, 914: False, 915: False, 916: False, 917: False, 918: False, 919: False, 921: False, 922: False, 923: False, 924: False, 925: False, 926: False, 927: True, 928: False, 929: False, 931: False, 932: False, 933: False, 934: False, 935: True, 936: False, 937: False, 938: False, 939: False, 941: False, 942: True, 943: False, 944: False, 945: False, 946: False, 947: False, 948: False, 949: False, 951: False, 952: False, 953: True, 954: False, 955: False, 956: False, 957: False, 958: False, 959: False, 961: False, 962: False, 963: False, 964: False, 965: False, 966: False, 967: False, 968: True, 969: False, 971: False, 972: False, 973: False, 974: False, 975: False, 976: True, 977: False, 978: False, 979: False, 981: False, 982: False, 983: False, 984: True, 985: False, 986: False, 987: False, 988: False, 989: False, 991: False, 992: False, 993: False, 994: False, 995: False, 996: False, 997: False, 998: False, 999: True}

        for k,v in sol.items():
            str_k = str(k)
            if v:
                self.set(int(str_k[0])-1, int(str_k[1])-1, int(str_k[2]))


    def read_solution(self, filename):
        f = open(filename, "r")
        for line in f:
            # ignore unset variables
            literal = int(line)
            if literal > 0:
                r = int(line[0])
                c = int(line[1])
                v = int(line[2])
                self.set(r, c, v)
        f.close()

    def __str__(self):
        s = ""
        for r in range(1, 10):
            if r == 4 or r == 7:
                s += "---------------------\n"

            for c in range(1, 10):

                if c == 4 or c == 7:
                    s += "| "
                s = s + str(self.get(r, c))
                s += " "

            s += "\n"

        return s

    def sudoku_literal(self, r, c, v, neg=False):
        return ("-" if neg else "") + str(r) + str(c) + str(v)

    def cell_clause(self, r, c):

        s = ""

        # at least one value:
        atleastone_str = ""
        for value in range(1, 10):
            atleastone_str += self.sudoku_literal(r, c, value) + " "
        atleastone_str += " \n"

        s = atleastone_str

        for vi in range(1, 10):
            for vj in range(vi + 1, 10):
                s += self.sudoku_literal(r, c, vi, neg=True) + " "
                s += self.sudoku_literal(r, c, vj, neg=True) + " "
                s += "\n"

        return s

    def row_clause(self, r):
        s = ""
        for value in range(1, 10):
            for c in range(1, 10):
                s += self.sudoku_literal(r, c, value) + " "
            s += "\n"

        return s

    def col_clause(self, c):
        s = ""
        for value in range(1, 10):
            for r in range(1, 10):
                s += self.sudoku_literal(r, c, value) + " "
            s += "\n"

        return s

    def write_block_clauses(self, filehandle):

        s = ""

        for sr in range(1, 10, 3):
            for sc in range(1, 10, 3):
                for value in range(1, 10):
                    for r_offset in range(3):
                        for c_offset in range(3):
                            r = sr + r_offset
                            c = sc + c_offset
                            s += self.sudoku_literal(r, c, value) + " "

                    s += "\n"

        filehandle.write(s)

    def write_fixed_clauses(self, filehandle):
        s = ""
        for r in range(1, 10):
            for c in range(1, 10):
                value = self.get(r, c)
                if value !=  0:
                    s += self.sudoku_literal(r, c, value) + "\n"

        filehandle.write(s)


    def write_col_clauses(self, filehandle):
        for c in range(1, 10):
            clause = self.col_clause(c)
            filehandle.write(clause)


    def write_row_clauses(self, filehandle):
        for r in range(1, 10):
            clause = self.row_clause(r)
            filehandle.write(clause)

    def write_cell_clauses(self, filehandle):
        for r in range(1, 10):
            for c in range(1, 10):
                clause = self.cell_clause(r, c)
                filehandle.write(clause)

    def generate_cnf(self, filename):
        f = open(filename, "w")
        self.write_cell_clauses(f)
        self.write_row_clauses(f)
        self.write_col_clauses(f)
        self.write_block_clauses(f)
        self.write_fixed_clauses(f)
        f.close()


if __name__ == "__main__":
    test_sudoku = Sudoku()

    test_sudoku.load("puzzle1.sud")
    #print(test_sudoku)
    # print(sudoku_literal(2, 3, 9, neg=True))

    # print(cell_clause(1, 1))

    test_sudoku.generate_cnf("puzzle1.cnf")

    #test_sudoku.read_solution("rules.sol")
    print(test_sudoku)
