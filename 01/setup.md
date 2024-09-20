# Setup
Micromamba is a simple way to create a virtual environment. It will become handy later on for managing nvidia driver dependencies. Lets create a simple environment:
```console
micromamba create -n ml-zoomcamp python=3.11
micromamba activate ml-zoomcamp
micromamba install numpy pandas scikit-learn seaborn jupyter
```
We need to install a Jupyter kernel spec for the new environment:
```console
micromamba run -n ml-zoomcamp python -m ipykernel install --user --name ml-zoomcamp --display-name "Python 3.11 (ml-zoomcamp)"
```
Now move into the Github project https://github.com/tomtuamnuq/ml-zoomcamp
```console
cd ml-zoomcamp
mkdir 01
micromamba list > 01/micromamba_list.txt
```
Download the files for the first homework and do the tasks:
```console
cd 01
wget https://raw.githubusercontent.com/alexeygrigorev/datasets/master/laptops.csv
jupyter lab
```
