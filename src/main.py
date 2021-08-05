import pandas as pd


def main():
        data = pd.read_csv('pokedex.csv')
        data = data.drop(['german_name','japanese_name','catch_rate','base_friendship','base_experience','growth_rate','egg_type_number','egg_type_1','egg_type_2','percentage_male','egg_cycles'], axis=1)
        print(data.columns)


if __name__ == '__main__':
    main()