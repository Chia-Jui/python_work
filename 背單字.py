dict ={'天文學':'astronomy', '衛星':'satellite', '隕石':'meteorite', '星座':'constellation', '流星':'meteor', '彗星':'comet', '行星':'planet', '小行星':'asteroid', '輻射':'radiation', '天文台':'observatory', '紅外線':'infrared ray', '紫外線':'ultraviolet ray', '水星':'Mercury','金星':'Venus', '火星':'Mars', '木星':'Jupiter', '土星':'Saturn', '天王星':'Uranus', '海王星':'Neptune', '矮星':'dwarf'}

print("請輸入正確的英文翻譯:")
for i in dict:
    print(i,":")
    k=1
    while True:
        answer=input()
        if answer==dict[i]:
            print("答對了!")
            break
        else:
            print("第{0:d}次答錯。\n再來一次。".format(k))
            k+=1
        
print("恭喜背完全部單字!")
