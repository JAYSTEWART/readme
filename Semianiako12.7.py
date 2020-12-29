money=int(input('Введите сумму депозита:'))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit=per_cent['ТКБ']*money , per_cent['СКБ']*money , per_cent['ВТБ']*money , per_cent['СБЕР']*money
print('Депозит:',deposit, """\n""""Максимальная сумма, которую вы можете заработать -",max(deposit))
