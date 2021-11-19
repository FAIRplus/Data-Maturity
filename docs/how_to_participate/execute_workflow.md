---
layout: default
title: Execute a workflow
parent: How to Participate
nav_order: 5
---

# Execute a workflow

To execute your workflows created using the [Execute a workflow](/docs/how_to_participate/create_workflow.md) section,
you will use [WfExS-backend](https://github.com/inab/WfExS-backend).

**WfExS-backend** is a high-level workflow execution command line program that consumes and creates [RO-Crates](https://www.researchobject.org/ro-crate/#what-is-ro-crate),
focusing on the interconnection of content-sensitive research infrastructures for handling sensitive human data analysis 
scenarios. WfExS-backend delegates workflow execution of existing workflow engines, and it is designed to facilitate 
more secure and reproducible workflow executions to promote analysis reproducibility and replicability. Secure 
executions are achieved using FUSE encrypted directories for non-disclosable inputs, intermediate workflow execution 
results and output files.

## Download from GitHub

```bash
git clone https://github.com/inab/WfExS-backend.git
cd WfExS-backend
```

## Install and Setup

### Core dependencies

WfExS-backend is written for Python 3.6 and later.

* In order to install the core dependencies you need `pip` and `venv` modules.
  - `pip` is available in many Linux distributions (Ubuntu packages `python3-pip`, CentOS EPEL package `python-pip`), 
  and also as [pip](https://pip.pypa.io/en/stable/) Python package.
  - `venv` is also available in many Linux distributions (Ubuntu package `python3-venv`). In some of them is integrated 
  into the Python 3.5 (or later) installation.

* The creation of a virtual environment where to install WfExS-backend dependencies is done running:
  
```bash
python3 -m venv .pyWEenv
source .pyWEenv/bin/activate
pip install --upgrade pip wheel
pip install -r requirements.txt
```

### Software dependencies

As there are additional software dependencies beyond core ones, which are needed depending on the setup of the instance. 
There is an automated installer at [installer.bash](https://github.com/inab/WfExS-backend/blob/main/installer.bash), 
which assumes both python3 and its pip and venv counterparts are properly installed. It installs both core dependencies, 
and it fetches and installs:

  * OpenJDK: needed by Nextflow.
  * gocryptfs: needed by secure directories feature.
  * A static bash copy: needed by Nextflow runner to monkey-patch some containers which do not have bash, or whose bash copy is buggy.

Depending on the local setup, some other external tools or container technologies are needed in several stages of the 
code. Please, install them, using either native packages (for instance, from your Linux distribution) or by hand and 
later set their path in the local configuration file you are using:

* [singularity](https://sylabs.io/singularity/): when local installation is set up to use singularity, 3.5 or later.
  
* [docker](https://www.docker.com/): when local installation is set up to use docker. Not all the combinations of 
workflow execution engines and secure or paranoid setups support it.
  
## Workflow config file

The WfExS-backend uses a workflow configuration file that is a YAML formatted file which describes the workflow before 
being executed, like where inputs are located and can be fetched, the security contexts to be used on specific 
inputs to get those controlled access resources, the parameters, the outputs to capture, ... for more information about
the fields you can add see [stage-definition_schema.md](https://github.com/inab/WfExS-backend/blob/main/docs/schemas/stage-definition_schema.md).

### WfExS-config-replicator usage

Example and usage of this tool, which helps to generate a workflow configuration file from a template and an Excel or 
CSV file with the fields to substitute:

```bash
python WfExS-config-replicator.py -W tests/wetlab2variations_execution_nxf.wfex.stage --params-file tests/wetlab2variations_execution_nxf.variations.xlsx tests/generated
```

```
python WfExS-config-replicator.py -h
usage: WfExS-config-replicator.py [-h] -W WORKFLOWCONFIGFILENAME
                                  (-p PARAM_NAME VALUE | --params-file PARAMS_FILES)
                                  [--fname-template FILENAME_TEMPLATE]
                                  [--symbol-template PARAMSYMBOLTEMPLATE]
                                  [destdir]

WfExS config replicator

positional arguments:
  destdir               Directory where all the variations of the workflow
                        configuration file are going to be created

optional arguments:
  -h, --help            show this help message and exit
  -W WORKFLOWCONFIGFILENAME, --workflow-config WORKFLOWCONFIGFILENAME
                        Workflow configuration file, to be used as template
  -p PARAM_NAME VALUE, --param PARAM_NAME VALUE
                        Param to substitute. Repeat to tell arrays of values
  --params-file PARAMS_FILES
                        Tabular params file with the different variations
  --fname-template FILENAME_TEMPLATE
                        Filename template for the created workflows
  --symbol-template PARAMSYMBOLTEMPLATE
```

## Usage

```bash
python WfExS-backend.py -d -L test/local_config.yaml -W test/<workflow-name>_execution_nxf.wfex.stage execute
```