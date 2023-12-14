from bardapi import BardCookies

cookie_dict = {
    "__Secure-1PSID": "__update__your__cookie__",
    "__Secure-1PSIDTS": "__update__your__cookie__",
}

while True:
    q = input("Query:  ")
    if q in ["q", ""] :
        print("<quit>")
        break
    bard = BardCookies(cookie_dict=cookie_dict)
    response = bard.get_answer(q)
    print(response['content'] + '\n')
