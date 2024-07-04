
## importamos streamlit
import streamlit as st

## Leer archivo

import pandas as pd

verbos = pd.read_excel('verbos.xlsx')

## diccionario

quechua = list(verbos['quechua'])
espanol = list(verbos['espanol'])

dict_que_esp = dict(zip(quechua,espanol))

## insertar cuadro con conjugaciones de presente
datos = pd.read_excel('Presente1.xlsx')

## Renombrar primera columna
datos = datos.rename(columns={'Unnamed: 0':'Persona'})


## Diccionario de conjugaciones del presente
D = {}
for i in datos.index:
  f = list(datos.loc[i])
  d = dict(zip(['Singular','Plural'],f[1:]))
  D[f[0]] = d


##### FUNCIONES ######

## Conj presente simple
def CPS(base,persona,numero):
  return base + D[persona][numero]

## Conj presente progresivo
def CPC(base,persona,numero):
  return base + 'chka' + CPS(base,persona,numero)[len(base):]

## Conj presente habitual
def CPH(base,persona,numero):
  if persona == 'Tercera':
    resultado = base + 'q' + 'mi'
  else:
    resultado = base + 'q' + ' ' + CPS('ka',persona,numero)
  return resultado

## Conj pasado experimentado simple:
def C_Pas_Exp(base,persona,numero):
  if persona == 'Tercera':
    if numero == 'Singular':
      r_pas_exp = base + 'rqa'
    if numero == 'Plural':
      r_pas_exp = base + 'rqa' + 'ku'
  else:
   r_pas_exp = base + 'rqa' + CPS(base,persona,numero)[len(base):]

  return r_pas_exp

## Conj pasado experimentado progresivo:
def C_Pas_Exp_Pro(base,persona,numero):
  if persona == 'Tercera' and numero == 'Singular':
    r_pas_exp_pro = base + 'chka' + 'rqa'
  else:
    r_pas_exp_pro = base + 'chka' + 'rqa' + CPS(base,persona,numero)[len(base):]

  return r_pas_exp_pro


## Conj pasado experimentado habitual
def C_Pas_Exp_Hab(base,persona,numero):
  if persona == 'Tercera':
    if numero == 'Singular':
      r_pas_exp_hab = base + 'q' + ' ' + 'karqa'
    if numero == 'Plural':
      r_pas_exp_hab = base + 'q' + ' ' + 'karqaku'
  else:
    r_pas_exp_hab = base + 'q' + ' ' + C_Pas_Exp('ka',persona,numero)
  return r_pas_exp_hab


## Conj pasado no experimentado simple
def C_Pas_NExp(base,persona,numero):
  if persona == 'Tercera':
    if numero == 'Singular':
      r_pas_nexp = base + 'sqa'
    if numero == 'Plural':
      r_pas_nexp = base + 'sqa' + 'ku'
  else:
    r_pas_nexp = base + 'sqa' + CPS(base,persona,numero)[len(base):]

  return r_pas_nexp

## Conj pasado no experimentado progresivo
def C_Pas_NExp_Pro(base,persona,numero):
  if persona == 'Tercera':
    if numero == 'Singular':
      r_pas_nexp_pro = base +'chka' + 'sqa'
    if numero == 'Plural':
      r_pas_nexp_pro = base + 'chka' + 'sqa' + 'ku'
  else:
    r_pas_nexp_pro = base + 'chka' + 'sqa' + CPS(base,persona,numero)[len(base):]

  return r_pas_nexp_pro

## Conj pasado no experimentado habitual
def C_Pas_NExp_Hab(base,persona,numero):
  if persona == 'Tercera':
    if numero == 'Singular':
      r_pas_nexp_hab = base + 'q' + ' ' + 'kasqa'
    if numero == 'Plural':
      r_pas_nexp_hab = base + 'q' + ' '+ 'kasqaku'
  else:
    r_pas_nexp_hab = base + 'q' + ' ' +  C_Pas_Exp('ka',persona,numero)

  return r_pas_nexp_hab

##### FIN DE FUNCIONES #####


########## configuracion del tema de la pagina



st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Oswald:wght@200..700&display=swap'); /* OSWALD */

@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400..900;1,400..900&display=swap'); /* PLAYFAIR DISPLAY */

@import url('https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,100..900;1,100..900&display=swap');

