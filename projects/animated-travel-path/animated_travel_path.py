# animated_travel_path.py

# Importación de librerías para mapas interactivos -> Importing libraries for interactive maps
import folium
from folium.plugins import AntPath

# 1. Configuración del mapa base centrado entre Casanare y Cundinamarca -> Base map setup centered between Casanare and Cundinamarca
map_center: list[float] = [4.97, -73.24]
travel_map = folium.Map(
    location=map_center, 
    zoom_start=8,
    tiles="https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}",
    attr="Esri World Imagery"
)

# 2. Definición de la secuencia de coordenadas Yopal -> Bogotá (Latitud, Longitud) -> Definition of coordinate sequence Yopal -> Bogota (Latitude, Longitude)
# Ruta: Yopal -> Aguazul -> Tauramena -> Monterrey -> Sisga -> Bogotá
route_coordinates: list[list[float]] = [
    [5.3378, -72.3959],  # Yopal (Casanare)
    [5.1728, -72.5471],  # Aguazul
    [5.0119, -72.7525],  # Tauramena
    [4.8778, -72.8972],  # Monterrey
    [5.0768, -73.7196],  # Represa del Sisga
    [4.6097, -74.0817]   # Bogotá (D.C.)
]

# 3. Creación de la ruta animada con el plugin AntPath -> Creation of animated route using AntPath plugin
AntPath(
    locations=route_coordinates,
    color="cyan",
    weight=6,
    delay=800,
    dash_array=[10, 20],
).add_to(travel_map)

# 4. Marcadores visuales de Origen y Destino -> Origin and Destination visual markers
folium.Marker(
    location=[5.3378, -72.3959],
    popup="Origen: Yopal, Casanare",
    icon=folium.Icon(color="green", icon="info-sign")
).add_to(travel_map)

folium.Marker(
    location=[4.6097, -74.0817],
    popup="Destino: Bogotá D.C.",
    icon=folium.Icon(color="red", icon="info-sign")
).add_to(travel_map)

# 5. Guardar el mapa como archivo HTML interactivo -> Save map as interactive HTML file
output_file: str = "travel_path.html"
travel_map.save(output_file)

print(f"¡Mapa de Yopal a Bogotá generado con éxito! Abre '{output_file}' en tu navegador web -> Yopal to Bogota map generated successfully! Open '{output_file}' in your web browser.")
