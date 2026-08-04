cities =["dhaka","barishal","khulna","rajshahi"]
heros = ["shakib khan","siam","afran niso"]


def cal_len(list):
    print(len(list))

    def cal_list(list):
        for iteam in list:
            print(iteam,end=" ")


    cal_list(heros)
cal_len(cities)