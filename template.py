import os
from pathlib import Path

package_name = "damond_pred"

list_of_files = [
   ".github/workflows/.gitkeep",
   "src/__init__.py",
   "src/components/__init__.py", 
   "src/components/data_ingestion.py", 
   "src/components/data_transformation.py", 
   "src/components/model_evaluation.py", 
 "src/components/model_trainer.py", 
  "src/logger/__init__.py",
  "src/logger/logging.py",
   "src/exception/__init__.py",
    "src/exception/exception.py",
     
   "tests/__init__.py",
   "tests/unit/__init__.py",
   "tests/unit/unit.py",
   "tests/integration/__init__.py",
   "tests/integration/int.py",
   "init_setup.sh",
   "requirements.txt", 
   "requirements_dev.txt",
   "setup.py",
   "setup.cfg",
   "pyproject.toml",
   "tox.ini",
   "experiments/experiments.ipynb", 
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass # create an empty file