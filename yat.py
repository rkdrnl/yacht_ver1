import random
import time

game = input("게임을 시작하시려면 엔터키를 누르십시오 ㅣ 설명을 보시려면 '설명'을 입력하십시오\n")

 
while (game != ""):
    
    if (game == "설명"):
    
        game = input("엔터키를 누르면 게임이 시작됩니다")
    
    elif (game != "" or game != "설명"):
        print("잘못된 입력입니다")
        game = input("게임을 시작하시려면 엔터키를 누르십시오 ㅣ 설명을 보시려면 '설명'을 입력하십시오\n")

p1_score = 0
p2_score = 0

p1_subtotal = 0
p2_subtotal = 0

p1_score_select_1 = 0
p1_score_select_2 = 0
p1_score_select_3 = 0
p1_score_select_4 = 0
p1_score_select_5 = 0
p1_score_select_6 = 0
p1_score_select_7 = 0
p1_score_select_8 = 0
p1_score_select_9 = 0
p1_score_select_10 = 0
p1_score_select_11 = 0
p1_score_select_12 = 0

p2_score_select_1 = 0
p2_score_select_2 = 0
p2_score_select_3 = 0
p2_score_select_4 = 0
p2_score_select_5 = 0
p2_score_select_6 = 0
p2_score_select_7 = 0
p2_score_select_8 = 0
p2_score_select_9 = 0
p2_score_select_10 = 0
p2_score_select_11 = 0
p2_score_select_12 = 0

score_count = 1

#*********************************************************************************************************************************************************



