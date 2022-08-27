def notas(*valor, sit=False):
   r = dict()
   r ['total'] = len(valor)
   r ['maior'] = max(valor)
   r ['menor'] = min(valor)
   r ['media'] = sum(valor)/len(valor)
#acima é importante

   if r ['media'] >= 7:
       r['situacao'] = 'Boa'
   elif  r ['media'] >= 5:
       r['situacao'] = 'OK fi'
   else:
       r['situacao'] = 'VAi se lascar'


   return r

#principa
resp = notas(10,10,10,10, sit= True)
print(resp)





