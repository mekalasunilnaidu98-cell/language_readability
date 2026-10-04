import re,sys,json
def syll(w): return max(1,len(re.findall(r'[aeiouy]+',w.lower())))
def score(t):
 s=max(1,len(re.findall(r'[.!?]+',t))); w=re.findall(r'[A-Za-z]+',t); n=max(1,len(w)); y=sum(syll(x) for x in w); f=206.835-1.015*n/s-84.6*y/n
 return {'words':n,'sentences':s,'flesch_reading_ease':round(f,1),'grade_estimate':round(0.39*n/s+11.8*y/n-15.59,1)}
if __name__=='__main__': print(json.dumps(score(open(sys.argv[1]).read() if len(sys.argv)>1 else input('Text: ')),indent=2))