import streamlit as st

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


# Tab layout
tabs = ["Life Expectancy", "Smoking", "Obesity", "Homicide", "Opioid overdoses", "Road Injuries"]
selected_tab = st.sidebar.selectbox("Select Tab", tabs)

  
# Data and visualization for Life Expectancy tab
if selected_tab == "Life Expectancy":
   
  # Page title
    st.title("What Influences Life Expectancy in the US")
    # Introduction
    st.write("Despite being the country that spends the most on healthcare globally, the life expectancy of Americans is comparatively shorter than in other affluent nations that allocate considerably less resources to healthcare. To better understand this phenomenon, we have examined several contributing factors, including smoking, obesity, homicides, opioid overdoses, and road accidents.")
   
    st.title("Life Expectancy")
    
   # Load the life expectancy data
    data = pd.read_csv("/Users/tijanmoghnieh/Desktop/DP_LIVE_09062023031048950.csv")
    
    # Define the selected countries and their corresponding labels
    selected_countries = {"ESP": "Spain", "JPN": "Japan", "AUS": "Australia", "DEU": "Germany", "FRA": "France", "USA": "United States", "CHE": "Switzerland"}
    
    # Filter the data for the selected countries
    filtered_data = data[data['LOCATION'].isin(selected_countries.keys())]
    
    # Define the color mapping
    colors = {code: "red" if code == "USA" else "gray" for code in selected_countries.keys()}
    
    # Filter the data for USD_CAP measure
    filtered_data_usd = filtered_data[filtered_data['MEASURE'] == 'USD_CAP']
    
    # Update the country labels in the data
    filtered_data_usd['LOCATION'] = filtered_data_usd['LOCATION'].map(selected_countries)
    
    # Plot the line graph
    fig = px.line(filtered_data_usd, x="TIME", y="Value", color="LOCATION")
    
    # Apply color mapping to lines
    for trace in fig.data:
        country = trace.name
        if country == "United States":
            trace.line.color = "red"
        else:
            trace.line.color = "gray"
    
    # Update the axis labels
    fig.update_layout(xaxis_title="Year", yaxis_title="Value in USD_CAP")
    # Update the title
    fig.update_layout(title="Health Expenditure in Rich Countries")
    
    st.plotly_chart(fig)
    
#2nd graph

 # Load the life expectancy data
    data2 = pd.read_csv("/Users/tijanmoghnieh/Desktop/DP_LIVE_09062023034900901.csv")
    
 
    # Define the selected countries and their corresponding labels
    selected_countries = {"ESP": "Spain", "JPN": "Japan", "AUS": "Australia", "DEU": "Germany", "FRA": "France", "USA": "USA", "CHE": "Switzerland"}
    
    # Filter the data for the selected countries
    filtered_data2 = data2[data2['LOCATION'].isin(selected_countries.keys())]
    
    # Define the color mapping
    colors = {"USA": "red", "ESP": "gray", "JPN": "gray", "AUS": "gray", "DEU": "gray", "FRA": "gray", "CHE": "gray"}
    
    # Update the country labels in the data
    filtered_data2["LOCATION"] = filtered_data2["LOCATION"].map(selected_countries)
    
    # Plot the line graph for life expectancy
    fig2 = px.line(filtered_data2, x="TIME", y="Value", color="LOCATION")
    
    # Apply color mapping to lines
    for trace in fig2.data:
        abbreviation = trace.name
        country = selected_countries.get(abbreviation, "gray")
        trace.line.color = colors.get(country, "gray")
    
    # Update the axis labels and title
    fig2.update_layout(xaxis_title="Year", yaxis_title="Life Expectancy", title="Life Expectancy in Selected Countries")
    
    st.plotly_chart(fig2)


    
# Data and visualization for Smoking tab
elif selected_tab == "Smoking":
    st.title("Smoking")
    
  # Load the dataset
    data1 = pd.read_csv("/Users/tijanmoghnieh/Desktop/sales-of-cigarettes-per-adult-per-day.csv")
    # Page title
    st.subheader("Death Rate from Smoking")
# Create the choropleth map
    fig1 = px.choropleth(data1,
                     locations="Code",
                     locationmode="ISO-3",
                     color="Sales of cigarettes per adult per day (International Smoking Statistics (2017)) ",
                     hover_name="Entity",
                     animation_frame="Year",
                     color_continuous_scale="Reds",
                     title="Sales of cigarettes per adult per day (International Smoking Statistics (2017)) ")

