import streamlit as st
import random

# פונקציה שבודקת אם כל הספרות שונות
def shonot(mispar):
    return len(mispar) == len(set([c for c in mispar]))

while True:
    sod = ''.join( [str(random.randint(0,9)) for _ in range(4)] )     # range טווח
    if shonot(sod):
        break
#st.write('סוד ', sod)
mone_nihushim = 0

nihush = st.text_input('ניחוש שלך 4 ספרות  ')

if not nihush.isnumeric() or len(nihush) != 4:
    st.write('!!!ביקשתי 4 ספרות')
else:
    mone_nihushim = mone_nihushim + 1
    
    # בדיקה לניחוש נכון
    if nihush == sod:
        st.write('!כל הכבוד')
        st.write('השתמשת ב ', mone_nihushim, 'ניחושים')
    
    parot = 0
    shvarim = 0

    for i, n in enumerate(nihush):    # תמספר
        for j, s in enumerate(sod):
            if n == s:
                if i == j:
                    shvarim = shvarim +1
                else:                       # אחרת
                    parot = parot+1

    st.write('פרות ', parot)
    st.write('שוורים ', shvarim)
