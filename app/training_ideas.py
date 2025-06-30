import pandas as pd


class TrainingIdeas:
    def __init__(self,label):
        self.training=pd.read_excel("../src/data_training.xlsx")
        self.label=label.lower()

    def get_training_idea(self):
        match self.label:
            case "menstruation":
                look_for_category=["Cross-functional training","Running training" ]
                look_for_focus=["Low-Impact Cardio","Mobility & Flexibility", "Plyometrics", "Balance",
                                "Very Low", "Low", "Low to Moderate" , "Low to High" ]
            case "progesterone-building":
                look_for_category=["Cross-functional training" ]
                look_for_focus=["Low-Impact Cardio","Mobility & Flexibility", "Plyometrics", "Balance",
                                    ]
            case "luteal phase":
                look_for_category=["Running training", "Strength training" ]
                look_for_focus=["Moderate to High", "High", "Very High" , "Low to High", "Core", "Upper Body", "Lower Body" ]
            case "ovulation":
                look_for_category=["Cross-functional training","Strength training" ]
                look_for_focus=["Lower Body Free weigth","Agility", "Plyometrics", "Balance",
                                "Core Free weigth" ]
            case "estrogen-predominant":
                look_for_category=["Running training" ]
                look_for_focus=["Moderate to High", "High", "Very High" , "Low to High" ]

        selection=(self.training[
                (self.training['Category'].isin(look_for_category)) &
                (self.training['Focus'].isin(look_for_focus))
            ][['Name', 'Category']])
        
        selected_dict = {key: [] for key in set(selection.Category)}

        for row in selection.itertuples():
            selected_dict[row.Category].append(row.Name)
        return selected_dict