# Update the layout
    fig1.update_geos(projection_type="equirectangular",
                 showcountries=True,
                 showcoastlines=True)
    fig1.update_layout(legend_title_text="Cigarettes per Adult per Day",
                   coloraxis_colorbar=dict(title="Number of Cigarettes"))

# Adjust the size and aspect ratio of the plot figure
    fig1.update_layout(height=800, width=800, autosize=False, margin=dict(l=0, r=0, t=40, b=0))

# Display the choropleth map
    st.plotly_chart(fig1)

    
#2nd graph:
   
    # Load the dataset
    data2 = pd.read_csv("/Users/tijanmoghnieh/Desktop/death-rate-smoking.csv")  # Replace with the actual file path of your data

# Define the selected countries
    selected_countries = ["Spain", "Japan", "Austria", "Germany", "France", "United States", "Switzerland"]

# Filter the data for the selected countries
    filtered_data2 = data2[data2['Entity'].isin(selected_countries)]

# Define the range of years
    min_year2 = filtered_data2["Year"].min()
    max_year2 = filtered_data2["Year"].max()

# Get the selected year range from the slider
    selected_years2 = st.slider("Select Year Range", min_value=min_year2, max_value=max_year2, value=(min_year2, max_year2))

# Filter the data based on the selected year range
    filtered_data2_years = filtered_data2[(filtered_data2["Year"] >= selected_years2[0]) & (filtered_data2["Year"] <= selected_years2[1])]

# Create the heatmap
    fig2 = go.Figure(data=go.Heatmap(
    z=filtered_data2_years['Deaths - Cause: All causes - Risk: Smoking - Sex: Both - Age: Age-standardized (Rate)'].values,
    x=filtered_data2_years['Year'],
    y=filtered_data2_years['Entity'],
    colorscale='Reds',
    colorbar=dict(title='Death rate')
))

# Update the title and axis labels
    fig2.update_layout(
    title='Death rate from smoking, {} to {}'.format(selected_years2[0], selected_years2[1]),
    xaxis=dict(title='Year'),
    yaxis=dict(title='Country')
)

# Show the heatmap
    st.plotly_chart(fig2)

# Data and visualization for Obesity tab
elif selected_tab == "Obesity":
    st.title("Obesity")

# Load the dataset for obesity

    data3 = pd.read_csv("/Users/tijanmoghnieh/Desktop/death-rate-from-obesity.csv")
    
    # Page title
    st.subheader("Death Rate from Obesity")
    # Define the selected countries
    selected_countries = ["Spain", "Japan", "Austria", "Germany", "France", "United States", "Switzerland"]

    # Filter the data for the selected countries
    filtered_data3 = data3[data3['Entity'].isin(selected_countries)]

    # Define the range of years
    min_year3 = filtered_data3["Year"].min()
    max_year3 = filtered_data3["Year"].max()

    # Get the selected year range from the slider
    selected_years3 = st.slider("Select Year Range for Homicide", min_value=min_year3, max_value=max_year3, value=(min_year3, max_year3))

    # Filter the data based on the selected year range
    filtered_data3_years = filtered_data3[(filtered_data3["Year"] >= selected_years3[0]) & (filtered_data3["Year"] <= selected_years3[1])]

    # Plot the line graph for homicide
    fig3 = px.line(filtered_data3_years, x="Year", y="Deaths - Cause: All causes - Risk: High body-mass index - Sex: Both - Age: Age-standardized (Rate)", color="Entity")

    # Apply color mapping and customize line and marker properties
    for trace in fig3.data:
         entity = trace.name
         if entity == "United States":
             trace.line.color = "red"
             trace.mode = "lines+markers"
             trace.marker.symbol = "circle"
             trace.marker.size = 6
         else:
             trace.line.color = "gray"
             trace.mode = "lines"

    # Update the title and axis labels
    fig3.update_layout(title="Death Rate from Obesity, {} to {}".format(selected_years3[0], selected_years3[1]),
                        xaxis_title="Year",
                        yaxis_title="Death Rate")

    # Remove the gray background
    fig3.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')

    st.plotly_chart(fig3)




