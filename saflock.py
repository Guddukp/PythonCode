
def sum_code():
    if d['one']+d['two']+d['thr']+d['four']+d['five']==30:
        return True

def password_code(n):
    if d['five']+d['thr']==14 and d['two']*2-1==d['one'] and d['two']+1==d['four'] and d['thr']+d['two']==10 and sum_code():
        return True
for code in range(0,100000):
    code = str(code).zfill(5)
    d={}
    d['one']=int(code[0])
    d['two']=int(code[1])
    d['thr']=int(code[2])
    d['four']=int(code[3])
    d['five']=int(code[4])
    if password_code(code):
        print(code)

 
