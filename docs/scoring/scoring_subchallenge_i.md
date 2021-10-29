---
layout: default
title: Scoring for subchallenge I
parent: Scoring
nav_order: 1
---

## Scoring for subchallenge I
In subchallenge I, the participants predict missing cellular markers in individual cells that are identified by given cell-ids (cells are uniquely identified by the columns: cell_line, treatment, time, cellID and fileID). These cell-ids will be used to match the predicted single cells with the measured cells. We will compute the root-mean squared error (RMSE) between the predicted and measured marker values over the single cells in each of the conditions and cell lines. This will result in an RMSE value for each marker of each cell line, in each condition (treatment and time). Finally, we will take the mean of the RMSE values that will serve as a final score. In the unlikely case of ties, i.e. if the mean RMSE values of multiple participants are closer than a threshold value, we will compare the individual RMSE values over all the conditions. The submissions involved in the tie will be ranked by the RMSE in each of the conditions and the lowest overall ranked submission will be the winner.

![Figure 1](../../../assets/images/scoring/scoring_subchallenge_i/figure1_scoring_aim11.png)
_Figure 1. Scoring scheme for subchallenge I. The figure shows the scoring of a marker in a given condition. The predicted cells will be matched to the measured cells using the cell-id. Then the RMSE will be calculated based on the distance of the predicted marker level and the measured marker level across all single cells. The process will be repeated for each predicted marker, for each cell line, in each condition and time._

### Code for score
Below is the current status of scoring script for subchallenge I, used for scoring the dry-runs. We keep the right to change the code and scoring metrics.

```
# scores the subchallenge subchallenge I
#' @param prediction_data_file path to prediction data file (.csv)
#' @param validation_data_file path to validation data file (.csv)
#' @description checks input for missing columns
#' check input for missing conditions (missing predicted cells)
#' computes root-mean square error by conditions, then averages these

score_subchallenge_1 <- function(prediction_data_file,validation_data_file){
	
	# load validation data
	
	validation_data <- read_csv(validation_data_file)
	prediction_data <- read_csv(prediction_data_file)
	
	### Checking inputs -------------------
	# checking columns of input data table
	required_columns <- c( "cell_line", "treatment", "time", "cellID", "fileID" , "p.Akt.Ser473.", "p.ERK",  "p.HER2", "p.PLCg2","p.S6" ) 
	
	if(!all(required_columns %in% names(prediction_data))) {
		stop(paste0("missing columns detected. Required columns: ", paste(required_columns,collapse = ", ")))
	}
	prediction_data = prediction_data %>% select(required_columns)
	
	
	# checking for any missing cell-predictions
	missing_prediction_data = anti_join(validation_data,prediction_data,by = c("cell_line", "treatment", "time", "cellID", "fileID"))
	if(nrow(missing_prediction_data)>0){
		print(missing_prediction_data %>% select(c("cell_line", "treatment", "time", "cellID", "fileID")))
		stop("missing predictions detected for above conditions")	
	} 
	
	### Formating -------------------------
	# convert to long format
	reporters = c("p.Akt.Ser473.", "p.ERK",  "p.HER2", "p.PLCg2","p.S6")
	validation_data_long <- validation_data %>% gather(key = "marker",value = "test",reporters)
	prediction_data_long <- prediction_data %>% gather(key = "marker",value = "prediction",reporters)
	
	
	combined_data = validation_data_long %>%
		full_join(prediction_data_long, by=c("cell_line", "treatment", "time", "cellID", "fileID", "marker"))
	
	### Calculate score --------------------
	# calculate the RMSE for each condition 
	RMSE_cond = combined_data %>% group_by(cell_line,treatment,time,marker) %>% 
		summarise(RMSE = sqrt(sum((test - prediction)^2)/n())) 
	final_score = mean(RMSE_cond$RMSE)
}
```