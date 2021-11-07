import streamlit as st
import pickle
from datetime import datetime
startTime = datetime.now()
# import znanych nam bibliotek

filename = "model.sv"
model = pickle.load(open(filename,'rb'))
# otwieramy wcześniej wytrenowany model

#sex_d = {0:"Kobieta",1:"Mężczyzna"}
#pclass_d = {0:"Pierwsza",1:"Druga", 2:"Trzecia"}
#embarked_d = {0:"Cherbourg", 1:"Queenstown", 2:"Southampton"}
# o ile wcześniej kodowaliśmy nasze zmienne, to teraz wprowadzamy etykiety z ich nazewnictwem
def main():

	st.set_page_config(page_title="Czy pacjent wyzdrowieje po tygodniu?")
	overview = st.container()
	left, right = st.columns(2)
	prediction = st.container()

	#st.image("https://integrisok.com/-/media/campaigns/doctor-oklahoma/ep3-vaccines.ashx?revision=da735841-b7dd-4186-aa5a-7df73b522f5e")

	# with overview:
	# 	st.title("Czy przeżyłbyś katastrofę?")

	# with left:
	# 	sex_radio = st.radio( "Płeć", list(sex_d.keys()), format_func=lambda x : sex_d[x] )
	# 	pclass_radio = st.radio( "Klasa", list(pclass_d.keys()), format_func=lambda x: pclass_d[x])
	# 	embarked_radio = st.radio( "Port zaokrętowania", list(embarked_d.keys()), index=2, format_func= lambda x: embarked_d[x] )

	# with right:
	# 	age_slider = st.slider("Wiek", value=50, min_value=1, max_value=100)
	# 	sibsp_slider = st.slider( "# Liczba rodzeństwa i/lub partnera", min_value=0, max_value=8)
	# 	parch_slider = st.slider( "# Liczba rodziców i/lub dzieci", min_value=0, max_value=6)
	# 	fare_slider = st.slider( "Cena biletu", min_value=0, max_value=500, step=10)

	with overview:
		st.title("Czy pacjent wyzdrowieje po tygodniu?")

	with left:
		wiek_slider = st.slider("Wiek", value=50, min_value=11, max_value=77)
		objawy_slider = st.slider("Objawy", value=2, min_value=1, max_value=5)

	with right:
		wzrost_slider = st.slider("Wzrost", value=165, min_value=150, max_value=200)
		choroby_slider = st.slider("Choroby", value=1, min_value=0, max_value=5)



	data = [[objawy_slider, wiek_slider,  choroby_slider, wzrost_slider]]
	survival = model.predict(data)
	s_confidence = model.predict_proba(data)

	with prediction:
		st.header("Czy dana osoba wyzdrowieje? {0}".format("Tak" if survival[0] == 0 else "Nie"))
		st.subheader("Pewność predykcji {0:.2f} %".format(s_confidence[0][survival][0] * 100))

	if survival[0] == 0:
		st.image("https://integrisok.com/-/media/campaigns/doctor-oklahoma/ep3-vaccines.ashx?revision=da735841-b7dd-4186-aa5a-7df73b522f5e")
	else:
		st.image("https://media1.tenor.com/images/adecdee5d4f010a8bb2edaf4601f70e5/tenor.gif?itemid=16728820")
if __name__ == "__main__":
    main()

## Źródło danych [https://www.kaggle.com/c/titanic/](https://www.kaggle.com/c/titanic), zastosowanie przez Adama Ramblinga