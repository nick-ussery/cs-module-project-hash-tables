def no_dups(s):
    # Your code here
    s = s.lower()
    words = s.split()
    count = []
    for i in words:
        if i not in count:
            count.append(i)
    finished_list = ''
    for i in range(len(count)):
        if len(finished_list) == 0:
            finished_list = count[i]
        else:
            finished_list = finished_list + " " + count[i]
    print(finished_list)
    return finished_list


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
