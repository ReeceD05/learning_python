from pandas import DataFrame as df, Series as ser
import matplotlib

print("Pandas Version:", df.__module__.split('.')[0])
print("Matploylib Version:", matplotlib.__version__)