@import url('https://fonts.googleapis.com/css2?family=Roboto+Condensed:ital,wght@0,100..900;1,100..900&display=swap');

@import url('https://fonts.googleapis.com/css2?family=Wittgenstein:ital,wght@0,400..900;1,400..900&display=swap');

.logo {
    display: flex;
    justify-content: center;
    align-items: center;
    margin-bottom: 20px;
}

.logo img {
    width: 150px; /* Ajusta el tamaño según sea necesario */
}

body {
    background-color: #F0EAD6;
    font-family: 'Crimson Pro', serif; /* Añadir la fuente 'Crimson Pro' */
}

/* Cambia el color y tamaño de los títulos */


.header1 {
    color: #654321; 
    font-size: 4em;
    font-family: 'Playfair Display', sans-serif; 
}

.header2 {
    color: #C2B080;     font-size: 2em;
    font-family: 'Wittgenstein', serif;
    margin-bottom: 1px; 
}

.header3 {
    color: #654321;     font-size: 40px;
    font-family: 'Wittgenstein', serif;
    margin-bottom: 1px; 
}

.header4 {
    color: #F5F5DC;     font-size: 2em;
    font-family: 'Crimson Pro', serif;
    margin-bottom: 1px; 
}

.caption-custom {
    color: #997d64; /* Cambia esto al color que desees */
    font-size: 16px; /* Cambia el tamaño de la fuente si es necesario */
    font-family: 'Montserrat', sans-serif;
    text-align: justify; 
    }

.custom-divider {
    border-top: 2px solid #b39c89;  /* Cambia el color y el grosor del divisor */
    margin-top: 0px;  /* Ajusta el margen superior */
    margin-bottom: 20px;  /* Ajusta el margen inferior */
}

div[data-baseweb="select"] {
  font-family: 'Montserrat', sans-serif;
  color: #997d64
  margin-top: 0px;
}



