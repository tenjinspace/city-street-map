import geopandas as gpd
import matplotlib.pyplot as plt
import streamlit as st

def main():
    st.title("City Street Map")
    st.markdown("with [Geopandas](https://geopandas.org/) and [Streamlit](https://streamlit.io/)")

    st.header("Genoa, IT")

    # Import all roads IT
    map_df = gpd.read_file('roads.shp')
    # Show data format
    map_df.head()

    # Set image properties
    fig, ax = plt.subplots(1, figsize=(10,14))
    map_df.plot(cmap='Wistia', ax=ax)
    ax.axis('off')

    genoa = {'lat': 44.4030, 'lon': 8.9449}

    # Set coordinates to match Genoa
    ax.set_xlim(genoa['lon']-0.0180, genoa['lon']+0.0180)
    ax.set_ylim(genoa['lat']-0.0248, genoa['lat']+0.0248)
    ax.set_aspect('equal')

    # Plot the street map of Utrecht
    plt.show()




    

if __name__ == "__main__":
    main()
