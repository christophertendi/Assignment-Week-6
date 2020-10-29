diction = {}
f = open('/Users/yantysumirkan/Desktop/Assignment Week 6/ebook.txt','r',encoding='utf-8')
txt = f.read().split()
new_txt = []
for word in txt:
    w1=word.strip('!.:;,?-/_$%()').lower()
    new_txt.append(w1)


def hapax(txt):
    for word in txt:
        if word in diction:
            diction[word] += 1
        else:
            diction[word] = 1
    hapaxes=[]
    for word,count in diction.items():
        if count==1:
            hapaxes.append(word)
    return hapaxes

print(hapax(new_txt))
f.close()