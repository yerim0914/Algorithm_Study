def solution(phone_book):
    answer = True
    phone_book.sort(key=lambda x: (x, len(x)))
    for i in range(0, len(phone_book)-1):
        for j in range(i+1, len(phone_book)):
            if i != j and len(phone_book[i]) < len(phone_book[j]):
                if phone_book[j].startswith(phone_book[i]):
                    answer = False
                    break
    return answer

print(solution(["119", "97674223", "1195524421"]))


def solution(phone_book):
    answer = True
    phone_book.sort(key=lambda x: (x, len(x)))
    for i in range(0, len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]):
                    answer = False
                    break
    return answer