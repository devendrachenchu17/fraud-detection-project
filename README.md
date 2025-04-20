# Fraud Detection Project

This project focuses on detecting fraudulent transactions using machine learning models and synthetic data generation techniques. It includes data preprocessing, model training using synthetic data generated through GANs (CTGAN, WGAN, SDGAN), and a Flask-based web interface for fraud prediction.

## Project Structure

```
Fraud detection project/
├── colab notebooks/         # Google Colab notebooks for training and data generation
│   ├── 8020ctganRF.ipynb
│   ├── CTGAN(t2_500).ipynb
│   ├── encoders_t2.ipynb
│   ├── gantest.ipynb
│   ├── Processing.ipynb
│   ├── sdgan (1).ipynb
│   └── WGAN.ipynb
│
├── data/                    # Real and synthetic datasets
│   ├── balanced SDGAN.csv
│   ├── balanced_WGAN.csv
│   ├── ctgan_t2_balanced.csv
│   ├── final_data.csv
│   ├── processed_fraud_data.csv
│   └── synthetic_fraud_dataset.csv
│
├── interface/               # Flask web app
│   ├── app.py
│   ├── preprocessing.py
│   ├── random_forest_fraud_model.pkl
│   ├── static/
│   │   ├── style.css
│   │   └── script.js
│   └── templates/
│       └── index.html
```

## Features

- Machine learning model trained on real and GAN-based synthetic transaction data
- Synthetic data generation using CTGAN, WGAN, and SDGAN architectures
- Exploratory data analysis and preprocessing performed in Google Colab
- Flask-based web interface for live fraud prediction
- Modular and well-structured codebase

## Colab Notebooks Summary

- `Processing.ipynb`: Data cleaning and transformation
- `CTGAN(t2_500).ipynb`, `8020ctganRF.ipynb`, `WGAN.ipynb`: Synthetic data generation and model training
- `encoders_t2.ipynb`, `gantest.ipynb`: Encoders and GAN experimentation

## Datasets

Located in the `data/` directory:

- `final_data.csv`: Cleaned version of real fraud dataset
- `ctgan_t2_balanced.csv`, `balanced_WGAN.csv`, `balanced SDGAN.csv`: Synthetic datasets generated using different GANs

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/fraud-detection-project.git
cd fraud-detection-project/interface
```

### 2. (Optional) Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate    # On Linux/macOS
venv\Scripts\activate     # On Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Flask Application

```bash
python app.py
```

### 5. Open in Browser

```
http://127.0.0.1:5000/
```

## Requirements

All required packages are listed in `requirements.txt`. Key dependencies include:

- Flask
- pandas
- scikit-learn
- numpy
- joblib

Install them using:

```bash
pip install -r requirements.txt
```

## License

This project is licensed under the MIT License.

## Author

Rishitha Muthyala,Devendra Chenchu,Akhila Sreeperumbuduru– Project Developers
"# fraud-detection-project" 
