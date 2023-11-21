import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

file_path = 'dataset.csv'
df = pd.read_csv(file_path)

def plot_quantity_distribution(sort_by):
    
    avg_quantity_by_country = df.groupby('Country')['Quantity'].mean().sort_values(ascending=False).reset_index()

   
    if sort_by == 'Ascending':
        avg_quantity_by_country.sort_values('Quantity', inplace=True)
    elif sort_by == 'Descending':
        avg_quantity_by_country.sort_values('Quantity', ascending=False, inplace=True)

    palette = sns.color_palette("pastel")

    plt.figure(figsize=(14, 8))
    sns.barplot(x='Country', y='Quantity', data=avg_quantity_by_country, palette=palette)
    plt.title('Average Quantity of Items Purchased by Country', fontsize=16)
    plt.xlabel('Country', fontsize=14)
    plt.ylabel('Average Quantity', fontsize=14)
    plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
    plt.tight_layout()

    st.pyplot(plt)

def main():
    st.title('Average Quantity Distribution by Country')
    st.sidebar.header('Sort Options')
    sort_by = st.sidebar.radio('Sort by:', ('Ascending', 'Descending'), index=1)

    plot_quantity_distribution(sort_by)

if __name__ == '__main__':
    main()
