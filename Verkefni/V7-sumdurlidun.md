# Verkefni 7

### Verkefnalýsing 

- Ritstjóri getur skráð sig inn á vefsíðu (login user)
- Þar getur hann búið til nýjar færslur (create posts)
- Ritstjóri getur eytt eigin póstum (delete posts)
- Ritstjóri getur skráð sig út af vefsíðunni (logout user)
- Allir geta lesið pistlana sem ritstjóri skrifar

### Sundurliðun

#### Firebase gagnagunnur (aðeins ritstjóri hefur aðgang)

Í gagnagrunninum eru 2 töflur

1. admin
    * user
    * psw
2. posts
    * title
    * text
    * image
    * datetime
    * editor

### Templates (vefsíður)

1. index
   * Hér birtast allir póstar úr gagnagrunni (_read only_)
2. login
   * ritstjóri getur skráð sig inn á /editor með _session login_
3. editor (lokuð síða)
   * editor/newpost - ritsjóri getur skráð nýja pósta
   * editor/deletepost - ritsjóri getur eytt pósti úr gagnagrunninum

### Templates tilkynningar, geta verið nánast þær sömu og í 6. verkefni
