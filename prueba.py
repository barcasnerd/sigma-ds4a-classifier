import RF_new
import joblib
from time import time 

start_time = time()
loc = "descripciones_tickets_preprocess.csv"
model  = joblib.load("./random_forest2.joblib")

df = RF_new.make_pred(loc, ["Servidor"], model)
final_time = time()-start_time
print(f"{final_time} seconds")