""", unsafe_allow_html=True)


#### logo y columna

col1, col2 = st.columns([1, 2])  

## título de la página
with col2:
    st.markdown('<h1 class="header1">CONJUGADOR DE QUECHUA CHANCA</h1>', unsafe_allow_html=True)
## logo de la página
with col1:
    st.image('assets/1.png', width=250)



## presentacion
st.markdown('<h2 class="header2">¡Bienvenido!</h2>', unsafe_allow_html=True)

## texto de presentacion
st.markdown('<p class="caption-custom">Te presentamos el conjugador de quechua de la variedad <b>chanca</b>. Esta variedad es conocida también como variedad <b>ayacuchana</b> y forma parte de la <b>subrama sureña</b> o <b>subrama Quechua II</b>. Es hablada en Huancavelica, Ayacucho y en la parte oeste de Apurímac.</p>', unsafe_allow_html=True)

## divider 2
st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)

### CONJUGADOR DE QUECHUA

## título de PARTE 1

st.markdown('<h3 class="header3">¡Escoge un verbo y conjúgalo!</h3>', unsafe_allow_html=True)


## Header escoger un verbo

st.markdown('<p class="caption-custom">Escoge el verbo que quieres conjugar:</p>', unsafe_allow_html=True)


## Con pronombres y aspecto

P = {'Primera':{'Singular':'ñuqa','Plural':'ñuqayku'},'Segunda':{'Singular':'qam','Plural':'qamkuna'},'Tercera':{'Singular':'pay','Plural':'paykuna'},'Cuarta':{'Singular':'ñuqanchik'}}

## Prototipo con tiempo y aspecto

### opcion de base

base = st.selectbox(
    "",
    (quechua))
st.write("El verbo en español es", dict_que_esp[base])


### opcion de persona

persona = st.radio(
    'Selecciona la persona',
    ['Primera','Segunda','Tercera','Cuarta'])

### opcion de numero

numero = st.radio(
    'Selecciona el número',
    ['Singular','Plural'])

### boton de tiempo

t = st.selectbox(
    'Selecciona el tiempo',
    ['Presente','Pasado'])

## boton cuando es tiempo presente
if t == 'Presente':
   asp = st.radio(
       'Seleeciona el aspecto',
       ['Simple','Progresivo','Habitual'])

## boton cuando tiempo es pasado
if t == 'Pasado':
  asp = st.radio(
      'Selecciona entre:',
      ['Experimentado','No experimentado'])
  
  if asp == 'Experimentado' or 'No experimentado':
    asp2 = st.radio(
        'Selecciona el aspecto', 
        ['Simple','Progresivo','Habitual'])

## Quitar el sufijo -y de infinitivo
if base[-1] == 'y':
  base = base[:len(base) - 1]

## Eliminar el error de cuarta persona plural
if persona == 'Cuarta' and numero == 'Plural':
  resultado = 'No existe cuarta persona plural'
## Establecer el resultado según tiempo y aspecto
else:
  ## presente simple
  if t == 'Presente' and asp == 'Simple':
    v_conj = CPS(base,persona,numero)
  ## presente progresivo
  if t == 'Presente' and asp == 'Progresivo':
    v_conj = CPC(base,persona,numero)
  ## presente habitual
  if t == 'Presente' and asp == 'Habitual':
    v_conj = CPH(base,persona,numero)
  ## pasado experimentado simple
  if t == 'Pasado' and asp == 'Experimentado' and asp2 == 'Simple':
    v_conj = C_Pas_Exp(base,persona,numero)
  ## pasado experimentado progresivo
  if t == 'Pasado' and asp == 'Experimentado' and asp2 == 'Progresivo':
    v_conj = C_Pas_Exp_Pro(base,persona,numero)
  ## pasado experimentado habitual
  if t == 'Pasado' and asp == 'Experimentado' and asp2 == 'Habitual':
    v_conj = C_Pas_Exp_Hab(base,persona,numero)
  ## pasado no experimentado simple
  if t == 'Pasado' and asp == 'No experimentado' and asp2 == 'Simple':
    v_conj = C_Pas_NExp(base,persona,numero)
  ## pasado no experimentado progresivo
  if t == 'Pasado' and asp == 'No experimentado' and asp2 == 'Progresivo':
    v_conj = C_Pas_NExp_Pro(base,persona,numero)
  ## pasado no experimentado habitual
  if t == 'Pasado' and asp == 'No experimentado' and asp2 == 'Habitual':
    v_conj = C_Pas_NExp_Hab(base,persona,numero)
  resultado = P[persona][numero] + ' ' + v_conj


st.write("**Resultado:**",resultado)

##############################################################################

st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)




#### TRADUCTOR INVERSO

ora = st.text_input("Ingresa el verbo conjugado (puedes incluir el pronombre también):", "ñuqa mikuni")

## poner en minusculas

ora = ora.lower()

## quitar simbolos raros
b = ['.',',','\n',')','(','"','-']
for simbolo in b:
    ora = ora.replace(simbolo,'')

## cortar en strings

ora2 = ora.split(' ')

## definiendo variables

if len(ora2) == 1:
    verb = ora2[0]
if len(ora2) == 2:
    pron = ora2[0]
    verb = ora2[1]

## definir persona
if verb.endswith("ni") or verb.endswith("niku"):
    persona = "Primera"

if verb.endswith("nki") or verb.endswith("nkichik"):
    persona = "Segunda"

if verb.endswith("n") or verb.endswith("nku") or verb.endswith("rqa"):
    persona = "Tercera"

if verb.endswith("nchik"):
    persona = "Cuarta"
    
st.write("Persona:",persona)

## definir número

if verb.endswith("ni") or verb.endswith("nki") or verb.endswith("n") or verb.endswith("nchik") or verb.endswith("rqa"):
    numero = "Singular"

if verb.endswith("niku") or verb.endswith("nkichik") or verb.endswith("nku") or verb.endswith("rqa"):
    numero = "Plural"


st.write("Número:",numero)

## definir tiempo

### presente

if verb.endswith("ni") or verb.endswith("niku") or verb.endswith("nki") or verb.endswith("nkichik") or verb.endswith("n") or verb.endswith("nku") or verb.endswith("nchik") and ('rqa' or 'sqa' not in verb):
    
    tiempo = "Presente"
    
### pasado experimentado

if 'rqa' in verb:
    tiempo = "Pasado experimentado"

### pasado no experimentado

if 'sqa' in verb:
    tiempo = "Pasado no experimentado"
    
st.write("Tiempo:",tiempo)

## definir aspecto

### progresivo
if 'chka' in verb:
    
    aspecto = 'Progresivo'



