import pygame, copy
from config import *
from drawing.pieces import *
from evaluation import *

temp_piece_list = {
    ' ': 0,
    'p': 0,
    'P': 0,
    'r': 0,
    'R': 0,
    'n': 0,
    'N': 0,
    'b': 0,
    'B': 0,
    'q': 0,
    'Q': 0,
    'k': 0,
    'K': 0
}

Zobrist_table = {
    0 : [379716459692, 681574598771, 976029390525, 814005198477, 929285387456, 451279860890, 467318546063, 43244428368, 943066643177, 542433681809, 530755655195, 676609462843],
    1 : [252957862543, 837635565963, 994580975407, 34419754377, 261011765882, 853850614420, 544234852596, 397479027426, 698923010450, 343708263084, 503697170424, 983342796304],
    2 : [620950271891, 790881049785, 843858206169, 332790355427, 945371491391, 97779348963, 1062295093518, 842224367513, 762023275093, 628883346643, 1080267691048, 242604651201],
    3 : [776001791852, 604696924065, 823245451755, 211713499579, 1054313142383, 52533459902, 248522000617, 473640767801, 149751891726, 554749441828, 581057372498, 175665470819],
    4 : [784294627405, 459722737829, 133227397000, 284549764658, 345984064936, 559755518807, 607038193370, 128785637826, 928416797413, 200751952550, 868842042191, 758155076723],
    5 : [696250990118, 743866781743, 753351811485, 1045336126856, 842950722962, 113576026448, 123601537760, 823128879244, 561013326221, 174831500364, 864526439873, 171545201411],
    6 : [439226454242, 251546451615, 545203110415, 980567052476, 376532329830, 1096670025158, 839073824289, 1017121914583, 1066003431864, 144307436203, 418666335875, 581295803352],
    7 : [378051124719, 469965669609, 1005200732909, 509670658564, 303009316922, 236724184658, 25822343873, 775367290576, 282476121656, 631438204662, 541322978214, 862781773764],
    8 : [445758400146, 1094916395490, 620235986579, 544932840877, 159951898675, 105337313582, 52988057793, 173865339818, 1094765618126, 613122875784, 526979646186, 193331779083],
    9 : [681597938877, 278627307654, 662770968652, 962753529611, 648353648072, 342121338158, 412489568812, 511042348503, 154124504557, 29171298170, 201643036440, 1065064928289],
    10 : [814087616087, 488226831424, 397253638922, 1097984087640, 792385465362, 1065654126839, 568503039929, 403894049289, 993448447187, 987865043669, 178414888920, 30960094354],
    11 : [518354080863, 989902708484, 995525618073, 824534740299, 469785712558, 34324374241, 479434097569, 672730563789, 483273012652, 297544517848, 183368150933, 941738621156],
    12 : [762017033719, 49159726639, 671431529579, 723487103292, 843490981712, 804743859925, 929178810500, 859528048984, 223203990438, 63426023009, 291361178951, 621354815856],
    13 : [527893969216, 115513419932, 215708896907, 568706803863, 166388221790, 279653034278, 103976682547, 151348342722, 4709858361, 348343658202, 916390694932, 650384104058],
    14 : [661937072974, 144823724191, 85894186707, 631218011418, 919441692454, 248709483012, 377562344528, 1082128491404, 277786754255, 679143119547, 937566416351, 1037395646946],
    15 : [165090203774, 78412433277, 668193878974, 351515407982, 571294981210, 675760427869, 799221633815, 201352147467, 545602585197, 319665786183, 1023069961229, 822254976652],
    16 : [1060536280782, 807328785182, 1067547702075, 921594769624, 197076748393, 319955012773, 272906655384, 895532463649, 905618673484, 370396954137, 688428231181, 761340377100],
    17 : [850223540962, 369253497837, 418176325149, 9481969424, 720663442985, 383544097938, 704997144098, 216435668038, 126374668388, 1092324992024, 312871400047, 943379754635],
    18 : [1094848851332, 327458161642, 185964768181, 366221417651, 616234939631, 952027263075, 80251415194, 967363587114, 155688881483, 876862604662, 949121950149, 411639699639],
    19 : [193843289221, 925754214781, 870900863988, 731769473825, 850848021785, 971079695491, 398760220623, 300572138162, 111271535662, 68867476328, 568991242210, 345532734294],
    20 : [1056482328329, 1040591567897, 120941812526, 737344690398, 581180851579, 492167662694, 869286391776, 1090451909147, 958288082158, 440801350029, 161526991602, 455281680563],
    21 : [859856730984, 223366222965, 65686763155, 650826081402, 970760073098, 973221881052, 592763560242, 921612404920, 537093908863, 610670412936, 277520078167, 1062502857765],
    22 : [697697430837, 523922988379, 823118146098, 961614052810, 33432598331, 1056711587563, 709728914, 753674969047, 877798319975, 69087284767, 160055625730, 965316366838],
    23 : [743759693013, 1023801278312, 239288497838, 601144706912, 709629979103, 555031860886, 941154596420, 303775015816, 680077222257, 114920066144, 416304447949, 1077814233102],
    24 : [202866374152, 575556967963, 553649536833, 555286123439, 269677166822, 936328949115, 216955269124, 420659664022, 469730790418, 938276901543, 751252303850, 602060496648],
    25 : [816343089399, 222858338746, 764949433484, 56559176014, 661619214672, 696625927118, 272171132851, 253160999433, 865312972695, 149631348620, 228628526980, 152470890537],
    26 : [426879010749, 182864574242, 945179046839, 968380042168, 657250174285, 594691620677, 14042286250, 327677095937, 568841294667, 13341442485, 136194410052, 650428436377],
    27 : [97992674663, 632894996608, 437834492004, 787258347719, 475845875044, 26185312775, 814391564341, 750735865821, 235607693758, 870537062408, 302966230267, 40870872751],
    28 : [1065486639921, 891936427812, 658517810216, 678923381114, 418670692846, 615050987632, 46614619701, 149641946368, 39918315373, 585561982915, 404466269416, 107889966961],
    29 : [679076009883, 964159007894, 677422407637, 346245088596, 341265249232, 917306723404, 432243452749, 750379351247, 857760786239, 836800517668, 482465571896, 101879047553],
    30 : [1030578063132, 515988255884, 768570297510, 410798632831, 120293665571, 643573368555, 941422071136, 341739261795, 1026048412782, 540207485443, 86903704908, 375979712884],
    31 : [461350863446, 139123703559, 916083993354, 697516706217, 371389924679, 848760013987, 1010814195305, 692249787022, 214868875721, 994206915355, 345925284727, 125825555375],
    32 : [402916034213, 777372099912, 171175165055, 955769590438, 388187985499, 1017973797658, 454694938962, 194006218912, 128699876069, 936631256623, 368098960591, 40366316599],
    33 : [938738471722, 384961168092, 253697479997, 461275426518, 910026040846, 976209366339, 312883844438, 30931764020, 337158308077, 58203164478, 310506643447, 30145152072],
    34 : [1048048072498, 812553454986, 365085681999, 119677968622, 391780246905, 36114650468, 338382489329, 1054770487700, 469249181528, 240051474186, 114000495763, 1001810252714],
    35 : [222452582469, 108448489491, 322903465046, 521003899446, 221649327108, 122701747210, 986744196257, 445758823160, 960174800478, 1028979459905, 545203887025, 582740370254],
    36 : [163241913867, 862224374917, 942313378476, 203889951426, 1021058991814, 981963036404, 360037331601, 740309330222, 569553176381, 512193067208, 1008057028659, 373634317782],
    37 : [361816262890, 316017887800, 954809839381, 516848221839, 287385096523, 381007651755, 1004661698083, 196410539470, 179256022922, 37415820366, 40304880728, 661811500378],
    38 : [609192429103, 1054038853800, 148059331518, 219255618821, 559482820348, 250400378662, 155472145311, 959287767547, 636920757614, 285824486846, 870171317692, 984690447797],
    39 : [287361179500, 634627795380, 731042312614, 12866658266, 436365484250, 525186904710, 802580924360, 356136527194, 195707381892, 970288906524, 251130412941, 618685570160],
    40 : [696061330446, 746833130359, 970179328140, 524427268300, 594130989365, 520511801506, 463221260244, 181308867316, 556107111117, 736531762783, 982715187565, 203792007645],
    41 : [554209922295, 582917946444, 508075619875, 25407245616, 76024125346, 452829311503, 490093114330, 910223896170, 361627101191, 854594205456, 703831788188, 30224039075],
    42 : [94883182372, 399904107490, 782193137146, 780311109991, 269648998451, 412878363340, 193015670747, 210191345542, 1089134274033, 58500375373, 117180971069, 693061512476],
    43 : [904940446488, 529583384223, 940785921952, 260818012620, 494327040497, 338297216696, 296111268457, 190998211828, 107048346022, 847912687976, 356643575483, 1011835387367],
    44 : [1097166217621, 460388050617, 852562156328, 286227733904, 772936596103, 688984417009, 660164846751, 1092208857209, 1035901022735, 874770233849, 185843307879, 797854567598],
    45 : [642921812786, 702256768975, 184189093993, 682630880019, 13885773944, 156186976622, 586451957599, 444003786520, 701984539747, 232286163447, 743237154424, 77438774506],
    46 : [613198127703, 875205909653, 841692042440, 604488400195, 803108536829, 490999918946, 172569243912, 33893467246, 1029103230321, 398779024934, 1014715898131, 65375806663],
    47 : [588224728715, 716712063998, 285215940517, 220091244822, 374946959308, 373228166560, 885719763561, 120286079250, 152431592706, 874714319188, 542697306470, 550808190886],
    48 : [945527492012, 685878769358, 334320493213, 534461673027, 983468758535, 377068727639, 992244814384, 155700914010, 439297862200, 562638124007, 683428243362, 979023532772],
    49 : [1066504519724, 916044280291, 108865445418, 791106238174, 340854375925, 771903208435, 14244808658, 191630431096, 569603362919, 942238520564, 996756906747, 540116314294],
    50 : [1006955554615, 235902987784, 133422714792, 174691802764, 41406649879, 750987468997, 852252826246, 235743396920, 575575323733, 753528494204, 652472813389, 575209352396],
    51 : [789617245952, 885420325030, 328377847662, 1023392877234, 420571160370, 620163044464, 747127522970, 481948672871, 373169465158, 529054702225, 572957229644, 584453117732],
    52 : [414527638560, 262219223111, 573944242712, 825605984393, 744483429116, 161363768378, 386978404876, 534294185952, 757851193376, 944144240942, 776226442954, 300181536926],
    53 : [663276480474, 572989934621, 290417316842, 422454355760, 570411022320, 748145262860, 34789008784, 815011192656, 239251401805, 457862456500, 773294603101, 940047359988],
    54 : [515970801348, 934636343333, 815617812551, 988178212587, 415455477553, 553081938805, 412321759288, 1003342648261, 772386059022, 177060386144, 1030569030210, 547562836374],
    55 : [790165108656, 545102066581, 775312203920, 316674622703, 644390840810, 242202903924, 1067576212347, 633852173532, 600728567140, 704321956737, 980135075663, 817321692305],
    56 : [798451333556, 29328750453, 924784121624, 472458665586, 1056056391706, 110640275622, 417459389949, 855621611142, 1070067214212, 843554003207, 153985965961, 919264786391],
    57 : [937605078219, 988824724024, 269591523599, 749574405506, 331324984414, 525114656262, 911070887808, 13328154363, 757156606546, 628609120305, 713514616956, 46779121623],
    58 : [364245452876, 251170535209, 387940711057, 963461223801, 495662843113, 430885735442, 516199082189, 378666671569, 722049630103, 1083439043090, 719918373558, 180255211774],
    59 : [934815328032, 746248850971, 921765569829, 1003824816170, 467702891743, 754131300565, 880717286081, 223038237927, 558657898597, 93862765571, 198718497877, 1083471834745],
    60 : [1047252154079, 1003005317869, 969551673902, 555497643836, 997259398491, 236287237173, 284147536202, 1091397650065, 887739053433, 641934139452, 257245605248, 810811477573],
    61 : [294840527739, 347186690679, 697005411077, 424589463148, 875120225203, 236615169258, 1034680406562, 948243083551, 750224899594, 585492380491, 524626741798, 1033122530418],
    62 : [184346433277, 886323043354, 977181598244, 480940056315, 644737607923, 848136091818, 264661429141, 699028488667, 1081566157991, 465877212766, 1002884125226, 535840759217],
    63 : [514245344459, 500452495989, 284885613135, 487592832874, 1021526183105, 272657337332, 592021984742, 734761362597, 974444341499, 1025445429843, 531048447161, 586060421217],
    'black_turn' : [327440181178]
}