while (score_count <= 12):                                                #점수가 전부 지정될때까지 반복


    D1 = random.randrange(1,7)                                             #주사위 숫자 부여
    D2 = random.randrange(1,7)
    D3 = random.randrange(1,7)
    D4 = random.randrange(1,7)
    D5 = random.randrange(1,7)


    rall = -1
    count = 1                                                            #주사위를 다시 돌린 횟수

    while (rall != 3):

        KD1 = 0                                                            #주사위의 킵확인
        KD2 = 0
        KD3 = 0
        KD4 = 0
        KD5 = 0

        keep = -1
        keepcount = 0

        if (count <= 2):

            print(D1,D2,D3,D4,D5,sep = "ㅣ")
            rall = int(input("다시 굴리기 - 1 ㅣ 킵 - 2 ㅣ 점수 지정 - 3\n"))

            if (rall == 2):    #킵하기

                while (keep != 0 and keepcount <= 4):                                                               #킵확인

                    keep = int(input("킵 - 주사위 순번 입력 ㅣ 킵 취소 - 주사위 순번 입력 ㅣ 다시 굴리기 - 0\n"))

                    if (keep == 1 and KD1 == 0):
                        KD1 = 1
                        keep = -1
                        keepcount += 1

                        print("킵이 되었습니다")

                    elif (keep == 1 and KD1 == 1):
                        KD1 = 0
                        keep = -1
                        keepcount -= 1

                        print("킵이 취소되었습니다")

                    if (keep == 2 and KD2 == 0):
                        KD2 = 1
                        keep = -1
                        keepcount += 1

                        print("킵이 되었습니다")

                    elif (keep == 2 and KD2 == 1):
                        KD2 = 0
                        keep = -1
                        keepcount -= 1

                        print("킵이 취소되었습니다")

                    if (keep == 3 and KD3 == 0):
                        KD3 = 1
                        keep = -1
                        keepcount += 1

                        print("킵이 되었습니다")

                    elif (keep == 3 and KD3 == 1):
                        KD3 = 0
                        keep = -1
                        keepcount -= 1

                        print("킵이 취소되었습니다")

                    if (keep == 4 and KD4 == 0):
                        KD4 = 1
                        keep = -1
                        keepcount += 1

                        print("킵이 되었습니다")

                    elif (keep == 4 and KD4 == 1):
                        KD4 = 0
                        keep = -1
                        keepcount -= 1

                        print("킵이 취소되었습니다")

                    if (keep == 5 and KD5 == 0):
                        KD5 = 1
                        keep = -1
                        keepcount += 1

                        print("킵이 되었습니다")

                    elif (keep == 5 and KD5 == 1):
                        KD5 = 0
                        keep = -1
                        keepcount -= 1

                        print("킵이 취소되었습니다")


            if (rall == 1 or rall == 2):

                if(KD1 == 0):                                    #주사위 다시 굴리기
                    D1 = random.randrange(1,7)

                if(KD2 == 0):
                    D2 = random.randrange(1,7)

                if(KD3 == 0):
                    D3 = random.randrange(1,7)

                if(KD4 == 0):
                    D4 = random.randrange(1,7)

                if(KD5 == 0):
                    D5 = random.randrange(1,7)

            if (rall != 1 and rall != 2 and rall != 3):    #잘못된 입력 감지
                print("잘못된 입력입니다")

                count -= 1

            count += 1

        else:
            rall = 3

    print(D1,D2,D3,D4,D5,sep = "ㅣ")


    dices = [D1,D2,D3,D4,D5]

    score_select = 0                                #점수 선택 확인

    if (p1_score_select_1 == 0):
        ones = dices.count(1)

    if (p1_score_select_2 == 0):
        twos = 2*dices.count(2)

    if (p1_score_select_3 == 0):
        threes = 3*dices.count(3)

    if (p1_score_select_4 == 0):
        fours = 4*dices.count(4)

    if (p1_score_select_5 == 0):
        fives = 5*dices.count(5)

    if (p1_score_select_6 == 0):
        sixes = 6*dices.count(6)

    if (p1_score_select_7 == 0):
        choice = 0
        for i in dices:
            choice += i

    if (p1_score_select_8 == 0):
        fc = 0                                            #fourcard

        if (dices.count(1) >= 4):
            for k in dices:
                fc += k

        elif (dices.count(2) >= 4):
            for k in dices:
                fc += k

        elif (dices.count(3) >= 4):
            for k in dices:
                fc += k

        elif (dices.count(4) >= 4):
            for k in dices:
                fc += k

        elif (dices.count(5) >= 4):
            for k in dices:
                fc += k
            
        elif (dices.count(6) >= 4):
            for k in dices:
                fc += k

    if (p1_score_select_9 == 0):
        fh = 0                                                #FullHouse
        j = 1
        while (j <= 6):
            
            if (dices.count(j) == 2):

                if(dices.count(j-5) == 3):

                    for k in dices:
                        fh += k

                elif(dices.count(j-4) == 3):

                    for k in dices:
                        fh += k

                elif(dices.count(j-3) == 3):

                    for k in dices:
                        fh += k

                elif(dices.count(j-2) == 3):

                    for k in dices:
                        fh += k

                elif(dices.count(j-1) == 3):

                    for k in dices:
                        fh += k

                elif(dices.count(j+1) == 3):

                    for k in dices:
                        fh += k

                elif(dices.count(j+2) == 3):

                    for k in dices:
                        fh += k

                elif(dices.count(j+3) == 3):

                    for k in dices:
                        fh += k

                elif(dices.count(j+4) == 3):

                    for k in dices:
                        fh += k

                elif(dices.count(j+5) == 3):

                    for k in dices:
                        fh += k
                        
            elif (p1_score_select_12 == 1 and dices.count(j) == 5):
                    
                    fh += 5 * j

            j += 1

    if (p1_score_select_10 == 0):
        ss = 0                                                #Small Straight
        l = 1

        while (l <= 3):

            if (0 < dices.count(l) <= 2 and 0 < dices.count(l+1) <= 2 and 0 < dices.count(l+2) <= 2 and 0 < dices.count(l+3) <= 2):

                ss = 15

            l += 1

    if (p1_score_select_11 == 0):
        bs = 0                                                #Big Straight
        n = 1

        while (n <= 2):

            if (0 < dices.count(n) <= 2 and 0 < dices.count(n+1) <= 2 and dices.count(n+2) <= 2 and 0 < dices.count(n+3) <= 2 and 0 < dices.count(n+4) <= 2):

                bs = 30

            n += 1

    if (p1_score_select_12 == 0):
        yacht = 0
        p = 1

        while (p <= 6):

            if (dices.count(p) == 5):

                yacht = 50

            p += 1


    while (score_select == 0):

        score_input = int(input("1.Ones(%d) ㅣ 2.Twos(%d) ㅣ 3.Threes(%d) ㅣ 4.Fours(%d) ㅣ 5.Fives(%d) ㅣ 6.Sixes(%d) ㅣ 7.Choice(%d) ㅣ 8.Fourcard(%d) ㅣ 9.FullHouse(%d) ㅣ 10.S.Straight(%d) ㅣ 11.B.Straight(%d) ㅣ 12.Yacht(%d)\n[subtotal - %d]\n"%(ones,twos,threes,fours,fives,sixes,choice,fc,fh,ss,bs,yacht,p1_subtotal)))

        if (score_input == 1 and p1_score_select_1 == 0):                                        #점수 선택
            p1_score += ones
            score_select = 1
            p1_score_select_1 = 1
            p1_subtotal += ones

        elif (score_input == 2 and p1_score_select_2 == 0):
            p1_score += twos
            score_select = 1
            p1_score_select_2 = 1
            p1_subtotal += twos

        elif (score_input == 3 and p1_score_select_3 == 0):
            p1_score += threes
            score_select = 1
            p1_score_select_3 = 1
            p1_subtotal += threes

        elif (score_input == 4 and p1_score_select_4 == 0):
            p1_score += fours
            score_select = 1
            p1_score_select_4 = 1
            p1_subtotal += fours

        elif (score_input == 5 and p1_score_select_5 == 0):
            p1_score += fives
            score_select = 1
            p1_score_select_5 = 1
            p1_subtotal += fives

        elif (score_input == 6 and p1_score_select_6 == 0):
            p1_score += sixes
            score_select = 1
            p1_score_select_6 = 1
            p1_subtotal += sixes


        elif (score_input == 7 and p1_score_select_7 == 0):
            p1_score += choice
            score_select = 1
            p1_score_select_7 = 1

        elif (score_input == 8 and p1_score_select_8 == 0):
            p1_score += fc
            score_select = 1
            p1_score_select_8 = 1

        elif (score_input == 9 and p1_score_select_9 == 0):
            p1_score += fh
            score_select = 1
            p1_score_select_9 = 1

        elif (score_input == 10 and p1_score_select_10 == 0):
            p1_score += ss
            score_select = 1
            p1_score_select_10 = 1

        elif (score_input == 11 and p1_score_select_11 == 0):
            p1_score += bs
            score_select = 1
            p1_score_select_11 = 1

        elif (score_input == 12 and p1_score_select_12 == 0):
            p1_score += yacht
            score_select = 1
            p1_score_select_12 = 1

        else:
            print("잘못된 입력 또는 이미 지정된 점수입니다")
            
            
        if (p1_subtotal >= 63):                                                    #1~6족보 합계가 63점 이상일떄 35점 추가
            p1_score += 35




    print ("P1 점수 : %d ㅣ P2 점수 : %d"%(p1_score,p2_score)) 


    #********************************************************************************************************************************************


    D1 = random.randrange(1,7)                                               #주사위 숫자 부여
    D2 = random.randrange(1,7)
    D3 = random.randrange(1,7)
    D4 = random.randrange(1,7)
    D5 = random.randrange(1,7)


    rall = -1
    count = 1                                                            #주사위를 다시 돌린 횟수

    while (rall != 3):

        KD1 = 0                                                            #주사위의 킵확인
        KD2 = 0
        KD3 = 0
        KD4 = 0
        KD5 = 0

        keep = -1
        keepcount = 0

        if (count <= 2):

            print(D1,D2,D3,D4,D5,sep = "ㅣ")
            rall = int(input("다시 굴리기 - 1 ㅣ 킵 - 2 ㅣ 점수 지정 - 3\n"))

            if (rall == 2):    #킵하기

                while (keep != 0 and keepcount <= 4):                                                               #킵확인

                    keep = int(input("킵 - 주사위 순번 입력 ㅣ 킵 취소 - 주사위 순번 입력 ㅣ 다시 굴리기 - 0\n"))

                    if (keep == 1 and KD1 == 0):
                        KD1 = 1
                        keep = -1
                        keepcount += 1

                        print("킵이 되었습니다")

                    elif (keep == 1 and KD1 == 1):
                        KD1 = 0
                        keep = -1
                        keepcount -= 1

                        print("킵이 취소되었습니다")

                    if (keep == 2 and KD2 == 0):
                        KD2 = 1
                        keep = -1
                        keepcount += 1

                        print("킵이 되었습니다")

                    elif (keep == 2 and KD2 == 1):
                        KD2 = 0
                        keep = -1
                        keepcount -= 1

                        print("킵이 취소되었습니다")

                    if (keep == 3 and KD3 == 0):
                        KD3 = 1
                        keep = -1
                        keepcount += 1

                        print("킵이 되었습니다")

                    elif (keep == 3 and KD3 == 1):
                        KD3 = 0
                        keep = -1
                        keepcount -= 1

                        print("킵이 취소되었습니다")

                    if (keep == 4 and KD4 == 0):
                        KD4 = 1
                        keep = -1
                        keepcount += 1

                        print("킵이 되었습니다")

                    elif (keep == 4 and KD4 == 1):
                        KD4 = 0
                        keep = -1
                        keepcount -= 1

                        print("킵이 취소되었습니다")

                    if (keep == 5 and KD5 == 0):
                        KD5 = 1
                        keep = -1
                        keepcount += 1

                        print("킵이 되었습니다")

                    elif (keep == 5 and KD5 == 1):
                        KD5 = 0
                        keep = -1
                        keepcount -= 1

                        print("킵이 취소되었습니다")


            if (rall == 1 or rall == 2):

                if(KD1 == 0):                                    #주사위 다시 굴리기
                    D1 = random.randrange(1,7)

                if(KD2 == 0):
                    D2 = random.randrange(1,7)

                if(KD3 == 0):
                    D3 = random.randrange(1,7)

                if(KD4 == 0):
                    D4 = random.randrange(1,7)

                if(KD5 == 0):
                    D5 = random.randrange(1,7)

            if (rall != 1 and rall != 2 and rall != 3):    #잘못된 입력 감지
                print("잘못된 입력입니다")

                count -= 1

            count += 1

        else:
            rall = 3

    print(D1,D2,D3,D4,D5,sep = "ㅣ")


    dices = [D1,D2,D3,D4,D5]

    score_select = 0                                #점수 선택 확인

    if (p2_score_select_1 == 0):
        ones = dices.count(1)

    if (p2_score_select_2 == 0):
        twos = 2*dices.count(2)

    if (p2_score_select_3 == 0):
        threes = 3*dices.count(3)

    if (p2_score_select_4 == 0):
        fours = 4*dices.count(4)

    if (p2_score_select_5 == 0):
        fives = 5*dices.count(5)

    if (p2_score_select_6 == 0):
        sixes = 6*dices.count(6)

    if (p2_score_select_7 == 0):
        choice = 0
        for i in dices:
            choice += i

    if (p2_score_select_8 == 0):
        fc = 0                                            #fourcard

        if (dices.count(1) >= 4):
            fc = dices.count(1) * 1

        elif (dices.count(2) >= 4):
            fc = dices.count(2) * 2

        elif (dices.count(3) >= 4):
            fc = dices.count(3) * 3

        elif (dices.count(4) >= 4):
            fc = dices.count(4) * 4

        elif (dices.count(5) >= 4):
            fc = dices.count(5) * 5

    if (p2_score_select_9 == 0):
        fh = 0                                                #FullHouse
        j = 1
        while (j <= 6):

            if (dices.count(j) == 2):

                if(dices.count(j-5) == 3):

                    for k in dices:
                        fh += k

                elif(dices.count(j-4) == 3):

                    for k in dices:
                        fh += k

                elif(dices.count(j-3) == 3):

                    for k in dices:
                        fh += k

                elif(dices.count(j-2) == 3):

                    for k in dices:
                        fh += k

                elif(dices.count(j-1) == 3):

                    for k in dices:
                        fh += k

                elif(dices.count(j+1) == 3):

                    for k in dices:
                        fh += k

                elif(dices.count(j+2) == 3):

                    for k in dices:
                        fh += k

                elif(dices.count(j+3) == 3):

                    for k in dices:
                        fh += k

                elif(dices.count(j+4) == 3):

                    for k in dices:
                        fh += k

                elif(dices.count(j+5) == 3):

                    for k in dices:
                        fh += k

            j += 1

    if (p2_score_select_10 == 0):
        ss = 0                                                #Small Straight
        l = 1

        while (l <= 3):

            if (0 < dices.count(l) <= 2 and 0 < dices.count(l+1) <= 2 and 0 < dices.count(l+2) <= 2 and 0 < dices.count(l+3) <= 2):

                ss = 15

            l += 1

    if (p2_score_select_11 == 0):
        bs = 0                                                #Big Straight
        n = 1

        while (n <= 2):

            if (0 < dices.count(n) <= 2 and 0 < dices.count(n+1) <= 2 and dices.count(n+2) <= 2 and 0 < dices.count(n+3) <= 2 and 0 < dices.count(n+4) <= 2):

                bs = 30

            n += 1

    if (p2_score_select_12 == 0):
        yacht = 0
        p = 1

        while (p <= 6):

            if (dices.count(p) == 5):

                yacht = 50

            p += 1
    
    while (score_select == 0):

        score_input = int(input("1.Ones(%d) ㅣ 2.Twos(%d) ㅣ 3.Threes(%d) ㅣ 4.Fours(%d) ㅣ 5.Fives(%d) ㅣ 6.Sixes(%d) ㅣ 7.Choice(%d) ㅣ 8.Fourcard(%d) ㅣ 9.FullHouse(%d) ㅣ 10.S.Straight(%d) ㅣ 11.B.Straight(%d) ㅣ 12.Yacht(%d)\n[subtotal - %d]\n"%(ones,twos,threes,fours,fives,sixes,choice,fc,fh,ss,bs,yacht,p2_subtotal)))
        
        if (score_input == 1 and p2_score_select_1 == 0):                                        #점수 선택
            p2_score += ones
            score_select = 1
            p2_score_select_1 = 1
            p2_subtotal += ones

        elif (score_input == 2 and p2_score_select_2 == 0):
            p2_score += twos
            score_select = 1
            p2_score_select_2 = 1
            p2_subtotal += twos

        elif (score_input == 3 and p2_score_select_3 == 0):
            p2_score += threes
            score_select = 1
            p2_score_select_3 = 1
            p2_subtotal += threes

        elif (score_input == 4 and p2_score_select_4 == 0):
            p2_score += fours
            score_select = 1
            p2_score_select_4 = 1
            p2_subtotal += fours

        elif (score_input == 5 and p2_score_select_5 == 0):
            p2_score += fives
            score_select = 1
            p2_score_select_5 = 1
            p2_subtotal += fives

        elif (score_input == 6 and p2_score_select_6 == 0):
            p2_score += sixes
            score_select = 1
            p2_score_select_6 = 1
            p2_subtotal += sixes

        elif (score_input == 7 and p2_score_select_7 == 0):
            p2_score += choice
            score_select = 1
            p2_score_select_7 = 1

        elif (score_input == 8 and p2_score_select_8 == 0):
            p2_score += fc
            score_select = 1
            p2_score_select_8 = 1

        elif (score_input == 9 and p2_score_select_9 == 0):
            p2_score += fh
            score_select = 1
            p2_score_select_9 = 1

        elif (score_input == 10 and p2_score_select_10 == 0):
            p2_score += ss
            score_select = 1
            p2_score_select_10 = 1

        elif (score_input == 11 and p2_score_select_11 == 0):
            p2_score += bs
            score_select = 1
            p2_score_select_11 = 1

        elif (score_input == 12 and p2_score_select_12 == 0):
            p2_score += yacht
            score_select = 1
            p2_score_select_12 = 1

        else:
            print("잘못된 입력 또는 이미 지정된 점수입니다")

        if (p2_subtotal >= 63):                                                    #1~6족보 합계가 63점 이상일떄 35점 추가
            p2_score += 35


    print ("P1 점수 : %d ㅣ P2 점수 : %d"%(p1_score,p2_score)) 

    score_count += 1
    
    
#*********************************************************************************************************************************************


print(".\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n")

if (p1_score > p2_score):
    print("player 1 승리")

elif (p1_score == p2_score):
    print("동점")

elif (p1_score < p2_score):
    print("player 2 승리")
