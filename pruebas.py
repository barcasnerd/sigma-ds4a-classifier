import RF_new

loc = "descripciones_tickets_preprocess.csv"

model = RF_new.model_classifier(loc)

RF_new.make_pred(loc,["Hola"],model)