#todos os times
times = ('flamengo','palmeiras','bragantino','cruzeiro','fluminense','internacional','bahia', 'botafogo','ceara','sao paulo', 'vasco','corinthians','juventude','mirassol','fortaleza','vitoria','atletico-MG','gremio','santos','sport')
top_5 = times[0:5] #os primeiros 5
ultimos_4 = times[-5:-1] #os ultimos 4
alfabetico = tuple(sorted(times)) #ordem alfabetica
pos = times.index('bahia')#onde esta bahia?
print('=-' * 30)
print(f'os times do brasileirao sao: {times}')
print('=-' * 30)
print(f'os primeiros 5 times sao: {top_5}. e os ultimos 4 sao: {ultimos_4}.')
print('=-' * 30)
print(f'os times em ordem alfabetica: {alfabetico}')
print('=-' * 30)
print(f'bahia está em {pos}º')
