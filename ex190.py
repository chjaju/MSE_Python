#apart리스트를 정의한다.
apart = [ [101, 102], [201, 202], [301, 302] ]
#for문을 써서 apart리스트 안에 리스트 각각을 층으로 나눈다. 그후 다시 for문을 써서 각층에 있는 것들을 집으로 한다.
for 층 in apart:
    for 집 in 층:
        #정의한 집을 "호"와 함께 프린트 한다.
        print(집, "호")
#모든 층이 끝났으므로 "-----"를 프린트한다.
print("-----")
#정답
#101 호
#102 호
#201 호
#202 호
#301 호
#302 호
#-----