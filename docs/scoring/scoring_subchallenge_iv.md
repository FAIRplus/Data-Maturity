---
layout: default
title: Scoring for subchallenge IV
parent: Scoring
nav_order: 3
---

## Scoring for subchallenge IV
In subchallenge IV we ask the participants to predict the median response of some cell lines in all the perturbed conditions. The root mean square error (RMSE) will be used to score the predictions. The RMSE will be computed in two steps, first the RMSE is computed for each cell line and for each of the perturbations (EGF or inhibition) across the time points, then the obtained RMSE values are averaged. In case of ties the same process as in subchallenge I will be followed.

### Code for scoring subchallenge IV
Below is the current status of scoring script for subchallenge IV, used for scoring the dry-runs. We keep the right to change the code and scoring metrics.

```
library(tidyverse)

# scores the subchallenge subchallenge IV
#' @param prediction_data_file path to prediction data file (.csv)
#' @param validation_data_file path to validation data file (.csv)
#' @description checks input for missing columns
#' check input for missing conditions (missing predicted cells)
#' computes root-mean square error by conditions, then averages these

score_subchallenge_4 <- function(prediction_data_file,validation_data_file){
	
	# load validation data
	validation_data <- read_csv (validation_data_file) 
	prediction_data <- read_csv(prediction_data_file)
	
	### Checking inputs -------------------
	# checking columns of input data table
	# HER2, PLCg2, cellID and fileID not included on purpose ! 
	required_columns <- c('cell_line','treatment', 'time',
						  'b.CATENIN', 'cleavedCas', 'CyclinB', 'GAPDH', 'IdU',
						  'Ki.67', 'p.4EBP1', 'p.Akt.Ser473.', 'p.AKT.Thr308.',
						  'p.AMPK', 'p.BTK', 'p.CREB', 'p.ERK', 'p.FAK', 'p.GSK3b',
						  'p.H3', 'p.JNK', 'p.MAP2K3', 'p.MAPKAPK2',
						  'p.MEK', 'p.MKK3.MKK6', 'p.MKK4', 'p.NFkB', 'p.p38',
						  'p.p53', 'p.p90RSK', 'p.PDPK1', 'p.RB', 
						  'p.S6', 'p.S6K', 'p.SMAD23', 'p.SRC', 'p.STAT1',
						  'p.STAT3', 'p.STAT5') 
	
	if(!all(required_columns %in% names(prediction_data))) {
		stop(paste0("missing columns detected. Required columns: ", paste(required_columns,collapse = ", ")))
	}
	prediction_data = prediction_data %>% select(required_columns)
	# as we agreed, we remove plcg and her2 from the validation data:
	validation_data = validation_data %>% select(required_columns)
	
	# checking for any missing conditions
	required_conditions <- validation_data %>% select(cell_line,treatment,time) %>% unique()
	predicted_conditions <- prediction_data %>% select(cell_line,treatment,time)
	
	missing_conditions = anti_join(required_conditions,predicted_conditions,by = c("cell_line", "treatment", "time"))
	
	if(nrow(missing_conditions)>0){
		print("table showing the conditions missing from the submitted predictions:")
		print(missing_conditions %>% select(c("cell_line", "treatment", "time")))
		stop("missing predictions detected for above conditions")	
	} 
	
	
	### Formating -------------------------
	# join the test and validation data
	
	combined_data = full_join(prediction_data %>% gather(marker,prediction,-cell_line, -treatment, -time ),
							  validation_data %>% gather(marker,test,-cell_line, -treatment, -time ),
							  by=c("cell_line", "treatment", "time","marker"))
	
	### Calculate score --------------------
	# calculate the  distance over all stats
	RMSE_cond = combined_data %>% group_by(cell_line,treatment,marker) %>% 
		summarise(RMSE = sqrt(sum((test - prediction)^2)/n())) 
	

	final_score = mean(RMSE_cond$RMSE)
}
```