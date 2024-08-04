# The Numenta Anomaly Benchmark (NAB) modified for the evaluation of VMFT-LAD

This repository contains the modified [Numenta Anomaly Benchmark (NAB) v1.1](https://github.com/numenta/NAB) code with
our dataset and labels used to evaluate our model, VMFT-LAD along with 4 other models implemented
in the original NAB repo.

## Scoreboard

The NAB scores for all evaluated models on our VM failure log dataset, under 2 different evaluation criterion,

### Criteria-1: relaxed

- The model is expected to detect failure indicators after the fault injection point and even within the post-failure region.

| Detector                                                                   | Standard Profile | Reward Low FP | Reward Low FN |
| -------------------------------------------------------------------------- | ---------------- | ------------- | ------------- |
| [VMFT-LAD](#)                                                              | 98.16            | 97.77         | 98.44         |
| [Numenta HTM](https://github.com/numenta/nupic)                            | 66.63            | 61.04         | 71.64         |
| [KNN CAD](https://github.com/numenta/NAB/tree/master/nab/detectors/knncad) | 32.13            | -22.05        | 42.32         |
| [EXPoSE](https://arxiv.org/abs/1601.06602v3)                               | 42.32            | 37.07         | 67.33         |
| [ARTime](https://github.com/markNZed/ARTimeNAB.jl)                         | 73.98            | 56.92         | 77.89         |
| [DeepLog](https://users.cs.utah.edu/~lifeifei/papers/deeplog.pdf)          | 71.82            | 43.75         | 76.06         |

### Criteria-2: strict

- Requires the model to detect failures before the failure point (Early failure detection).

| Detector                                                                   | Standard Profile | Reward Low FP | Reward Low FN |
| -------------------------------------------------------------------------- | ---------------- | ------------- | ------------- |
| [VMFT-LAD](#)                                                              | 90.74            | 90.36         | 89.67         |
| [Numenta HTM](https://github.com/numenta/nupic)                            | 21.52            | 16.22         | 3.13          |
| [KNN CAD](https://github.com/numenta/NAB/tree/master/nab/detectors/knncad) | 1.47             | -54.94        | 0.21          |
| [EXPoSE](https://arxiv.org/abs/1601.06602v3)                               | 52.50            | 18.42         | 56.17         |
| [ARTime](https://github.com/markNZed/ARTimeNAB.jl)                         | 48.53            | 26.99         | 46.55         |
| [DeepLog](https://users.cs.utah.edu/~lifeifei/papers/deeplog.pdf)          | 71.50            | 43.30         | 75.79         |

## Dataset

The evaluation dataset contains a corpus of 695 timeseries data files simulating different VM failure scenarios,

| Dataset name | Description                                               | File count |
| ------------ | --------------------------------------------------------- | ---------- |
| Benign       | Normal state dataset that does not contain any VM failure | 152        |
| HDD          | Simulated short-term HDD failures using SCSI_debug module | 134        |
| Buffer I/O   | Simulated buffer I/O error                                | 144        |
| CPU          | CPU over-allocation failure dataset                       | 128        |
| OOM          | Out of Memory failure dataset                             | 137        |

- The _master_ branch contains the data labels for criteria-1: relaxed.
- For the data and labels of criteria-2: strict, switch to _eval-failure_ branch.

## Installing and running

### Initial requirements

You need to manually install the following:

- [Python 3.6](https://www.python.org/download/)
- [pip](https://pip.pypa.io/en/latest/installing.html)
- [NumPy](http://www.numpy.org/)

#### Download this repository

Use the Github links provided in the right sidebar.

#### Install NAB

##### Pip

From inside the checkout directory:

    pip install -r requirements.txt
      pip install . --user

If you want to manage dependency versions yourself, you can skip dependencies
with:

    pip install . --user --no-deps

If you are actively working on the code and are familiar with manual
PYTHONPATH setup:

      pip install -e . --install-option="--prefix=/some/other/path/"

##### Anaconda:

    conda env create

##### Runing EXPoSE/KNN CAD

    cd /path/to/nab
    python run.py -d expose --detect  --windowsFile labels/combined_windows_new.json

This will run the EXPoSE detector (for KNN CAD replace 'expose' with 'knncad')

##### Running HTM (Python 2)

Instructions on how to run HTM can be found in the `nab/detectors/numenta` directory.

##### Running ARTime

    cd /path/to/nab
    cd docker
    docker-compose up

##### Run NAB optimization and scoring

    cd /path/to/nab
    python run.py -d vmft-lad,knncad,expose,numenta,ARTime --optimize --score --normalize --windowsFile labels/combined_windows_new.json --skipConfirmation
