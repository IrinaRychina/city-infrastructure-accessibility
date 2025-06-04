# city-infrastructure-accessibility
![Python](https://img.shields.io/badge/Python-3.10-blue)
![Status](https://img.shields.io/badge/Status-In%20Progress-yellow)

Analyzing wheelchair accessibility in urban environments using Python

# Urban Accessibility for People with Limited Mobility

This project explores how accessible urban infrastructure (such as buildings, public toilets, and shared spaces) is for people with limited mobility. It uses OpenStreetMap data and Python tools for analysis and visualization.

## Planned Features:
- Data collection via Overpass API
- Insights into the state of urban accessibility

## Technologies:
Python, OpenStreetMap

## Project Progress

- [x] Idea formulated  
- [x] Initial Overpass API query created  
- [x] Create development environment in Docker 
- [ ] Data processing and filtering
- [ ] Analysis and insights  
- [ ] Presentation of results  

### Future Ideas

- Add filtering by object type (e.g. restaurants, schools, pharmacies)
- Evaluate accessibility by district and create a ranking
- Compare accessibility across different cities

## Пример карты
![Map Screenshot](./screenshots/map_example.png)

## Technical Setup & Usage Guide

To build the Docker image, navigate to the project directory on your local machine and run:
> docker build -t city-accessibility .  

To execute the script inside the container, run:
> docker run --rm city-accessibility  

For debugging or accessing output files, you can mount the local data folder:
> docker run --rm -v "${pwd}/data:/app/data" city-accessibility

This will create a file named wheelchair_accessible.csv in your local data directory.
