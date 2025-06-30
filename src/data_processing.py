import os
import pandas as pd
os.getcwd()

labeling={
    "Estrogen":["Anacardi", "Arachidi salate e tostate", "Mandorle", "Noci", "Noci del Brasile", "Pinoli", "Semi di girasole", "Semi di sesamo", 
                "Semi di zucca", "Carruba", "Ceci", "Fagioli borlotti", "Fagioli dall'occhio", "Fagioli di Lima", "Fagioli rossi", "Fagioli verdi", "Lenticchie", 
                "Piselli", "Soia", "Aglio", "Broccoli", "Cavolfiori", "Cavoli", "Cipolle", "Fragole", "Germogli", "Mirtilli", "Mirtilli rossi", "Spinaci", "Zucchine", "Zucca", 
                "Semi di lino", "Cavoletti di Bruxelles", "Bok choy", "Bietola", "Cavolo riccio", "Cavolo verde", "Senape indiana", "Prezzemolo"],
    "Progesteron": ["Barbabietole", "Finocchio", "Igname", "Patate bianche", "Patate rosse", "Rape", "Zucca acorn", "Zucca comune", "Zucca spaghetti", 
                "Broccoli", "Cavoletti di Bruxelles", "Cavolfiori", "Banana", "Mango", "Papaia", "Arancia", "Lime", "Limoni", "Pompelmo", 
                "Semi di girasole", "Semi di lino", "Semi di sesamo", "Ceci", "Fagioli neri", "Fagioli rossi", 
                "Patate dolci", "Zucca", "Zucche", "Mele", "Frutti di bosco", "Cavolo", "Banane"],
    "Probiotic": ["Crauti", "Kefir", "Kimchi", "Sottoaceti", "Yogurt", "Miso", "Kombucha", "Tempeh", "Natto", "Lassi"],
    "Prebiotic": ["Aglio", "Anacardi", "Asparagi", 
                "Ceci", "Cipolle", "Fagioli rossi", "Hummus", "Piselli spezzati", "Pistacchi", "Porri", 
                "Radice di bardana", "Radice di cicoria", "Radice di konjac", "Radice di tarassaco", "Topinanmbur",
                "Manioca", "Carciofi", "Jicama", "Frutta secca", "Semi", 
                "Banane verdi", "Pomodori", "Verdure a foglia", 
                "Bacche", "Kiwi", "Ciliegia", "Mela", "Pera", "Mango", "Quinoa", 
                "Lenticchie", "Ceci"],
    "Polifenols":[
                "Broccoli", "Cavoletti di Bruzelles", "Cioccolato amaro", "Cuori di carciofo",
                "Olive", "Prezzemolo", "Scalogno", "Vino rosso",
                "Chiodi di garofano", "Menta piperita", "Cacao", "Semi di lino", "Origano",
                "Carciofo", "Noci", "Semi di sedano", "Sambuco nero", "Salvia", "Rosmarino",
                "Vino rosso", "Mirtilli", "Timo", "Olive nere", "Olive verdi", "Ciliegie",
                "Prugne", "Basilico dolce", "More", "Fragole", "Curry", "Lamponi", "Cavolfiore",
                "Pesche", "Caffè", "Prugne secche", "Red onion", "Zenzero", "Uva nera",
                "Spinaci", "Tè verde", "Melograni", "Tè nero", "Cipolla gialla", "Olio extra vergine di oliva", "Mele"
                ],
    "Liver": ["Agrumi", "Aneto", "Caffe", "Cavoletti di Bruxelles", "Cavoli di foglia", 
                "Curcuma", "Melanzane", "Menta piperita", "Rucola", "Semi di sesamo", 
                "Tarassaco", "Te verde", "Topinambur", "Zafferano", "Zenzero"],
    "Good Fats": ["Avocado", "Burro di malga", "Burro di noci", "Latticini di malga", "Noci di cocco", 
                "Olio di avocado", "Olio di cocco", "Olio di coriandolo", "Olio di cumino nero", 
                "Olio di oliva", "Olio di semi di lino", "Olio di sesamo", "Olio MCT", "Olive"],
    "Muscle": ["Pesci", "Pollo", "Quinoa", "Ricotta", "Semi di chia", "Tacchino", "Tofu", "Uova", 
                "Crostacei", "Funghi", "Maiale", "Manzo", "Agnello"]


}
#Functions to create the DataFrame
def create_dataframe(df):
    n=len(set(df.loc[:,"Original name"]))
    new_dataset = pd.DataFrame({
    "Ingredient": ["" for _ in range(n)],
    "Food group": ["" for _ in range(n)],
    "Proteins": [0.0 for _ in range(n)],
    "Fats": [0.0 for _ in range(n)],
    "Carbs": [0.0 for _ in range(n)],
    "Fibers": [0.0 for _ in range(n)],
    "Hormonal phase": [[] for _ in range(n)],
    "Target area": [[] for _ in range(n)],
    "Fasting state": [[] for _ in range(n)],
    "Label": [[] for _ in range(n)],
    })
    new_dataset['Ingredient'] =(list(set(df.loc[:,"Original name"])))
    return new_dataset

