import re

genes =  { 'AAA': ['borstkanker', 12],
              'AAB': ['huidkanker', 13],
              'AAC': ['botkanker', 19],
              'AAD': ['borstkanker', 21],
              'AAE': ['huidkanker', 15],
              'ABA': ['hersenkanker', 3],
              'ABB': ['botkanker', 6],
              'ABC': ['hartkanker', 8],
              'ABD': ['borstkanker', 9]

              }

genes2 =  { 'AAA': 'borstkanker',
              'AAB': 'huidkanker',
              'AAC': 'botkanker',
              'AAD': 'borstkanker',
              'AAE': 'huidkanker',
              'ABA': 'hersenkanker',
              'ABB': 'botkanker',
              'ABC': 'hartkanker',
              'ABD': 'borstkanker'
           }
#print(gene_dic)

#search = '.*borst.*'

match = re.search('^.*borst.*', genes2.values())
print(match)