Zobrist_decode = {
        'p': 0,
        'P': 1,
        'r': 2,
        'R': 3,
        'n': 4,
        'N': 5,
        'b': 6,
        'B': 7,
        'q': 8,
        'Q': 9,
        'k': 10,
        'K': 11,
    }

def new_chess_board():
    screen = pygame.display.set_mode(screen_size)
    screen.fill(screen_color)
    block_size = screen_size[0] / 8
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                continue
            pygame.draw.rect(screen, black_block, (i * block_size, j * block_size, block_size, block_size))
    return screen

def make_moves(state, old_pos = (0, 0), new_pos = (0, 0)):
    if state.board[old_pos[0]][old_pos[1]] in black_pieces:

        state.pieces_counting[state.board[new_pos[0]][new_pos[1]]] -= 1

        if state.board[new_pos[0]][new_pos[1]] in white_pieces:
            state.white_pieces_list.remove(new_pos)
        state.black_pieces_list.append(new_pos)
        state.black_pieces_list.remove(old_pos)

        if state.board[old_pos[0]][old_pos[1]] == 'K':
            if old_pos == (4, 0) and new_pos == (6, 0):
                state.board[4][0] = ' '
                state.board[5][0] = 'R'
                state.board[6][0] = 'K'
                state.board[7][0] = ' '
                state.black_pieces_list.remove((4, 0))
                state.black_pieces_list.append((6, 0))
                state.black_pieces_list.append((5, 0))
                state.black_pieces_list.remove((7, 0))
                bk.moved = True
                return 0
            elif old_pos == (4, 0) and new_pos == (2, 0):
                state.board[4][0] = ' '
                state.board[3][0] = 'R'
                state.board[2][0] = 'K'
                state.board[0][0] = ' '
                state.black_pieces_list.remove((4, 0))
                state.black_pieces_list.append((2, 0))
                state.black_pieces_list.append((3, 0))
                state.black_pieces_list.remove((0, 0))
                bk.moved = True
                return 0
            bk.moved = True

        state.board[new_pos[0]][new_pos[1]] = state.board[old_pos[0]][old_pos[1]]
        state.board[old_pos[0]][old_pos[1]] = ' '
        if new_pos[1] == 7 and state.board[new_pos[0]][new_pos[1]] == 'P':
            state.board[new_pos[0]][new_pos[1]] = 'Q'
            state.pieces_counting['Q'] += 1
            state.pieces_counting['P'] -= 1
            return 1
        return 0
    else:
        state.pieces_counting[state.board[new_pos[0]][new_pos[1]]] -= 1

        if state.board[new_pos[0]][new_pos[1]] in black_pieces:
            state.black_pieces_list.remove(new_pos)
        state.white_pieces_list.append(new_pos)
        state.white_pieces_list.remove(old_pos)

        if state.board[old_pos[0]][old_pos[1]] == 'k':
            if old_pos == (4, 7) and new_pos == (6, 7):
                state.board[4][7] = ' '
                state.board[5][7] = 'r'
                state.board[6][7] = 'k' 
                state.board[7][7] = ' '
                for k in state.board:
                    print(k)
                for k in state.white_pieces_list:
                    print(k)
                state.white_pieces_list.remove((4, 7))
                state.white_pieces_list.append((6, 7))
                state.white_pieces_list.append((5, 7))
                state.white_pieces_list.remove((7, 7))
                wk.moved = True
                return 0
            elif old_pos == (4, 7) and new_pos == (2, 7):
                state.board[4][7] = ' '
                state.board[3][7] = 'r'
                state.board[2][7] = 'k'
                state.board[0][7] = ' '
                state.white_pieces_list.remove((4, 7))
                state.white_pieces_list.append((2, 7))
                state.white_pieces_list.append((3, 7))
                state.white_pieces_list.remove((0, 7))
                wk.moved = True
                return 0
            wk.moved = True

        state.board[new_pos[0]][new_pos[1]] = state.board[old_pos[0]][old_pos[1]]
        state.board[old_pos[0]][old_pos[1]] = ' '
        if new_pos[1] == 0 and state.board[new_pos[0]][new_pos[1]] == 'p':
            state.board[new_pos[0]][new_pos[1]] = 'q'
            state.pieces_counting['q'] += 1
            state.pieces_counting['p'] -= 1
            return 1
        return 0
    # piece_list[board[new_pos[0]][new_pos[1]]] -= 1
    # if board[old_pos[0]][old_pos[1]] == 'k':
    #     if old_pos == (4, 7) and new_pos == (6, 7):
    #         board[4][7] = ' '
    #         board[5][7] = 'r'
    #         board[6][7] = 'k' 
    #         board[7][7] = ' '
    #         return 0
    #     elif old_pos == (4, 7) and new_pos == (2, 7):
    #         board[4][7] = ' '
    #         board[3][7] = 'r'
    #         board[2][7] = 'k'
    #         board[0][7] = ' '
    #         return 0
    # if board[old_pos[0]][old_pos[1]] == 'K':
    #     if old_pos == (4, 0) and new_pos == (6, 0):
    #         board[4][0] = ' '
    #         board[5][0] = 'R'
    #         board[6][0] = 'K'
    #         board[7][0] = ' '
    #         return 0
    #     elif old_pos == (4, 0) and new_pos == (2, 0):
    #         board[4][0] = ' '
    #         board[3][0] = 'R'
    #         board[2][0] = 'K'
    #         board[0][0] = ' '
    #         return 0
    # board[new_pos[0]][new_pos[1]] = board[old_pos[0]][old_pos[1]]
    # board[old_pos[0]][old_pos[1]] = ' '
    # if new_pos[1] == 7 and board[new_pos[0]][new_pos[1]] == 'P':
    #     board[new_pos[0]][new_pos[1]] = 'Q'
    #     return 1
    # if new_pos[1] == 0 and board[new_pos[0]][new_pos[1]] == 'p':
    #     board[new_pos[0]][new_pos[1]] = 'q'
    #     return 1

