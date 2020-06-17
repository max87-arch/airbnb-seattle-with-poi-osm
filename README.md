# Analysis of Airbnb Seattle Dataset combined with OSM
This repository contains the source code related to analyzing three business questions on Airbnb Seattle Dataset:

1. How much does cost accommodation in Seattle?
2. Which factors do they influence the price?
3. Do Poi influence the price?

## Getting Started

Before proceeding, you need [Airbnb Seattle Dataset](https://www.kaggle.com/airbnb/seattle/data). Please download the package, extract it and save listings.csv.

Clone this repository:

```bash
# download
git clone https://github.com/max87-arch/airbnb-seattle-with-poi-osm.git
cd airbnb-seattle-with-poi-osm

#put listings.csv inside the directory
mv /path/to/listings.csv .

# install dependencies
pip3 install pandas numpy matplotlib overpy geopandas seaborn sklearn

# Run jupyter
jupyter notebook
```

Inside the repository you find two python notebooks:

* AirBnBSeattle.ipynb contains the analysis of dataset
* ImportSeattlePoi.ipynb contains the procedure to generate the dataset seattle_poi.csv. If you decide to regenerate the dataset,  you would consider that this operation take many times.

## License
This code is release under [MIT License](LICENSE).
