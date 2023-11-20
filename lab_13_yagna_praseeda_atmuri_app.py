import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

# Load data
df = pd.read_csv('C:/Users/prase/OneDrive/Documents/INFORMATICS/Project_proposal/dataset.csv')

def plot_quantity_distribution(sort_by):
    # Group the data by 'Country' and calculate the average quantity for each country
    avg_quantity_by_country = df.groupby('Country')['Quantity'].mean().sort_values(ascending=False).reset_index()

    # Sort the data based on the selected sorting option
    if sort_by == 'Ascending':
        avg_quantity_by_country.sort_values('Quantity', inplace=True)
    elif sort_by == 'Descending':
        avg_quantity_by_country.sort_values('Quantity', ascending=False, inplace=True)

    # Set a creative color palette
    palette = sns.color_palette("pastel")

    # Plotting the bar chart with seaborn
    plt.figure(figsize=(14, 8))
    sns.barplot(x='Country', y='Quantity', data=avg_quantity_by_country, palette=palette)
    plt.title('Average Quantity of Items Purchased by Country', fontsize=16)
    plt.xlabel('Country', fontsize=14)
    plt.ylabel('Average Quantity', fontsize=14)
    plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
    plt.tight_layout()

    # Display the plot using Streamlit
    st.pyplot(plt)

# Streamlit app
def main():
    st.title('Average Quantity Distribution by Country')
    st.sidebar.header('Sort Options')
    sort_by = st.sidebar.radio('Sort by:', ('Ascending', 'Descending'), index=1)

    plot_quantity_distribution(sort_by)

if __name__ == '__main__':
    main()
