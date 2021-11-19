---
layout: default
title: Create a workflow
parent: How to Participate
nav_order: 4
---

# Create a workflow

You are probably here because you want to take your models and put them in a functional workflow so that it takes care 
of their execution. You have come to the right place.

### A practical example

The objective of this tutorial is to introduce you the concepts of [Nextflow](https://www.nextflow.io/) workflows so 
that you can create a new workflow by yourself. You will do this through the process of creating a simple workflow, 
containing only one container, and referencing an existing Nextflow workflow. This existing workflow was developed for 
the [COSIFER](https://github.com/PhosphorylatedRabbits/cosifer) tool and is implemented in the 
[iPC Workflows for VRE](https://github.com/inab/ipc_workflows/tree/main/cosifer/nextflow) repository.

### Prerequisites

This tutorial assumes that you have [Nextflow](https://www.nextflow.io), [docker](https://docs.docker.com/get-docker/) 
and [git](https://git-scm.com/downloads) installed.

## Nextflow setup

### Clone a GitHub repository

Let's start by setting up a folder, so you can use version control. You must create a clone in your local machine of 
the [iPC Workflows for VRE](https://github.com/inab/ipc_workflows) repository using the command:

```bash
git clone --single-branch --branch dream-challenge https://github.com/inab/ipc_workflows.git
```

Next, you need to create a folder for your workflow inside the `dream_challenge` folder. Our recommendation to name the 
new folder is giving it the name of the model  which will be executed by the workflow resulting from this tutorial. 

### Files

Every Nextflow workflow requires two main files.

- nextflow.nf:
  - The nextflow.nf file contains the main workflow script that calls the processes.
  - It doesn't have to be called nextflow.nf, but it is a standard practice to do so.
- nextflow.config:
  - The nextflow.config file contains default parameters to use in the workflow.

```bash
touch nextflow.nf nextflow.config
```

Now, your folder should contain the following files:

```bash
ls 
nextflow.nf nextflow.config
```

## Nextflow config file

The Nextflow config file is `nextflow.config`. In here, you can set default global parameters for workflow (params), 
process, manifest, executor, profiles, docker, singularity, timeline, report and more.

For now, copy the following [example](https://github.com/inab/ipc_workflows/blob/main/cosifer/nextflow/nextflow.config) 
into the `nextflow.config` file:

```bash
manifest {
  name = 'COSIFER - COnSensus Interaction Network InFErence Workflow'
  homePage = 'https://github.com/inab/ipc_workflows/tree/main/cosifer/nextflow'
  defaultBranch = 'master'
  mainScript = 'nextflow.nf'
  nextflowVersion = '>=19.10.0'
}

params {
  data_matrix = "${baseDir}/test/data_matrix.csv"
  outputsDir = "${baseDir}/test/results/"
  index_col = ""
  hallmark_gene_sets_file = ""
  sep = "\t"
  samples_on_rows = ""
}

docker {
  runOptions='-u $(id -u):$(id -g)'
  enabled = true
}
```

- **manifest**: The manifest configuration allows you to define certain required metadata information when publishing 
your workflow to *GitHub*, *Bitbucket*, or *Gitlab*, or when running your workflow. The following settings that you need
to modify:
  - name: The project short name.
  - homePage: The project home page URL (e.g. **https://github.com/inab/ipc_workflows/tree/dream-challenge/your-folder-name**)
  - defaultBranch: The Git repository default branch (e.g. dream-challenge)
  - mainScript: The project main script (e.g. nextflow.nf)
  - nextflowVersion: The minimum required Nextflow version. **Not need to be modified**.
- **params**: The params allows you to define parameters, usually input and output values, to be accessible in the 
workflow script.
- **docker**: The docker configuration control how `Docker` containers are executed by Nextflow. **Not need to be modified**.

## Nextflow workflow

Copy the following [example](https://github.com/inab/ipc_workflows/blob/main/cosifer/nextflow/nextflow.nf)
into the `nextflow.nf` file:

```bash
#!/usr/bin/env nextflow

data_matrix = file(params.data_matrix)
outdir = file(params.outputsDir)
result = outdir.mkdirs()
println result ? "Created directory $outdir" : "Cannot create output directory: $outdir"

separator = params.sep
index_col = params.index_col
gmt_filepath = file(params.hallmark_gene_sets_file != '' ? params.hallmark_gene_sets_file : '.empty.')
samples_on_rows = params.samples_on_rows

// We are telling we want the result in this specific subdirectory
// of the outdir
// When empty string is no subdir
cosifer_input = Channel.of([data_matrix,outdir,''])

process cosifer {
  container "tsenit/cosifer:b4d5af45d2fc54b6bff2a9153a8e9054e560302e"

  publishDir "${destdir}", saveAs: { filename -> (destsubdir!='' ? "${destsubdir}/" : '') + filename.minus('resdir/') }

  input:
    tuple matrix, destdir, val(destsubdir) from cosifer_input
    file gmt_filepath
    val separator
    val index_col
    val samples_on_rows

  output:
    path "resdir/**" into cosifer_output

  """
  cosifer -i "${matrix}" "--sep=${separator}" ${index_col!='' ? '--index ' + index_col : ''}  ${gmt_filepath.name != '.empty.' ? '--gmt_filepath ' + gmt_filepath : ''} -o "resdir" ${samples_on_rows ? '--samples_on_rows' : ''}
  """
}

cosifer_output.subscribe{ result -> println "Output:" + result.name }
```
