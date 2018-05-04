# Deep RL Quadcopter Controller

*Teaching a Quadcopter How to Fly!*

Designed an agent to fly a quadcopter, and then train it using a reinforcement learning algorithm.

## Project Instructions

1. Clone the original repository and navigate to the downloaded folder

```
git clone https://github.com/udacity/RL-Quadcopter-2.git
cd RL-Quadcopter-2
```

1.1. Clone the original repository and navigate to the downloaded folder

```
git clone https://github.com/boscoybarra/DDPG_Quadcopter_Project_RL
cd DDPG_Quadcopter_Project_RL
```

2. Create and activate a new environment.

```
conda create -n quadcop python=3.6 matplotlib numpy pandas ipykernel keras
source activate quadcop
```

3. Create an [IPython kernel](http://ipython.readthedocs.io/en/stable/install/kernel_install.html) for the `quadcop` environment. 
```
python -m ipykernel install --user --name quadcop --display-name "quadcop"
```

4. Open the notebook.
```
jupyter notebook Quadcopter_Project.ipynb
```

5. Before running code, change the kernel to match the `quadcop` environment by using the drop-down menu (**Kernel > Change kernel > quadcop**). Then, follow the instructions in the notebook.

6. You will likely need to install more pip packages to complete this project.  Please curate the list of packages needed to run your project in the `requirements.txt` file in the repository.