def undo_moves(state, old_pos = (0, 0), new_pos = (0, 0), captured_piece = ' ', promoted = 0):
    if state.board[new_pos[0]][new_pos[1]] in black_pieces:

        state.pieces_counting[captured_piece] += 1

        if captured_piece in white_pieces:
            state.white_pieces_list.append(new_pos)
        state.black_pieces_list.remove(new_pos)
        state.black_pieces_list.append(old_pos)

        if state.board[new_pos[0]][new_pos[1]] == 'K':
            if new_pos == (6, 0) and old_pos == (4, 0):
                state.board[4][0] = 'K'
                state.board[5][0] = ' '
                state.board[6][0] = ' '
                state.board[7][0] = 'R'
                state.black_pieces_list.append((7, 0))
                state.black_pieces_list.remove((6, 0))
                state.black_pieces_list.remove((5, 0))
                state.black_pieces_list.append((4, 0))
                return
            elif new_pos == (2, 0) and old_pos == (4, 0):
                state.board[4][0] = 'K'
                state.board[3][0] = ' '
                state.board[2][0] = ' '
                state.board[0][0] = 'R'
                state.black_pieces_list.append((0, 0))
                state.black_pieces_list.remove((2, 0))
                state.black_pieces_list.remove((3, 0))
                state.black_pieces_list.append((4, 0))
                return
        state.board[old_pos[0]][old_pos[1]] = state.board[new_pos[0]][new_pos[1]]
        state.board[new_pos[0]][new_pos[1]] = captured_piece
        if promoted == 1:
            if new_pos[1] == 7:
                state.board[old_pos[0]][old_pos[1]] = 'P'
                state.pieces_counting['P'] += 1
                state.pieces_counting['Q'] -= 1
    
    else:

        state.pieces_counting[captured_piece] += 1

        if captured_piece in black_pieces:
            state.black_pieces_list.append(new_pos)
        state.white_pieces_list.remove(new_pos)
        state.white_pieces_list.append(old_pos)

        if state.board[new_pos[0]][new_pos[1]] == 'k':
            if new_pos == (6, 7) and old_pos == (4, 7):
                state.board[4][7] = 'k'
                state.board[5][7] = ' '
                state.board[6][7] = ' '
                state.board[7][7] = 'r'
                return
            elif new_pos == (2, 7) and old_pos == (4, 7):
                state.board[4][7] = 'k'
                state.board[3][7] = ' '
                state.board[2][7] = ' '
                state.board[0][7] = 'r'
                return
        state.board[old_pos[0]][old_pos[1]] = state.board[new_pos[0]][new_pos[1]]
        state.board[new_pos[0]][new_pos[1]] = captured_piece
        if promoted == 1:
            if new_pos[1] == 0:
                state.board[old_pos[0]][old_pos[1]] = 'p'
                state.pieces_counting['p'] += 1
                state.pieces_counting['q'] -= 1

    # piece_list[captured_piece] += 1
    # if board[new_pos[0]][new_pos[1]] == 'k':
    #     if new_pos == (6, 7) and old_pos == (4, 7):
    #         board[4][7] = 'k'
    #         board[5][7] = ' '
    #         board[6][7] = ' '
    #         board[7][7] = 'r'
    #         return
    #     elif new_pos == (2, 7) and old_pos == (4, 7):
    #         board[4][7] = 'k'
    #         board[3][7] = ' '
    #         board[2][7] = ' '
    #         board[0][7] = 'r'
    #         return
    # if board[new_pos[0]][new_pos[1]] == 'K':
    #     if new_pos == (6, 0) and old_pos == (4, 0):
    #         board[4][0] = 'K'
    #         board[5][0] = ' '
    #         board[6][0] = ' '
    #         board[7][0] = 'R'
    #         return
    #     elif new_pos == (2, 0) and old_pos == (4, 0):
    #         board[4][0] = 'K'
    #         board[3][0] = ' '
    #         board[2][0] = ' '
    #         board[0][0] = 'R'
    #         return
    # board[old_pos[0]][old_pos[1]] = board[new_pos[0]][new_pos[1]]
    # board[new_pos[0]][new_pos[1]] = captured_piece
    # if promoted == 1:
    #     if new_pos[1] == 7:
    #         board[old_pos[0]][old_pos[1]] = 'P'
    #     else:
    #         board[old_pos[0]][old_pos[1]] = 'p'


