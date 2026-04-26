
import kagglehub


df = kagglehub.dataset_download("artheon/pulse-2026-music-evolution-and-viral-analytics")

import pandas as pd 

data=pd.read_csv('Music_Evolution_2026_Pulse.csv')

def show_head(df):
    print("\n Showing first 5 rows: ")
    print(df.head())

def show_tail(df):
    print("\n Showing last 5 rows: ")
    print(df.tail())
def show_columns(df):
    """Show all column names"""
    print("\n📋 COLUMN NAMES:")
    for i, col in enumerate(df.columns, 1):
        print(f"   {i}. {col}")
def show_shape(df):
    print("Showing the shape of dataset")
    print(f"SHAPE {df.shape[0]} rows, {df.shape[1]} columns")
def show_stats(df):
    print("\n📊 STATISTICAL SUMMARY:")
    print(df.describe())
def missing_values(df):
    print("Showing the missing values: ")
    missing=df.isnull().sum()
    if missing.sum()==0:
        print("\n NO MISSING VALUES")
    else:
        for col in df.columns:
            if missing[col] > 0:
                print(f" ❌ {col}: {missing[col]} missing values")

#-----Menu-----
def show_menu():
    """Display menu (Day 2 & 4 concept)"""
    print("\n" + "="*50)
    print("        SIMPLE DATA ANALYZER")
    print("="*50)
    print("1. Show first 5 rows (head)")
    print("2. Show last 5 rows (tail)")
    print("3. Show column names")
    print("4. Show shape (rows, columns)")
    print("5. Show statistical summary (describe)")
    print("6. Show missing values")
    print("7. Exit")
    print("="*50)

def main():
    print("\n🔍 WELCOME TO SIMPLE DATA ANALYZER")
    print("This tool helps you explore any CSV dataset.\n")
    df=pd.read_csv('Music_Evolution_2026_Pulse.csv') 
    
    # Menu loop (Day 2 & 3 concept)
    while True:
        show_menu()
        choice = input("Enter your choice (1-7): ")
        
        # Conditionals (Day 3 concept)
        if choice == "1":
            show_head(df)
        elif choice == "2":
            show_tail(df)
        elif choice == "3":
            show_columns(df)
        elif choice == "4":
            show_shape(df)
        elif choice == "5":
            show_stats(df)
        elif choice == "6":
            missing_values(df)
        elif choice == "7":
            print("\n👋 Thank you for using Data Analyzer. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please enter a number between 1 and 7.")

# Run the program
if __name__ == "__main__":
    main()