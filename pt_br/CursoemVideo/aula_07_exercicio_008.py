print('Este programa converte uma medida em metros \npara mm, cm, dm, dam, hm e km')
m = float(input('Digite o valor em metros: '))
km = m/1000
hm = m/100
dam = m/10
dm = m*10
cm = m*100
mm = m*1000
print('A medida de {} metros equivale a:'.format(m))
print(' {} km \n {} hm \n {} dam \n {:.0f} dm \n {:.0f} cm \n {:.0f} mm'.format(km, hm, dam, dm, cm, mm))