def new_board():
    board = [['R', 'P', ' ', ' ', ' ', ' ', 'p', 'r'],
             ['N', 'P', ' ', ' ', ' ', ' ', 'p', 'n'],
             ['B', 'P', ' ', ' ', ' ', ' ', 'p', 'b'],
             ['Q', 'P', ' ', ' ', ' ', ' ', 'p', 'q'],
             ['K', 'P', ' ', ' ', ' ', ' ', 'p', 'k'],
             ['B', 'P', ' ', ' ', ' ', ' ', 'p', 'b'],
             ['N', 'P', ' ', ' ', ' ', ' ', 'p', 'n'],
             ['R', 'P', ' ', ' ', ' ', ' ', 'p', 'r']]
    return board

def is_valid(state, new_pos, old_pos):
    if new_pos[0] < 0 or new_pos[0] > 7 or new_pos[1] < 0 or new_pos[1] > 7:
        return False
    if color[state.board[new_pos[0]][new_pos[1]]] == color[state.board[old_pos[0]][old_pos[1]]]:
        return False
    piece = state.board[old_pos[0]][old_pos[1]]
    # if piece in black_pieces:
    #     if bk.being_checked(board):
    #         if piece == 'P':
    #             if not bp.is_valid(board, old_pos, new_pos):
    #                 return False
    #             temp_board = copy.deepcopy(board)
    #             make_moves(piece_list, temp_board, old_pos, new_pos)
    #             if bk.being_checked(temp_board):
    #                 return False
    #         elif piece == 'R':
    #             if not br.is_valid(board, old_pos, new_pos):
    #                 return False
    #             temp_board = copy.deepcopy(board)
    #             make_moves(piece_list, temp_board, old_pos, new_pos)
    #             if not bk.being_checked(temp_board):
    #                 return False
    #         elif piece == 'N':
    #             if not bn.is_valid(board, old_pos, new_pos):
    #                 return False
    #             temp_board = copy.deepcopy(board)
    #             make_moves(piece_list, temp_board, old_pos, new_pos)
    #             if not bk.being_checked(temp_board):
    #                 return False
    #         elif piece == 'B':
    #             if not bb.is_valid(board, old_pos, new_pos):
    #                 return False
    #             temp_board = copy.deepcopy(board)
    #             make_moves(piece_list, temp_board, old_pos, new_pos)
    #             if not bk.being_checked(temp_board):
    #                 return False
    #         elif piece == 'K':
    #             if not bk.is_valid(board, old_pos, new_pos):
    #                 return False
    #             temp_board = copy.deepcopy(board)
    #             make_moves(piece_list, temp_board, old_pos, new_pos)
    #             if not bk.being_checked(temp_board):
    #                 return False
    #         elif piece == 'Q':
    #             if not bq.is_valid(board, old_pos, new_pos):
    #                 return False
    #             temp_board = copy.deepcopy(board)
    #             make_moves(piece_list, temp_board, old_pos, new_pos)
    #             if not bk.being_checked(temp_board):
    #                 return False
    #         return True
    # else:
    #     if wk.being_checked(board):
    #         if piece == 'p':
    #             if not wp.is_valid(board, old_pos, new_pos):
    #                 return False
    #             temp_board = copy.deepcopy(board)
    #             make_moves(piece_list, temp_board, old_pos, new_pos)
    #             if wk.being_checked(temp_board):
    #                 return False
    #         elif piece == 'r':
    #             if not wr.is_valid(board, old_pos, new_pos):
    #                 return False
    #             temp_board = copy.deepcopy(board)
    #             make_moves(piece_list, temp_board, old_pos, new_pos)
    #             if not wk.being_checked(temp_board):
    #                 return False
    #         elif piece == 'n':
    #             if not wn.is_valid(board, old_pos, new_pos):
    #                 return False
    #             temp_board = copy.deepcopy(board)
    #             make_moves(piece_list, temp_board, old_pos, new_pos)
    #             if not wk.being_checked(temp_board):
    #                 return False
    #         elif piece == 'b':
    #             if not wb.is_valid(board, old_pos, new_pos):
    #                 return False
    #             temp_board = copy.deepcopy(board)
    #             make_moves(piece_list, temp_board, old_pos, new_pos)
    #             if not wk.being_checked(temp_board):
    #                 return False
    #         elif piece == 'k':
    #             if not wk.is_valid(board, old_pos, new_pos):
    #                 return False
    #             temp_board = copy.deepcopy(board)
    #             make_moves(piece_list, temp_board, old_pos, new_pos)
    #             if not wk.being_checked(temp_board):
    #                 return False
    #         elif piece == 'q':
    #             if wq.is_valid(board, old_pos, new_pos):
    #                 return False
    #             temp_board = copy.deepcopy(board)
    #             make_moves(piece_list, temp_board, old_pos, new_pos)
    #             if wk.being_checked(temp_board):
    #                 return False
    #         return True
    if piece == 'p':
        return wp.is_valid(state.board, old_pos, new_pos)
    elif piece == 'r':
        return wr.is_valid(state.board, old_pos, new_pos)
    elif piece == 'n':
        return wn.is_valid(state.board, old_pos, new_pos)
    elif piece == 'b':
        return wb.is_valid(state.board, old_pos, new_pos)
    elif piece == 'k':
        return wk.is_valid(state.board, old_pos, new_pos)
    elif piece == 'q':
        return wq.is_valid(state.board, old_pos, new_pos)
    elif piece == 'P':
        return bp.is_valid(state.board, old_pos, new_pos)
    elif piece == 'R':
        return br.is_valid(state.board, old_pos, new_pos)
    elif piece == 'N':
        return bn.is_valid(state.board, old_pos, new_pos)
    elif piece == 'B':
        return bb.is_valid(state.board, old_pos, new_pos)
    elif piece == 'K':
        return bk.is_valid(state.board, old_pos, new_pos)
    elif piece == 'Q':
        return bq.is_valid(state.board, old_pos, new_pos)
    return True

class State:
    def __init__(self):
        self.board = new_board()
        self.pieces_counting = {
            'p': 8,
            'r': 2,
            'n': 2,
            'b': 2,
            'k': 1,
            'q': 1,
            'P': 8,
            'R': 2,
            'N': 2,
            'B': 2,
            'K': 1,
            'Q': 1,
            ' ': 32,
        }
        self.black_pieces_list = [(0, 0), (0, 1),
                                  (1, 0), (1, 1),
                                  (2, 0), (2, 1),
                                  (3, 0), (3, 1),
                                  (4, 0), (4, 1),
                                  (5, 0), (5, 1),
                                  (6, 0), (6, 1),
                                  (7, 0), (7, 1)]
        self.white_pieces_list = [(0, 6), (0, 7),
                                  (1, 6), (1, 7),
                                  (2, 6), (2, 7),
                                  (3, 6), (3, 7),
                                  (4, 6), (4, 7),
                                  (5, 6), (5, 7),
                                  (6, 6), (6, 7),
                                  (7, 6), (7, 7)]
        self.black_position_bitboard = 217020518514230019
        self.white_position_bitboard = 13889313184910721216
        self.black_available_takes_bitboard = 289360691352306692
        self.white_available_takes_bitboard = 2314885530818453536