import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader.data as web
import yfinance as yf
yf.pdr_override()


#coleta dos dados do mercado


ibov = web.get_data_yahoo('^BVSP')

""" ###  PARA O TEMPO TOTAL DOS DADOS
ibov["Close"].plot(figsize=(22,8), label="IBOV")
ibov["Close"].rolling(21).mean().plot(label="M21")
ibov["Close"].rolling(200).mean().plot(label="M200")
plt.legend()"
"""

"""" ### PARA O TEMPO DE UM ANO
ibov_parc = ibov[ibov.index.year == 2020]
ibov_parc["Close"].plot(figsize=(22,8), label="IBOV")
ibov_parc["Close"].rolling(21).mean().plot(label="M21")
ibov_parc["Close"].rolling(200).mean().plot(label="M200")
plt.legend()
"""

""""  ### PARA UM INTERVALO DE ANOS
ibov_parc = ibov[(ibov.index.year >= 2010) & (ibov.index.year <= 2020)]
ibov_parc["Close"].plot(figsize=(22,8), label="IBOV")
ibov_parc["Close"].rolling(21).mean().plot(label="M21")
ibov_parc["Close"].rolling(200).mean().plot(label="M200")
plt.legend()
"""

""" ### PARA UM DETERMINADO MÊS/DIA EM 'N' ANOS
ibov_parc = ibov[ibov.index.month == 8]
ibov_parc.tail(5)
"""

"""" ### PARA UM PERÍODO ESPECÍFICO
ibov = web.get_data_yahoo('^BVSP', start='2010-05-03', end='2020-06-04')
"""