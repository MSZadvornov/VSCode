text = input()
count_gl = 0
count_sgl= 0
gl= "eyioau"
sgl = "qwrtpsdfghjklzxcvbnm"
for i in text:
    if i in gl:     
        count_gl +=1
    elif i in sgl:
        count_sgl +=1
print(count_sgl,count_gl)


