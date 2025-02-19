import leafmap.maplibregl as leafmap
import os
import solara
import pandas as pd

zoom = solara.reactive(8)
center = solara.reactive((41.5, 14))
os.environ["MAPTILER_KEY"] = "N84VgiZTD01zt0weKWVc"
fname= 'https://raw.githubusercontent.com/pd-allen/pd-allen.github.io/main/docs/8thHussarsItaly.xlsx'

data =  pd.read_excel(fname,dtype={'Comments': str},na_values=[''])


@solara.component
def Page():
    with solara.Column(style={"min-width": "800px"}):
        solara.Text(
            "Not fully working yet. Try resizing the window to use the full width."
        )

        # solara components support reactive variables
        solara.SliderInt(label="Zoom level", value=zoom, min=1, max=20)
        # using 3rd party widget library require wiring up the events manually
        # using zoom.value and zoom.set
        m = leafmap.Map(center=[data['Longitude'][14],data['Latitude'][14]], zoom=14, pitch=60, style="3d-terrain")
        m.add_basemap("OpenTopoMap",opacity=0.5)
        #m.add_basemap("Esri.WorldStreetMap",opacity=0.5)
        m.add_layer_control()
        m
       
        solara.Text(f"Zoom: {zoom.value}")
        solara.Text(f"Center: {center.value}")