import pandas as pd 
from sklearn.model_selection import train_test_split
from datasets import load_dataset
    
def load_data():
    
    dataset = load_dataset("fawern/turkish-hate-speech")

    df = pd.DataFrame(dataset['train'])

    X = df['tweet']
    y = df['label']

    labels = y.unique()
    label_dict = {label: i for i, label in enumerate(labels)}

    y = y.map(label_dict)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    return X_train, X_test, y_train, y_test, label_dict