# Data and visualization for Homicide tab
elif selected_tab == "Homicide":
    st.title("Homicide")


    # Load the homicide data
    data3 = pd.read_csv("/Users/tijanmoghnieh/Desktop/homicide-rate.csv")
    # Page title
    st.subheader("Death Rate from Homicide")

    # Define the selected countries
    selected_countries = ["Spain", "Japan", "Austria", "Germany", "France", "United States", "Switzerland"]

    # Filter the data for the selected countries
    filtered_data3 = data3[data3['Entity'].isin(selected_countries)]

    # Define the range of years
    min_year3 = filtered_data3["Year"].min()
    max_year3 = filtered_data3["Year"].max()

    # Get the selected year range from the slider
    selected_years3 = st.slider("Select Year Range for Homicide", min_value=min_year3, max_value=max_year3, value=(min_year3, max_year3))

    # Filter the data based on the selected year range
    filtered_data3_years = filtered_data3[(filtered_data3["Year"] >= selected_years3[0]) & (filtered_data3["Year"] <= selected_years3[1])]

    # Plot the line graph for homicide
    fig3 = px.line(filtered_data3_years, x="Year", y="Deaths - Interpersonal violence - Sex: Both - Age: All Ages (Rate)", color="Entity")

    # Apply color mapping and customize line and marker properties
    for trace in fig3.data:
        entity = trace.name
        if entity == "United States":
            trace.line.color = "red"
            trace.mode = "lines+markers"
            trace.marker.symbol = "circle"
            trace.marker.size = 6
        else:
            trace.line.color = "gray"
            trace.mode = "lines"

    # Update the title and axis labels
    fig3.update_layout(title="Death Rate from Homicide, {} to {}".format(selected_years3[0], selected_years3[1]),
                       xaxis_title="Year",
                       yaxis_title="Death Rate")

    # Remove the gray background
    fig3.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')

    st.plotly_chart(fig3)
    
#Opioid overdoses 
    

# Data and visualization for Opioid Overdoses tab
elif selected_tab == "Opioid overdoses":
    st.title("Opioid overdoses ")

    # Load the dataset for opioid overdoses
    data_opioid = pd.read_csv("/Users/tijanmoghnieh/Desktop/death-rate-from-opioid-use.csv")
    # Page title
    st.subheader("Death Rate from Opioid Overdoses ")
    # Create the choropleth map
    fig_opioid = px.choropleth(data_opioid,
                               locations="Code",
                               locationmode="ISO-3",
                               color="Deaths - Opioid use disorders - Sex: Both - Age: Age-standardized (Rate)",
                               hover_name="Entity",
                               animation_frame="Year",
                               color_continuous_scale="Reds")

    # Update the layout
    fig_opioid.update_geos(projection_type="equirectangular",
                           showcountries=True,
                           showcoastlines=True)
    fig_opioid.update_layout(legend_title_text="Death Rate",
                             coloraxis_colorbar=dict(title="Rate per 100,000 population"))

    # Adjust the size and aspect ratio of the plot figure
    fig_opioid.update_layout(height=900, width=900, autosize=False, margin=dict(l=0, r=0, t=40, b=0))

    # Display the choropleth map
    st.plotly_chart(fig_opioid)
    
#Road Injuries 
# Data and visualization for Road Injuries tab

# Data and visualization for Road Injuries tab
elif selected_tab == "Road Injuries":
    st.title("Road Injuries")

    # Load the data
    data = pd.read_csv("/Users/tijanmoghnieh/Desktop/death-rates-road-incidents 2.csv")

    # Define the selected countries
    selected_countries = ["Spain", "Japan", "Austria", "Germany", "France", "United States", "Switzerland"]

    # Filter the data for the selected countries
    filtered_data = data[data['Entity'].isin(selected_countries)]

    # Page title
    st.subheader("Road Injury Deaths by Country")

    # Define the range of years
    min_year = filtered_data['Year'].min()
    max_year = filtered_data['Year'].max()

    # Select years using a range slider
    selected_years = st.slider("Select Year Range", min_value=min_year, max_value=max_year, value=(min_year, max_year))

    # Filter data for the selected year range
    filtered_data_years = filtered_data[(filtered_data['Year'] >= selected_years[0]) & (filtered_data['Year'] <= selected_years[1])]

    # Create a pie chart
    fig = px.pie(filtered_data_years, values='Deaths - Road injuries - Sex: Both - Age: Age-standardized (Rate)',
                 names='Entity', title="Road Injury Deaths", color_discrete_sequence=px.colors.sequential.Reds)

    # Update the layout
    fig.update_traces(textposition='inside', textinfo='percent+label')

    # Show the pie chart
    st.plotly_chart(fig)
    
    
    




   




