def solution(phone_book):
    answer = True
    phone_book.sort(key=lambda x: (x, len(x)))
    print(phone_book)
    for i in range(0, len(phone_book)-1):
        for j in range(i+1, len(phone_book)-1):
            if i != j:
                if (phone_book[i].startswith(phone_book[j]) or phone_book[j].startswith(phone_book[i])):
                    answer = False
                    break
    # for i in range(0, len(phone_book)-1):
    #     for j in range(len(phone_book)-1, 1, -1):
    #         if i != j:
    #             if phone_book[i] in phone_book[j]:
    #                 answer = False
    #                 break
    print(answer)
    return answer

solution(["119", "1195524421", "97674223"])