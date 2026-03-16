import streamlit as st
from map_coloring import solve_map_coloring, demo_6_countries

st.set_page_config(page_title="CSP - Map Coloring", layout="centered")

st.title("CSP Solver - Map Coloring")
st.write("Backtracking + MRV heuristic")

countries, neighbors = demo_6_countries()

st.subheader("Map (6 countries)")
st.write("Countries:", countries)
st.write("Adjacency (neighbors):")
st.json(neighbors)

st.subheader("Choose number of colors")
num_colors = st.selectbox("Colors", [3, 4], index=0)

colors = ["Red", "Green", "Blue"] if num_colors == 3 else ["Red", "Green", "Blue", "Yellow"]

if st.button("Solve Map Coloring"):
    sol = solve_map_coloring(countries, neighbors, colors)
    if sol is None:
        st.error("No solution found with selected colors.")
    else:
        st.success("Solution found!")
        st.table([{"Country": k, "Color": v} for k, v in sol.items()])
