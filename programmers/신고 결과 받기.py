def solution(id_list, report, k):
    answer = []
    dict = {}
    a = []
    b = []
    for i in range(0, len(report)):
        if report[0:i+1].count(report[i]) >= 2:
            break
        a.append(report[i].split(' ')[0])
        b.append(report[i].split(' ')[1])
    for i in id_list:
        dict[i] = 0
    for i in range(0, len(id_list)):
        if b.count(id_list[i]) >= k:
            lis = [k for k, ele in enumerate(b) if ele == id_list[i]]
            for j in lis :
                dict[a[j]] += 1
    print(dict.values())
    answer = list(dict.values())
    return answer

solution(["muzi", "frodo", "apeach", "neo", "neoneo"],
["frodo muzi","neoneo muzi"], 2)
# solution(["con", "ryan"], ["con ryan", "ryan con", "ryan con", "ryan con"], 3)