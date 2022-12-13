from functools import cmp_to_key

f = [x for x in open("input.txt").read().strip().split('\n\n')]
p1List = [x.split('\n') for x in f]

p2List = []
for p in p1List: p2List.extend(p)
p2List.append('[[2]]')
p2List.append('[[6]]')


def compare(left, right):
    ltype, rtype = type(left), type(right)

    try:
        if ltype == int and rtype == int:
            if left > right:
                return False
            if left < right:
                return True
            return None
        if ltype == list and rtype == list:
            for i in range(len(left)):
                rez = compare(left[i], right[i])
                if rez is not None: return rez
            if range(len(left)) == range(len(right)):
                return None
            else:
                return True

        if ltype == list and rtype == int:
            rez = compare(left, [right])
            if rez != None: return rez
        if ltype == int and rtype == list:
            rez = compare([left], right)
            if rez != None: return rez
        return True
    except Exception as inst:
        if len(left) < len(right):
            return True
        else:
            return False


count = 0
for idx, pair in enumerate(p1List):
    if compare(eval(pair[0]), eval(pair[1])):
        count += idx + 1
print('p1:', count)

p2List = sorted(p2List, key=cmp_to_key(lambda a, b: -1 if compare(eval(a), eval(b)) else 1))
i1 = p2List.index('[[2]]') + 1
i2 = p2List.index('[[6]]') + 1
print('p2:', i1 * i2)
