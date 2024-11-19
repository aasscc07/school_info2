import time


label = ["하수","중수","고수"]

re_time = [0,0,0]


def trans_S_time(Stime):
    T_time_0 = Stime / 3600
    T_time_1 = ((Stime) % 3600) / 60
    T_time_2 = ((Stime) % 3600) % 60

    return [T_time_0,T_time_1,T_time_2]


    
    

while True:
    state = int(input(" 시작 : 1 , 종류 : 2"))
    if state == 1:
        st = time.time()

        temp = input("공부중...(종류 하려면 아무키나 누르세요)")
        et = time.time()


        dt = et - st

        

        if dt > 3600:
            print(f"당신은 {label[0]}입니다. ")
        

        

        
    elif state == 2:
        exit()
    else:
        "다시 입려해 주세요"
        continue
