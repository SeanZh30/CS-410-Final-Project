# CS410 Final Project

Welcome to our GitHub repository for the CS410 Final Project! This project focuses on exploring different approaches to text classification and natural language processing (NLP). The repository includes implementations of three major methodologies:

1. **Traditional Machine Learning Models (LR and SVM)**
2. **GPT**
3. **BERT**

All code is organized within the `code` folder.

---

## Table of Contents
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Approaches and Methodologies](#approaches-and-methodologies)
  - [1. Traditional Machine Learning (LR and SVM)](#1-traditional-machine-learning-lr-and-svm)
  - [2. GPT](#2-gpt)
  - [3. BERT](#3-bert)
- [Results](#results)
- [Contributors](#contributors)

---

## Project Structure
The repository is structured as follows:

```
.
├── code
│   ├── tradition-LR-SVM
│   │   ├── preprocess.py      # Preprocessing scripts
│   │   ├── lr_svm.py          # Logistic Regression and SVM implementation
│   │   └── utils.py           # Utility functions
│   ├── GPT
│   │   ├── run.py             # Run the model
│   │   ├── fewshot.prompt     # Prompt for fewshot detection
│   │   └── zeroshot.prompt    # Prompt for zeroshot detection
│   ├── BERT
│   │   ├── bert.ipynb         # Jupyter notebook for BERT experimentation
│   │   ├── datamodule.py      # Data preparation and loading module
│   │   ├── inference.py       # Inference script for BERT
│   │   ├── model.py           # BERT model definition
│   │   ├── run.py             # Main script to fine-tune and evaluate BERT
│   │   └── utils.py           # Utility functions for BERT
├── data
│   ├── train.csv              # Training dataset
│   ├── test.csv               # Testing dataset
│   └── README.md              # Description of datasets
├── README.md                   # Project description and instructions
└── requirements.txt            # Python dependencies
```

---

## Installation

To get started, clone the repository and install the required dependencies:

```bash
# Clone the repository
$ git clone https://github.com/SeanZh30/CS-410-Final-Project.git
$ cd CS-410-Final-Project

# Install dependencies
$ pip install -r requirements.txt
```

---

## Usage

### Running the Traditional Machine Learning Models (LR and SVM)

```bash
$ jupyter notebook code/tradition-LR-SVM/Tradition_LR_SVM.ipynb
```

### Running GPT

```bash
# Run GPT with customizable models and parameters
$ python code/GPT/run.py
```
The run.py script supports selecting different models and parameters, including few-shot and zero-shot settings.

### Running BERT

```bash
# Run BERT with customizable models and parameters
$ python code/BERT/run.py
```

The `run.py` script supports running BERT models with the following options:
- Model: `FacebookAI/roberta-base` (RoBERTa)
- Model: `microsoft/deberta-base` (DeBERTa)


---

## Contributors

- **Sean Zhang**
- **Yiming Niu**
- **Leyi Zhang**
- **Yibin Huang**

---

Feel free to contribute or raise issues for improvements. Thank you for exploring our CS410 final project!