def populate_dataframe(index, item, df, new_dataset):
    filtered_df=df[df['Original name']==item]
    new_dataset.loc[index,'Food group'] = next(iter(filtered_df['Food group']),0)
    new_dataset.loc[index,'Carbs']=next(iter(filtered_df[filtered_df['Component Name']=='carbohydrate']['Selected value']),0)
    new_dataset.loc[index,'Fibers']=next(iter(filtered_df[filtered_df['Component Name']=='fibre, total dietary']['Selected value']),0)
    new_dataset.loc[index,'Proteins']=next(iter(filtered_df[filtered_df['Component Name']=='protein, total']['Selected value']),0)
    new_dataset.loc[index,'Fats']=next(iter(filtered_df[filtered_df['Component Name']=='fat, total']['Selected value']),0)
    return new_dataset

#Labelling functions:

def populate_macro(row):
    values = {
        "Proteins": row["Proteins"],
        "Fats": row["Fats"],
        "AdjustedCarbs": row["Carbs"] - row["Fibers"]
    }

    max_col = max(values, key=values.get)
    data_food.loc[index,'Macro'] = max_col

def populate_label_non_whole_food(row):
    if row['Food group'] in [ 'MISCELLANEOUS FOOD PRODUCT', 'BEVERAGE (NON-MILK)']:
        data_food.loc[index,'Label'].append('Ultra-processed food') 
    elif row['Food group'] in ['GRAIN OR GRAIN PRODUCT']:
        data_food.loc[index,'Label'].append('Processed carbs')
    elif row['Food group'] in ['SUGAR OR SUGAR PRODUCT']:
        data_food.loc[index,'Label'].append('Processed sugars')
    if data_food.loc[index,'Label']:
        data_food.loc[index,'Macro'] = None

def get_label_from_dataset(row):
    index=labelled_data[labelled_data.Ingredient == row.Ingredient].index[0]

    label=labelled_data['Matched Labels'][index]
    if str(label) != 'nan':
        data_food.loc[index,'Label'].extend(label.split(', '))

def derive_funcs_from_label(row):
    if 'Estrogen' in row.Label:
            data_food.loc[index,'Hormonal phase'].append('Estrogen-building')

    if 'Progesteron' in row.Label:
        data_food.loc[index,'Hormonal phase'].append('Progesteron-building')

    if 'Liver' in row.Label:
        data_food.loc[index,'Target area'].append('Liver')

    if 'Muscle' in row.Label:
        data_food.loc[index,'Target area'].append('Muscle')

    if 'Good Fats' in row.Label:
        data_food.loc[index,'Fasting state'].append('Extend fasting')

    if 'Probiotic' in row.Label or 'Prebiotic' in row.Label or 'Polifenols' in row.Label:
        data_food.loc[index,'Target area'].append('Gut')
    if 'Probiotic' in row.Label:
        data_food.loc[index,'Fasting state'].append('Gut healing')

def derive_funcs_from_macro(row):
    if row.Macro == 'Proteins':
        data_food.loc[index,'Fasting state'].append('Muscle building')

    if row.Macro == 'AdjustedCarbs' and row['Food group'] not in ['MISCELLANEOUS FOOD PRODUCT', 'BEVERAGE (NON-MILK)','GRAIN OR GRAIN PRODUCT','SUGAR OR SUGAR PRODUCT']:
        if 'Progesteron-building' not in data_food.loc[index,'Hormonal phase']:
            data_food.loc[index,'Hormonal phase'].append('Progesteron-building')
#import the various dataset and concatenate into a single dataframe
list_dataset=[]
for i in range(0,36):

    df=pd.read_excel(f"data/FoodEXplorer_data ({i}).xlsx", sheet_name="FoodEXplorer_Export", skiprows=2)
    new_dataset=create_dataframe(df)
    for index, item in new_dataset.Ingredient.items():
        new_dataset= populate_dataframe(index, item, df, new_dataset)
    list_dataset.append(new_dataset)

data_food=pd.concat(list_dataset, ignore_index=True)
labelled_data= pd.read_excel("../../ingredient_label_matches.xlsx")

for index in range(len(data_food)):
    populate_macro(data_food.loc[index])

    populate_label_non_whole_food(data_food.loc[index])
    # data_food.loc[index,'Label']=None
    
    get_label_from_dataset(data_food.loc[index])

    if data_food.loc[index].Label:
        derive_funcs_from_label(data_food.loc[index])
    derive_funcs_from_macro(data_food.loc[index])

data_food.to_excel("data_ready.xlsx")
print(data_food.head())
print("All good!")