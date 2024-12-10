# CS410 Final Project

Welcome to our GitHub repository for the CS410 Final Project! This project focuses on exploring different approaches to text classification and natural language processing (NLP). The repository includes implementations of three major methodologies:

1. **Traditional Machine Learning Models (LR and SVM)**
2. **BERT**
3. **GPT**


All code is organized within the `code` folder.

---

## Table of Contents
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Contributors](#contributors)

---

## Project Structure
The repository is structured as follows:

```
.
├── code
│   ├── tradition-LR-SVM
│   │   └── Traditional_LR_SVM.ipynb    # Jupyter notebook for traditional model
│   ├── GPT
│   │   ├── run.py                      # Run the model
│   │   ├── fewshot.prompt              # Prompt for fewshot detection
│   │   └── zeroshot.prompt             # Prompt for zeroshot detection
│   ├── BERT
│   │   ├── bert.ipynb                  # Jupyter notebook for BERT experimentation
│   │   ├── datamodule.py               # Data preparation and loading module
│   │   ├── inference.py                # Inference script for BERT
│   │   ├── model.py                    # BERT model definition
│   │   ├── run.py                      # Main script to fine-tune and evaluate BERT
│   │   └── utils.py                    # Utility functions for BERT
├── data
│   └── spam_ham_dataset.csv            # Training dataset
├── README.md                           # Project description and instructions
└── requirements.txt                    # Python dependencies
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

### 1. Running LR and SVM

```bash
$ jupyter notebook code/tradition-LR-SVM/Tradition_LR_SVM.ipynb
```

### 2. Running BERT

#### Data prepare

The required data is included in the `code/BERT/dataset` folder, along with preprocessing scripts. Preprocessed data is already uploaded, but in case of corruption, you can rerun `data process.ipynb` to split the data into `train`, `test`, and `val` sets.

#### Training Process

To train the model, open and run `bert.ipynb`. During training, checkpoints will be saved to the specified location, with results saved after each epoch. Before running, ensure you configure a Weights & Biases (wandb) account to log detailed training metrics such as loss and epochs. The training process will also automatically output the `test accuracy` and `train accuracy`, which are included in our final report.

```bash
# Run BERT with customizable models and parameters
$ jupyter notebook code/BERT/bert.ipynb
```

**Important Notes:**
- Training can be time-intensive, so we recommend running it on a GPU.
- Training two epochs typically takes about 40 minutes.

#### Configurations

In `run.py`, you can adjust the BERT configurations, including the following pretrained models:
- `FacebookAI/roberta-base` (RoBERTa)
- `microsoft/deberta-base` (DeBERTa)

Other pretrained models can also be used as backbones for further evaluation without modifying the subsequent MLP layers.


### 3. Running GPT

Before running, you need to configure your OpenAI API key in the environment or directly in `GPT/run.py` by setting:

```python
openai.api_key = "YOUR_API_KEY"
```

**Important Notes:**
- Ensure you install the `openai` library, version `0.28.0`, as the project uses this version. Using a different version may cause compatibility issues.

#### Execution

After configuring the API key, you can run the following command:

```bash
$ python code/GPT/run.py
```

You can also run ipynb file here:

```bash
$ jupyter notebook code/GPT/run.ipynb
```

The output will include accuracy metrics. You can also customize the prompts to test specific scenarios.

---

## Contributors

- **Yibin Huang**
- **Sean Zhang**
- **Yiming Niu**
- **Leyi Zhang**
  
---

Feel free to contribute or raise issues for improvements. Thank you for exploring our CS410 final project!

